#import python built in modules No External modules/librires used
import glob, os

#changes the working directory to -> files
os.chdir("files")

# Create Dirctory Function
def create_dirctory(path):
    #check dirctory exists
    if not os.path.exists(path):
        #make the dirctory
        os.makedirs(path)

#List All txt files from Files Dirctory
for file in glob.glob("*.txt"):
        #split file name to get the name of it's dirctory by taking index 0
        dirctory_name = file.split('-')[0]
        # Create Dirctory By File
        create_dirctory(dirctory_name)
        #Move File from current Dirctory to It's new Dirctory (files --> files/Dirctoryname/example-1.txt)
        os.rename(file, dirctory_name+"/"+file)
