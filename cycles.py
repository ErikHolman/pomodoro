import os
import timer

def pom_cycles (count: str, work_len:str, break_len:str):

  cycles = int(count)
  total_cycles = count
  
  work_minutes = work_len[0]
  work_seconds = work_len[1]

  break_minutes = break_len[0]
  break_seconds = break_len[1]

  for i in range(cycles):    
    while cycles > 0:
      cycles = cycles - 1
      if cycles == 0:
        print("Last cycle before a longer break.\n")
      else:
        print("Cycles remianing: "+ str(cycles + 1) + " out of " + str(total_cycles) + "\n")
      timer.countdown(work_minutes, work_seconds)
      if cycles != 0:
        input("Press ENTER to start a break.\n")
        timer.countdown(break_minutes, break_seconds)
        input("Press ENTER to move to the next cycle.\n")
        os.system("clear")
    break
  print("GOOD WORK! Take a longer break! See you soon. \n")