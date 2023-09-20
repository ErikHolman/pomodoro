# A Pomodoro written in Python by Erik Holman on 9/20/23

import os
import selected
import time

#  UI will ask for status of Pomodoro:
#    - "Fresh Pomodoro" 
#      + 1 full Pomodoro cycle [25 on, 5 off] repeated 4 times, then 30 min timer and reset app
#    - "Ripe Pomodoro"
#      + User defines between 1 and 4 cycles
#    - "GMO Pomodoro"
#      + User defines mins and secs
# Selection is evaluated and leads to selected.py

print("Good call starting a timer for your work. You'll get so much shit done yo! How do you want your Pomodoro prepared?\n")

print("[1] - Fresh Pomodoro")
print("[2] - Ripeish Pomodoro")
print("[3] - GMO Pomodoro\n")


print('Pick a number (1-3)')

attempts = 3

for retry in range(attempts):
  pomodoro_choice = int(input("> "))
  if (int(pomodoro_choice) >= 1 and int(pomodoro_choice) <= 3) or int(pomodoro_choice) == 69:
    selected.pomodoro_selection(pomodoro_choice)
  attempts -= 1
  if attempts != 1:
    print("Nah blood, I didn't code for that... Try Again. You've got "+str(attempts)+" tries left.")
  else:
    print("Nah blood, I didn't code for that... Try Again. You've got "+str(attempts)+" try left.")
else:
  print("I think you're looking for a different piece of software, I'll help you find it now")
  time.sleep(2)
  os.system("exit")