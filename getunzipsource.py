import os
import sys
from pathlib import Path
import shutil

from google.cloud import storage
from zipfile import ZipFile

# Remove left overs from last run
if os.path.isdir("source"):
    shutil.rmtree("source")

source_dir = Path("source")
source_dir.mkdir()

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

    print(f'Python got zip download location as: {zip_location}')
    blob = bucket.get_blob(zip_location)
    
    output_zip = blob.name.split('/')[1]  # the file from folder/thing.zip
    print(f'Downloading to file {source_dir / output_zip}')
    blob.download_to_filename(source_dir / output_zip)

    with ZipFile(source_dir / output_zip, 'r') as zipObj:
        zipObj.extractall(source_dir)

    for file_name in os.listdir(source_dir):
        print(f'Received file {file_name}')


if __name__ == "__main__":
    zip_location = sys.argv[1]
    get_unzip_source(zip_location)
