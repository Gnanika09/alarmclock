import datetime
import time
import winsound

def set_alarm(alarm_time):
    while True:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        if current_time == alarm_time:
            print("Wake up!")
            # Play alarm sound (Windows only)
            winsound.Beep(1000, 2000)  # Frequency: 1000Hz, Duration: 2000ms
            break
        else:
            print("Current time:", current_time)
            time.sleep(1)  # Wait for 1 second

# Get the alarm time from the user
alarm_time_input = input("Enter the alarm time in HH:MM:SS format: ")
set_alarm(alarm_time_input)
