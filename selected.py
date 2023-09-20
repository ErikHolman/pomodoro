import time
import cycles
import os

# modify these for testing [min, sec]
standard_work_unit = [0,6]
standard_break_unit = [0,3]

def pomodoro_selection (user_pick):

  if int(user_pick) == 1:
    os.system("clear")
    print("You picked a Fresh Pomodoro. Here we go!\n")
    time.sleep(.2)
    print("Have a productive ... thing?\n")
    cycles.pom_cycles(4, standard_work_unit, standard_break_unit)

  if int(user_pick) == 2:
    os.system("clear")
    print("You've picked a Ripeish Pomodoro. How many cycles are do you want?\n")
    user_cycle = int(input("Cycle count: "))
    if user_cycle == 4:
      print(str(user_cycle) + " cycles is the same as a Fresh Pomodoro, JSYK for next time. Here we go!\n")
    else:
      print(str(user_cycle) + " cycles coming right up!\n")
    time.sleep(.2)
    cycles.pom_cycles(user_cycle, standard_work_unit, standard_break_unit)

  if int(user_pick == 3):
    os.system("clear")
    print("You've picked a GMO Pomodoro. How many cycles are do you want?\n")

    def gmo_pom ():
      cycle = ""
      work_min = ""
      work_sec = ""
      break_min = ""
      break_sec = ""

      print (cycle, work_min, work_sec, break_min, break_sec)
      
      cycle = int(input("Cycle count: "))
      work_min = int(input("Define working length in Minutes: "))
      work_sec = int(input("Define working length in Seconds: "))
      break_min = int(input("Define break length in Minutes: "))
      break_sec = int(input("Define break length in Seconds: "))

      return cycle, work_min, work_sec, break_min, break_sec

    user_cycle, user_work_min, user_work_sec, user_break_min, user_break_sec = gmo_pom()

    def show_stats ():

      print("Stats:\n")
      print("Cycles: ", user_cycle)
      print("Working lengths (mm:ss): "+str(user_work_min)+":"+str(user_work_sec))
      print("Break lengths (mm:ss): "+str(user_break_min)+":"+str(user_break_sec)+"\n")
    
    user_gmo_start = input("You gonna eat that Pomodoro? [Y]es or [N]o\n")
    
    if user_gmo_start == "Y" or "y":
      print("\n")
      cycles.pom_cycles(user_cycle, [user_work_min, user_work_sec], [user_break_min, user_break_sec])
    else:
      os.system("clear")
      print("ok, let's try this again\n")
      user_cycle, user_work_min, user_work_sec, user_break_min, user_break_sec = gmo_pom()
      show_stats()

  if int(user_pick == 69):
    print("heh... nice")
    time.sleep(2)
    os.system("exit")