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
#      + User defines number of cycles, working  mins/secs, and break mins/secs
# Selection is evaluated and leads to selected.py

print('''
🍅 🍅 🍅 🍅 🍅 🍅 🍅 🍅 🍅 🍅 🍅 🍅 🍅 🍅 🍅 🍅 🍅 🍅 🍅 🍅 🍅 🍅 🍅 🍅 🍅 🍅 
🍅                                                                    
🍅 Good call starting a timer for your work.                           
🍅 You'll get so much shit done yo! 
🍅     
🍅 How do you want your Pomodoro prepared?
🍅
🍅   🍅 [1] - Fresh Pomodoro (just as Francesco Cirillo intended)
🍅   🥫 [2] - Canned Pomodoro (you pick the amount amount of cycles)
🍅   🧪 [3] - GMO Pomodoro (you pick cycles and durations)
🍅     
🍅 🍅 🍅 🍅 🍅 🍅 🍅 🍅 🍅 🍅 🍅 🍅 🍅 🍅 🍅 🍅 🍅 🍅 🍅 🍅 🍅 🍅 🍅 🍅 🍅 🍅
''')

pomodoro_choice: int

while(True):
  try:
    pomodoro_choice = int(input("Pick a number (1-3): "))
    if (pomodoro_choice >= 1 and pomodoro_choice <= 3) or pomodoro_choice == 69:
      selected.pomodoro_selection(pomodoro_choice)
    break
  except TypeError:
    # print('type error')
    pomodoro_choice = input("So, we're looking for a number. 1, 2, 3, or a different 'special' number. Try agin: ")
  except ValueError:
    # print('value error')
    pomodoro_choice = input("Hmm, that does not look like a '1', '2', '3', or a different 'special' number. Try agin: ")