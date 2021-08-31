Topic Cloud Storage

● Create dropbox account and Install dropbox using pip 

● Using how do I to get the best solution to upload files to dropbox 

● Building and customizing a python program to get file name or file path as input from user on command line

what we learned in the last class?

ESR: We learned about functions. We also learned about functions defined for file object and use them to manipulate text inside files

Libraries in python are called Modules. We will learn how to import modules into our project and use them in programming. We will learn about two specific modules - os module and shutil module. At the end of the class, we will have built two python tools which will automate - backing up any folder which we want. - organizing different kinds of files - images, videos, songs into separate folders

What is a cloud storage service? 

A remote storage space which allows us to store our files remotely. These storage spaces allow us to access data from anywhere and from any device

r, in the last class we had progressed to create backup for our files. But we were backing up on our own system in a different storage location / drive

Let us learn to write a python program which backup any file we want on a cloud storage service/ We will be using a popular cloud storage service called DropBox.

opens the terminal and write howdoi upload files to dropbox using python.

opens the terminal and write howdoi upload files to dropbox using python.

```python
import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        """upload a file to Dropbox using API v2
        """
        dbx = dropbox.Dropbox(self.access_token)

        with open(file_from, 'rb') as f:
            dbx.files_upload(f.read(), file_to)

def main():
    access_token = '******'
    transferData = TransferData(access_token)

    file_from = 'test.txt'
    file_to = '/test_dropbox/test.txt'  # The full path to upload the file to, including the file name

    # API v2
    transferData.upload_file(file_from, file_to)

if __name__ == '__main__':
    main()

```

STEPS :

1. opens the terminal and write howdoi upload files to dropbox using python.> You'll see a code to upload file to dropbox. In the code you can see that it needs an access token. Access token is something by which you can gain access to your cloud storage on dropbox.

2. To use dropbox in our code we need to import it first. so importing dropbox import dropbox

3. TransferData is a class

def __init__(self, access_token): self.access_token = access_token In this class a constructor (__init__) is used to initialize the object. The object accepts an access token which is passed in the init function

\4. In the next method dropbox is initialized and stored in variable dbx dbx = dropbox.Dropbox(self.access_token) with open(file_from, 'rb') as f: 

dbx.files_upload([f.read()](https://f.read()/),

 file_to) In this line with statement has been used to open a file as 'f'. with make the code readable and also handles any exception thrown when opening the file. The file is opened in r -> read

mode and b-> binary mode.

What' s this main function doing?

access_token variable is declared which has some string. Then a new transferData object is created using the class defined earlier and access_token is passed to it

After that a variable called file_from is declared which will have the path of the file or folder which we want to upload. below that file_to variable is declared which has the full path to upload the file to, including name that you wish the file to be called once uploaded.

\6. Then upload_file function of the class is called and file_from and file_to is passed to it as arguments

\7. Do you know what this line means? codeif __name__ == '__main__': main() here the name of the file is set to main and main() is called. If the python interpreter is running that module (the source file) as the main program, it sets the special __name__ variable to have a value “__main__”. If this file is being imported from another module, __name__ will be set to the module’s name. Module’s name is available as value to __name__ global variable.

dropbox access key 

sl.A3pvoH6so4_CDRs14M3CCNHEtpo5xezHD467pIq9p0ZKlydqw9_0W5fLh_cMc4lBPULjSS2tlfofXibrnhQCb_XgWA3nYX2_5-3MqstDrM9H9LjAk9EBETjzpOlZbM8hsNrvDS8