from datetime import datetime
import time

# Get current time
current_time = datetime.now()
#print(current_time.strftime("%x %I:%M:%S %p"))

# Get event info
event = input("Event name: ")
#year = input("Is your event due this year? (y/n): ")

event_datetime_str = input("Enter the date and time (YYYY-MM-DD HH:MM:SS): ")
event_datetime = datetime.strptime(event_datetime_str, "%Y-%m-%d %H:%M:%S")


#Calculate time difference
#datetime_difference = event_datetime - current_time
#print(datetime_difference)

# Countdown loop
while True:
    current_time = datetime.now()
    time_difference = event_datetime - current_time

    if time_difference.total_seconds() <= 0:
        print(f"{event} countdown has started!")
        break
    
    # Extract days, hours, minutes, seconds
    days = time_difference.days
    total_seconds = time_difference.total_seconds()

    hours = int(total_seconds // 3600) % 24
    minutes = int(total_seconds // 60) % 60
    seconds = int(total_seconds % 60)

    #Dispaly countdown
    print(f"{days} days, {hours} hours, {minutes} minutes, {seconds} seconds until {event}")

    time.sleep(1)