# automatically moves files written by raphael keller

def main():
    from watchdog import observers
    from watchdog.events import FileSystemEventHandler
    import os
    import time
    import shutil
    import sys
    import ctypes

    path = "\\TestPath1"
    path2 = "\\Testpath2"
    move_folder = ''.join(("//Test_move/", os.getlogin(),))
    backup_folder = "\\backuptest"

    if not os.path.exists(path2):
        os.mkdir(path2)

    if not os.path.exists(path):
        os.mkdir(path)

    if not os.path.exists(backup_folder):
        os.mkdir(backup_folder)

    if not os.path.exists(move_folder):
        ctypes.windll.user32.MessageBoxW(0, (move_folder), "Path does not exist", 0)

    class FileHandler(FileSystemEventHandler):
        def on_any_event(self, event):
            time.sleep(6)
            for files in os.listdir(path):
                file_folder = os.path.join(path, files)
                if os.path.exists(path) and os.path.exists(move_folder) and os.path.exists(
                        backup_folder) and files.startswith(
                        "Test") and files.endswith(".DAT"):
                    print("file found", file_folder)
                    shutil.copy(file_folder, backup_folder)
                    time.sleep(1)
                    print("File copyed to", backup_folder)
                    shutil.copy(file_folder, move_folder)
                    time.sleep(1)
                    print("File copyed to", move_folder)
                    time.sleep(1)
                    os.remove(file_folder)
                    print("File removed", file_folder, "from", path, "the next file will be copyed now")

    event_handler = FileHandler()
    observer = observers.Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(10)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()


main()