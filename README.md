# Quote-Generator

Grabs the Quote and Author name from Google Sheets (which is linked with Google Forms) and prints the Quote in the Generated Image.

### Potential Use Cases

  - Instagram/Twitter Quote Pages
  - News/ Media Channels to generate sharable image from text content


### How to use it?

  1. Fill the Google Forms 
  2. Run the Python Code 
  3. Image is generated with the Content (Google Forms)

## Replicate Quote Generator
### Installation - Required Libraries
```sh
$ sudo pip install -r requirements.txt
```

### Configure Google Sheets & Drive API

1. Go to [Google Developers Console](https://www.console.developers.google.com)
2. Create a Project
3. Go to API & Services 
4. **Enable Google Drive & Google Sheets API**
5. Go to Credentials & Create Credentials (Select Service account key)
6. Select Project-> Owner in Roles & Key type as json
7. **Save that document and replace that file, instead of 'quote-generator.json'**
8. In the 'Quote-Generator.py' change the file name accordingly
9. Share your 'Google Sheets' to the Client email mentioned in the json file.

### Change the following in Quote-Generator.py

* Credentials file name
* Worksheet name
* Worksheet cell value (depends on your google sheets)

And finally run **Quote-Generator.py**

Here is a sample of how your google sheets should look like

![](https://github.com/ikram-shah/Quote-Generator/blob/master/SampleScreentshot-Google_Forms.png)

And this is how your Generated Image will be
 
 <img src="https://github.com/ikram-shah/Quote-Generator/blob/master/Sample-Generated_Quote.png" width="60%">

### Make a Note

* You can change the background color and the font (Make sure that the new font is installed in your system)
* Don't share your client id/email or private key/key_id in Public
 
