import time
import cycles
import os

# modify these for testing [min, sec]
standard_work_unit = [25,0]
standard_break_unit = [5,0]

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
    print("You've picked a GMO Pomodoro. Let us SCIENCE!\n")

    def gmo_pom ():
      cycle = ""
      work_min = ""
      work_sec = ""
      break_min = ""
      break_sec = ""

      print (cycle, work_min, work_sec, break_min, break_sec)
      
      cycle = int(input("How many cycles would you like: "))
      print('Ok, now we will define the length for work(s) and length for break(s). Minutes first, then seconds.')
      work_min = int(input("Define working length in whole Minutes: "))
      work_sec = int(input("Define working length in whole Seconds: "))
      break_min = int(input("Define break length in whole Minutes: "))
      break_sec = int(input("Define break length in whole Seconds: "))

      return cycle, work_min, work_sec, break_min, break_sec

    user_cycle, user_work_min, user_work_sec, user_break_min, user_break_sec = gmo_pom()

    def show_stats ():

      print("Stats:\n")
      print("Cycles: ", user_cycle)
      print("Working lengths (mm:ss): "+str(user_work_min)+":"+str(user_work_sec))
      print("Break lengths (mm:ss): "+str(user_break_min)+":"+str(user_break_sec)+"\n")
    
    user_gmo_start = input("\nYou ready to eat this Pomodoro? [Y]es or [N]o ")
    
    if user_gmo_start == "Y" or "y":
      os.system("clear")
      cycles.pom_cycles(user_cycle, [user_work_min, user_work_sec], [user_break_min, user_break_sec])
    else:
      # todo: Currently we can't get here?
      os.system("clear")
      print("ok, let's try this again\n")
      user_cycle, user_work_min, user_work_sec, user_break_min, user_break_sec = gmo_pom()
      show_stats()

  if int(user_pick == 69):
    print("heh ... nice")
    time.sleep(2)
    print("Ok, come back when you're ready to be serious.")
    os.system("exit")