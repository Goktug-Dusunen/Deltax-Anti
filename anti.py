import os
import hashlib
import numpy as np
import urllib.request
from sklearn.svm import SVC
import time
os.system('bash loading.sh')
def extract_features(file_path):
    with open(file_path, 'rb') as f:
        file_data = f.read()
        file_hash = hashlib.md5(file_data).hexdigest()
        feature_vector = np.array([ord(x) for x in file_hash], dtype=np.float32)
        return feature_vector

def get_label(file_path, databases):
    for database_url, database_file in databases:
        if not os.path.exists(database_file):
            urllib.request.urlretrieve(database_url, database_file)
        with open(database_file, 'r') as f:
            for line in f:
                if line.startswith(hashlib.md5(file_path.encode()).hexdigest()):
                    return int(line.split()[1])
    return -1

def scan_directory(dir_path, databases):
    features = []
    labels = []
    for root, dirs, files in os.walk(dir_path):
        for file in files:
            file_path = os.path.join(root, file)
            feature_vector = extract_features(file_path)
            features.append(feature_vector)
            label = get_label(file_path, databases)
            labels.append(label)
            os.system('clear')
            os.system('figlet Deltax-Anti')
            print(f"Scanned {len(features)} files in {dir_path}")
    return np.array(features), np.array(labels)

def train_model(features, labels):
    model = SVC(kernel='linear')
    model.fit(features, labels)
    print("Trained the model")

databases = [("https://virusshare.com/hashfiles/VirusShare_00000.md5", "VirusShare_00000.md5"),
             ("https://virusshare.com/hashfiles/VirusShare_00001.md5", "VirusShare_00001.md5"),
             ("https://virusshare.com/hashfiles/VirusShare_00002.md5", "VirusShare_00002.md5"),
             ("https://virusshare.com/hashfiles/VirusShare_00003.md5", "VirusShare_00003.md5"),
             ("https://virusshare.com/hashfiles/VirusShare_00004.md5", "VirusShare_00004.md5"),
             ("https://virusshare.com/hashfiles/VirusShare_00005.md5", "VirusShare_00005.md5"),
             ("https://virusshare.com/hashfiles/VirusShare_00006.md5", "VirusShare_00006.md5"),
             ("https://virusshare.com/hashfiles/VirusShare_00007.md5", "VirusShare_00007.md5"),
             ("https://virusshare.com/hashfiles/VirusShare_00008.md5", "VirusShare_00008.md5"),
             ("https://virusshare.com/hashfiles/VirusShare_00009.md5", "VirusShare_00009.md5"),
             ("https://virusshare.com/hashfiles/VirusShare_00010.md5", "VirusShare_00010.md5"),
             ("https://virusshare.com/hashfiles/VirusShare_00011.md5", "VirusShare_00011.md5"),
             ("https://virusshare.com/hashfiles/VirusShare_00012.md5", "VirusShare_00012.md5"),
             ("https://virusshare.com/hashfiles/VirusShare_00013.md5", "VirusShare_00013.md5"),
             ("https://virusshare.com/hashfiles/VirusShare_00014.md5", "VirusShare_00014.md5"),
             ("https://virusshare.com/hashfiles/VirusShare_00015.md5", "VirusShare_00015.md5"),

            ]

features, labels = scan_directory('/run/media/gjdusunen/365E0A915E0A49D7/GrandRP Launcher/', databases)
if not np.any(labels == -1):
    train_model(features, labels)
    for file in infected_files:
        os.remove(file)
        print(f"Removed {file} as it was infected. [x]")
else:
    print("No virus was found [✓]")

#power by Gdusunen
