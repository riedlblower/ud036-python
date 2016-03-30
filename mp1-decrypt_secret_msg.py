import os

def rename_files():
    #1 get file names from a folder
    file_list = os.listdir(r"D:\udacity\ud036-python\mini-project-1\files") #r for raw path
    # sample files are f09beijing.jpg, p04chennai.jpg, p02beijing.jpg, etc
    print file_list
    
    saved_path = os.getcwd()
    print saved_path

    #2 for each file, rename filename
    os.chdir(r"D:\udacity\ud036-python\mini-project-1\files")
    for file_name in file_list:
        print ("Old Name - " + file_name)
        # work out name of new file by removing all the letters only leaving digits and a dot
        new_name =  file_name.translate(None,"abcdefghijklmnopqrstuvwxyz")
        new_name = new_name + 'jpg'   # add back in the 'jpg' file extension letters
        print ("New Name = " + new_name)
        # rename the file to its decrpyted filename e.g 01.jpg, 02.jpg, etc
        os.rename(file_name, new_name)
    os.chdir(saved_path)
            
rename_files()
