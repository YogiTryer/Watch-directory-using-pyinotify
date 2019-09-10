
import asyncore
import pyinotify

path='pelase insert your path directory'
wm = pyinotify.WatchManager()  # Watch Manager
mask = pyinotify.IN_DELETE | pyinotify.IN_CREATE | pyinotify.IN_MOVED_FROM # watched events

class EventHandler(pyinotify.ProcessEvent):
    def process_IN_CREATE(self, event):
        print ("Creating:", event.path, event.name)
        NamaFile,TypeFile=event.name.split(".")
    
        print(NamaFile)
        print(TypeFile)
        
    def process_IN_DELETE(self, event):
        print ("Removing:", event.pathname)
    
    def process_IN_MOVED_FROM(self, event):
        print ("Moving:", event.pathname)

notifier = pyinotify.AsyncNotifier(wm, EventHandler())
wdd = wm.add_watch(path, mask, rec=True,auto_add=True)

asyncore.loop()
