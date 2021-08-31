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
    access_token = 'sl.A3pvoH6so4_CDRs14M3CCNHEtpo5xezHD467pIq9p0ZKlydqw9_0W5fLh_cMc4lBPULjSS2tlfofXibrnhQCb_XgWA3nYX2_5-3MqstDrM9H9LjAk9EBETjzpOlZbM8hsNrvDS8'
    transferData = TransferData(access_token)

    file_from = input("enter the file path to transfer")
    file_to = input("enter the full path to upload the dropbox")  # The full path to upload the file to, including the file name

    # API v2
    transferData.upload_file(file_from, file_to)
    print("file has been moved")

    main()
