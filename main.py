
#install using: pip install easygui
from easygui import *
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from tkinter import *
from tkinter import filedialog

cancelled = False
dir = False
choice= buttonbox("Which directory would you like to track?","Choose Directory",("All Folders", "Pick a Folder", "Cancel"),None,None,"Pick a Folder","Cancel")
if(choice == "All Folders"):
    dir = "/"
elif(choice == "Pick a Folder"):
    dir = filedialog.askdirectory()
else:
    print("Cancelled")
    cancelled=True

# Event Hanlder Class
if(cancelled!=True):
    class FileMovementHandler(FileSystemEventHandler):
        def on_created(self, event):
            print("An event happened at " + str(event.src_path) + " and resulted in something being "+str(event.event_type)+"\n")
        def on_modified(self, event):
            print("An event happened at " + str(event.src_path) + " and resulted in something being "+str(event.event_type)+"\n")
        def on_moved(self, event):
            print("An event happened at " + str(event.src_path) + " and resulted in something being "+str(event.event_type)+"\n")
        def on_deleted(self, event):
            print("An event happened at " + str(event.src_path) + " and resulted in something being "+str(event.event_type)+"\n")


    # Initialize Event Handler Class
    event_handler = FileMovementHandler()


    # Initialize Observer
    observer = Observer()

    # Schedule the Observer
    observer.schedule(event_handler, dir, recursive=True)


    # Start the Observer
    observer.start()


    while True:
        pass

