from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

gauth = GoogleAuth()
gauth.LocalWebserverAuth()
drive = GoogleDrive(gauth)

class HandleFiles:

    def searchWord(self,word):
        fileList = drive.ListFile({'q': "fullText contains '{palabra}'".format(palabra=word)}).GetList()
        for file in fileList:
            print('Word found in: Title: %s, ID: %s' % (file['title'], file['id']))

    def createFile(self,name,description,content):
        file = drive.CreateFile({'title': '{}'.format(name), 'description': '{}'.format(description)})
        file.SetContentString(content)
        file.Upload()
        print('File created with: Title: %s, Description: %s, ID: %s' % (file['title'],file['description'],file['id']))
        return file

    def deleteFile(self,file):
        file.Delete()









