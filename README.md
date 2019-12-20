![](https://github.com/ShanuDey/GDrive-Upload/workflows/Python%20application/badge.svg)

# GDrive Upload

This python script will upload file to google drive using python.

## Steps:
- Clone this tool
- ```python -m pip install --upgrade pip```
- ```pip install -r requirements.txt```
- Create Client Secrets from Google Developer Console
	- Go to GCP page
	- Make a new project or choose existing one
	- Go to API section
	- Enable **Google Drive API**
	- Set Oauth and give a name
	-  download credential and rename it to ```client_secrets.json```
- Run ```python main.py -h``` for help
- For upload file ```python main.py filePath```
- Enjoy
