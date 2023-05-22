import time
import os
import shutil
from watchdog.observers import Observer
from watchog.events import FileSystemEventHandler


#Source file path
source = 'main.txt'

#destination file path
dest = 'newfile.txt'


#Event handler class

class FileMovementHandler(FileSystemEventHandler):

def on_created(self,event):

    name,extension = os.path.splitext(event.src_path)

    time.sleep(1)
    for key, value in dir_tree.items():

        time.sleep(1)
        if extension in value:

            file_name = os.path.basename(event.src_path)

            print("Download" + file_name)

            path1 = from_dir + '/' + file_name
            path2 = to_dir + '/' + key
            path3 = to_dir + '/' + key + '/' + file_name


            time.sleep(1)
            if os.path.exists(path2):

                print("Directory Exists...")
                time.sleep(1)


                if os.path.exists(path3):

                   print("File Already Exists In" + key + "....")
                   print("Renaming File" + file_name + "....")


                   new_file_name = os.path.splitext(file_name)[0] + str(random.randint(0, 999)) + os.path.splitext(file_name)[1]


                   path4 = to_dir + '/' + key + '/' + new_file_name

                   print("Moving" + new_file_name + "...")
                   shutil.move(path1, path4)
                   time.sleep(1)


                else:
                    print("Moving" + file_name + "....")
                    shutil.move(path1, path3)
                    time.sleep(1)

                else:
                    print("Making Directory...")
                    os.makedirs(path2)
                    print("Moving" + file_name + "....")
                    shutil.move(path1, path3)
                    time.sleep(1)



