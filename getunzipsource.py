import os
import sys
import shutil

from google.cloud import storage
from zipfile import ZipFile

# Remove left overs from last run
if os.path.isdir("source"):
    shutil.rmtree("source")


def get_client():
    """
    Get a storage client
    """
    try:
        storage_client = storage.Client()
    except Exception as err:
        raise Exception("Unable to get storage client. Aborting operation:") from err
        
    return storage_client


def get_unzip_source(zip_location):
    storage_client = get_client()

    bucket = storage_client.get_bucket('data-source-bucket-ons')

    blob = bucket.get_blob(zip_location)
    blob.download_to_filename(blob.name)

    with ZipFile(blob.name, 'r') as zipObj:
        zipObj.extractall()

if __name__ == "__main__":
    zip_location = sys.argv[1]
    get_unzip_source(zip_location)