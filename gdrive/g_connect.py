from oauth2client.service_account import ServiceAccountCredentials
from pydrive.drive import GoogleDrive
from pydrive.auth import GoogleAuth

def google_auth():
    g_auth = GoogleAuth()
    g_auth.LocalWebserverAuth()
    g_drive = GoogleDrive(g_auth)

    return g_drive