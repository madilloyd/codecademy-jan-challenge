import time
from datetime import datetime
import keyboard

# Get event info
event = input("Event name: ")

while True:
    try:
        event_datetime_str = input("Enter the date and time (YYYY-MM-DD HH:MM:SS): ")
        event_datetime = datetime.strptime(event_datetime_str, "%Y-%m-%d %H:%M:%S")

        if event_datetime < datetime.now():
            print("The event must be in the future. Please try again.")
        else:
            break

    except ValueError:
        print("Invalid date and time format. Please try again.")

# Keyboard input to stop the countdown  
print("Press 'q' at anytime to stop the countdown.")

#Check for input
last_display_time = 0
stop_input = False

# Countdown loop
while not stop_input:
    # Check for user key press
    if keyboard.is_pressed("q"):
        print("\nUser stopped countdown.")
        stop_input = True
        break

    # Update countdown display every second
    current_time = time.time()
    if current_time - last_display_time >= 1:
        last_display_time = current_time
        
        # Get current time
        current_time = datetime.now()

        # Calculate difference
        time_difference = event_datetime - current_time

        # Stop loop if event time met
        if time_difference.total_seconds() <= 0:
            print(f"\nTime for {event}!")
            print("Thnak you for using countdown.py")
            break
        
        # Extract days, hours, minutes, seconds
        days = time_difference.days
        total_seconds = time_difference.total_seconds()
        hours = int(total_seconds // 3600) % 24
        minutes = int(total_seconds // 60) % 60
        seconds = int(total_seconds % 60)

        #Dispaly countdown
        print(f"{days} days, {hours} hours, {minutes} minutes, {seconds} seconds until {event}", end="\r")

    # Check for key press
    time.sleep(0.1)
    
    