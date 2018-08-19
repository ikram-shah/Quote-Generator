import gspread
from oauth2client.service_account import ServiceAccountCredentials 

from PIL import Image,ImageFont,ImageDraw

scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']

credentials= ServiceAccountCredentials.from_json_keyfile_name('quote-generator.json',scope)

gc=gspread.authorize(credentials)

worksheet=gc.open('Quote Generator (Responses)').sheet1

def text_wrap(text, font, max_width):
    lines = []
    if font.getsize(text)[0] <= max_width:
        lines.append(text) 
    else:
        words = text.split(' ')  
        i = 0
        while i < len(words):
            line = ''         
            while i < len(words) and font.getsize(line + words[i])[0] <= max_width:                
                line = line + words[i] + " "
                i += 1
            if not line:
                line = words[i]
                i += 1
            lines.append(line)    
    return lines

def quote_text(text,author,i):    
    # open the background file
    img = Image.new('RGB', (1000, 1000), color = (255,219,0))

    # size() returns a tuple of (width, height) 
    image_size = img.size 
    right_space=image_size[0]-30

    # create the ImageFont instance
    font_file_path = 'fonts/UbuntuMono-R.ttf'
    font = ImageFont.truetype(font_file_path, size=50, encoding="unic")
    
    lines = text_wrap(text, font, right_space)
    author_name=text_wrap(author,font,right_space)
    line_height = font.getsize('hg')[1]
    d = ImageDraw.Draw(img)
    
    x = 20
    y = 400
    for line in lines:
        # draw the line on the image
        d.text((x, y), line, fill=(68,68,68), font=font,align='center')
    
        # update the y position so that we can use it for next line
        y = y + line_height

    a = 20
    b = 940
    for auth in author_name:
        # draw the line on the image
        d.text((a, b), '--'+auth, fill=(68,68,68), font=font,align='center')
    
        # update the y position so that we can use it for next line
        b = b + line_height  

    logo=Image.open('logo.png','r')
    offset=(547,0)
    img.paste(logo,offset)

    img.save(str(i-1)+'.png', optimize=True)

for i in range(2,len(worksheet.get_all_values())+1):
    values_list = worksheet.cell(i,2).value
    valu=worksheet.cell(i,3).value

    print(values_list)
    print(valu)

    quote_text(values_list,valu,i)
