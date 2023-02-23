# folderSync.py

from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from oauth2client.service_account import ServiceAccountCredentials
import os

# set currentDir
currentDir = os.path.realpath(os.path.dirname(__file__))

clientSecrets = f'{currentDir}/client_secrets.json' # path to client_secrets.json file

def folderSync():
    try:
        # Authenticate with Google Drive
        gauth = GoogleAuth()
        scope = ["https://www.googleapis.com/auth/drive"]
        gauth.credentials = ServiceAccountCredentials.from_json_keyfile_name(clientSecrets, scope)
        drive = GoogleDrive(gauth)

        # Get a list of file names in the local directory and the Google Drive directory
        local_file_names = os.listdir(f'{currentDir}/images')
        drive_file_names = [file['title'] for file in drive.ListFile().GetList() if file['mimeType'].split('/')[0] == 'image']

        # Sort the lists of file names so they can be compared
        local_file_names.sort()
        drive_file_names.sort()

        # If the lists of file names are not equal, delete any local files that are not in the Google Drive directory
        # and download any Google Drive files that are not in the local directory
        if local_file_names != drive_file_names:
            print('different list')     
            for file in local_file_names:
                if file not in drive_file_names:
                    os.remove(f'images/{file}')

            for file in drive.ListFile().GetList():
                if file['mimeType'].split('/')[0] == 'image':
                    if file['title'] not in local_file_names:
                        file.GetContentFile(f"{currentDir}/images/{file['title']}")

        # Create a list of file paths in the local directory and return it
        list_return = [f'{currentDir}/images/{file}' for file in os.listdir('images')]
        return list_return
    
    # If there is an exception, return a list of file paths in the local directory
    except Exception as e:
        print(e)
        list_return = [f'{currentDir}/images/{file}' for file in os.listdir('images')]
        return list_return