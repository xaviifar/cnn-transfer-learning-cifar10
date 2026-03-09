import requests
import tarfile
import pickle
import os

URL = "https://www.cs.toronto.edu/~kriz/cifar-10-python.tar.gz"
DATA_DIR = "./data"
x_list = []
y_list = []



def downloadDataset():
    
    with requests.get(URL, stream=True) as r:
        local_filename = URL.split('/')[-1]
        r.raise_for_status()

        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)


def decompressDataset(file):

    with tarfile.open(file, 'r:gz') as tar:
        tar.extractall()
        print("File decompress succesfully")



def cleanDataset():
    
    for file in os.listdir():
        file_path = os.path.join(DATA_DIR, file)

        with open(file_path, 'rb') as f:
            data = pickle.load(f)

            x_list.append(data[b'data'])
            y_list.extend(data[b'label'])






