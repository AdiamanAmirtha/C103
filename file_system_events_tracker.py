import sys
import time
import random

import os
import shutil

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from_dir="C:/Users/User/Downloads"
class FileMovementHandler(FileSystemEventHandler):

    def on_deleted(self,event):
        print(f"Oops! someone deleted {event.src_path}!")
 # Initialize Event Handler Class       
event_handler = FileMovementHandler()

# Initialize Observer

observer= Observer()

# Schedule the Observer
observer.schedule(event_handler,from_dir,recursive=True)
observer.start()
try:
    while True:
       time.sleep(2)
       print("running...")
except keyboardInterupt:
      print("stopped!")
      observer.stop()    