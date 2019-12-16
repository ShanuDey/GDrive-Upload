from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import os
import argparse

# argparser
argParser = argparse.ArgumentParser()
argParser.add_argument("-f","--file", required=True, help="Select the File")
args = vars(argParser.parse_args())
print("args = ",args)

# Login
gLogin = GoogleAuth()
gLogin.LocalWebserverAuth()
drive = GoogleDrive(gLogin)


with open(args["file"],"r") as file:
	# extracted file name
    fileName = os.path.basename(args["file"])
    print(fileName)

    fileDrive = drive.CreateFile({'title':fileName})
    fileDrive.SetContentString(file.read())

    print("Uploading ...")
    fileDrive.Upload()

print("File ",fileName," uploaded successfully")