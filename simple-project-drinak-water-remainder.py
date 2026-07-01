import time
from plyer import notification

while True:
    print("please sip water")
    notification.notify(title= "please drink some water", message = "you need to drink some water",)
    time.sleep(60*60)