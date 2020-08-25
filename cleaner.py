import hashlib
import os
import bz2

hasher = hashlib.md5()

def read(filename):
    with open(filename, "rb") as f:
        return bz2.decompress(f.read()).decode()

for i in range(6000):
    scp = "scp-" + f'{i:03}'
    file = 'SCPscrapes/' + scp + '.bz2'
    if os.path.isfile(file):
        print(scp)
        if "<span>This page doesn't exist yet!</span>" in read(file):
            os.remove(file)
            print('Removing SCP-' + f'{i:03}')