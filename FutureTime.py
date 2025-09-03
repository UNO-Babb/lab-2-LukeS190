#FutureTime.py
#Name:Luke Sheardown
#Date:9-1-2025
#Assignment:Lab 2

# datetime will allow us to access the system date and time.
import datetime
def main():
  #getting current time from system, storing to variable
  #this is just for checking, we should delete it later
  #TODO:
  #Ask user for hours
  #Ask user for minutes
  #Calculate the time after the user-supplied time has passed.
  #Do not use any if statements in calculating the time.
  #Output the future time in standard format "HH:MM"
 import datetime

now = datetime.datetime.now()
current_hour = now.hour
current_minute = now.minute

print(f"Current time: {current_hour % 12 or 12}:{current_minute:02d}")

add_hours = int(input("hours to add: "))
add_minutes = int(input("minutes to add: "))

total_minutes = current_hour * 60 + current_minute + add_hours * 60 + add_minutes

future_hour = (total_minutes // 60) % 24   
future_minute = total_minutes % 60

display_hour = (future_hour % 12) or 12

print(f"Future time: {display_hour}:{future_minute:02d}")




if __name__ == '__main__':
  main()
