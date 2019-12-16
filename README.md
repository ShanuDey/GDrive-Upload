# GDrive Upload

This python script will upload file to google drive using python.

## Steps:
- Clone this tool or ```wget https://raw.githubusercontent.com/ShanuDey/GDrive-Upload/master/main.py```
- Create Clinet Secrets from Google Developer Console
	- Go to GCP page
	- Make a new project or choose existing one
	- Go to API section
	- Enable **Google Drive API**
	- Set Oauth and give a name
	-  download credential and rename it to ```client_secrets.json```
- Run ```python main.py -h``` for help
- For upload file ```python main.py -f file```  
- Enjoy
