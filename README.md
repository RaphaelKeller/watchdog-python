Hello Guys 

This python script will move files automatically when they appear in the -source- folder.

files will be copied from "path" (the source folder) to the backup_folder and will be copied to the move_folder and get deleted
in the source_folder. A move has appeared to be running in alot of error sometimes, so i did it that way.

you can change the folowing strings as you need it:

path = "\\TestPath1"


path2 = "\\Testpath2"


move_folder = ''.join(("//Test_move/", os.getlogin(),))


with the move_folder i did something special i wanted to get a login name from the user that runs this script so 
that you can copy a file/or fodler into a pathwith alot of usernames in it and move the files direcly into the specific username folder-->


backup_folder = "\\backuptest"


if os.path.exists(path) and os.path.exists(move_folder) and os.path.exists(
  backup_folder) and files.startswith(
    "Test") and files.endswith(".DAT"):
    
    
in this case i will copy all files that start with "Test" and end with ".DAT" and delete them after they get copyed.
       
