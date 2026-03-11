import requests
import tarfile
import pickle
from pathlib import Path
import os
import shutil
import re

URL = "https://www.cs.toronto.edu/~kriz/cifar-10-python.tar.gz"
DATA_DIR = "./dataset"
x_list = []
y_list = []


def downloadDataset():
    try:
        with requests.get(URL, stream=True) as r:
            local_filename = URL.split('/')[-1]
            r.raise_for_status()

            with open(local_filename, 'wb') as f:
                for chunk in r.iter_content(chunk_size=8192):
                    f.write(chunk)

    except Exception as e:
        print(f"Error downloading in: {URL}")
        print(f"Error:{e}")


def decompressDataset(folder_path):

    with tarfile.open(folder_path, 'r:gz') as tar:
        tar.extractall()
        print("File decompress succesfully")

        shutil.move("./cifar-10-batches-py", "./dataset")

        for file in os.listdir(folder_path):
            if re.match(file, "^data_batch_"): 
                file_path = os.path.join(DATA_DIR, file_path)
                shutil.move(file_path, DATA_DIR)

        

def cleanDataset():
    if not os.path.exists(DATA_DIR):
        # raise FileNotFoundError(f"The directory {DATA_DIR} does not exist")
         
        for file in os.listdir():
            file_path = os.path.join(DATA_DIR, file)

            with open(file_path, 'rb') as f:
                data = pickle.load(f)

                x_list.append(data[b'data'])
                y_list.extend(data[b'label'])










