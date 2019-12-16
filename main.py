from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import os

# Login
gLogin = GoogleAuth()
gLogin.LocalWebserverAuth()
drive = GoogleDrive(gLogin)


with open("test.txt","r") as file:
	# extracted file name
    fileName = os.path.basename(args["file"])
    print(fileName)

    fileDrive = drive.CreateFile({'title':fileName})
