# to display the list of items in the directory 

import os

# specifiing directory to list
directory = "."

print(f"Contents of directory '{directory}':")

# list all the files and folder in the directory
for item in os.listdir(directory):
    path = os.path.join(directory, item) 
    if os.path.isdir(path):
        print(f"[DIR]  {item}")
    else:
        print(f"       {item}")
