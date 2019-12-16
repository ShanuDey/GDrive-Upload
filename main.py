from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

# Login
gLogin = GoogleAuth()
gLogin.LocalWebserverAuth()
drive = GoogleDrive(gLogin)