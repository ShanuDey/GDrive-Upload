from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import os
import argparse

# argparser
argParser = argparse.ArgumentParser()
argParser.add_argument("file", help="select the file to be uploaded")
args = vars(argParser.parse_args())
print("args = ",args)

# Login
gLogin = GoogleAuth()
gLogin.LocalWebserverAuth()
drive = GoogleDrive(gLogin)

fileName = os.path.basename(args["file"])
print("file name = ", fileName)

fileDrive = drive.CreateFile({'title':fileName})
fileDrive.SetContentFile(args["file"])
fileDrive.Upload()

print("File ",fileName," uploaded successfully")