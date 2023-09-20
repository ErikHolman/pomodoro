import time
import datetime

def countdown (m:str, s:str):

  total_seconds = m * 60 + s

  while total_seconds > 0:
    timer = datetime.timedelta(seconds=total_seconds)

    print(timer, end="\r", flush=True)

    time.sleep(1)

    total_seconds -= 1