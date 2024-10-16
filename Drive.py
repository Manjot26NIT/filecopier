import os
import shutil
import time
import os.path
import argparse

parser=argparse.ArgumentParser()
parser.add_argument("path",type=str,default="C://",help="Enter the path of the directory you want to copy files from")
parser.add_argument("extension", default=".txt", type=str,help="Enter the extension of the file you want to copy")

dl='ABCDEFGHIJKLMNOPQRSTUVWXYZ'

args=parser.parse_args()
extension=args.extension
root_dir=args.path
drives=[d for d in dl if os.path.exists(d+":")]
print(drives)

a=extension
def func(list_1,list_2):
    list_3 = [value for value in list_1 if value not in list_2]
    return list_3


def copier(x):
    if os.name == "nt":
        print("Windows OS Detected")
    start_time = time.time()
    for dirpath, dirnames, filenames in os.walk(x):
        for filename in filenames:
            if filename.endswith(a):
                source_path = os.path.join(dirpath, filename)
                shutil.copy(source_path, root_dir)
    end_time = time.time()
    print("Time taken to copy files: ", end_time - start_time)

while True:
    x=[d for d in dl if os.path.exists(d+":")]
    z=func(drives,x)
    if z:
        print("Drive removed: ",z)
        drives=x
    z=func(x,drives)
    if z:
        usage=shutil.disk_usage(z[0]+":")
        print(f'Total: {usage.total/(1024*1024*1024)}, Used: {usage.used/(1024*1024*1024)}, Free: {usage.free/(1024*1024*1024)}')
        print("Drive Detected: ",z)
        for xxx in z:
         copier(xxx+":")
        drives=x    
 

 