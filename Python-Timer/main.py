#
# https://www.w3schools.com/python/ref_string_format.asp
import time

def countdown(time_sec) :
    while time_sec:
      mins, secs = divmod(time_sec, 60)
      timeformat = '{:02d}:{:02d}' . format(mins, secs)
      print(timeformat,end='\r')
      time.sleep(1)
      time_sec -= 1

    print("stop")

num = int(input("Set Your Timer in Sec : ") )
countdown(num)