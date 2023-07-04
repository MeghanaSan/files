import os
import shutil

from_dir = "Image_Files"
to_dir = "Document_Files"

list_of_files = os.listdir(from_dir)


for file_name in list_of_files:
    root,ext= os.path.splitext(file_name)
    print(root)
    print(ext)  
    if ext == "":
        continue
    if ext in(".gif","png",".jpg",".jpeg",".jfif"):
        path1 = from_dir + "/" + file_name
        path2 = to_dir + "/" + "Document_Files"
        path3 = to_dir + "/"+ "Document_Files" + "/" + file_name
    if os.path.exists(path2):
         print("Moving"+ file_name + ".....")
         shutil.move(path1,path3)
    else:
        os.makedirs(path2)
        print("Moving"+ file_name + ".....")
        shutil.move(path1,path3)