from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import os

# Login
gLogin = GoogleAuth()
gLogin.LocalWebserverAuth()
drive = GoogleDrive(gLogin)


with open("test.txt","r") as file:
	print(file.read())