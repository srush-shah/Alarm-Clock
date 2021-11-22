# Works with playsound version 1.2.2
# Concepts: DateTime Module, Playsound library

from datetime import datetime
from playsound import playsound

alarm_time = input('Enter the time of alarm to be set (HH:MM:SS AM/PM): ')
alarm_hour = alarm_time[0:2]
alarm_min = alarm_time[3:5]
alarm_sec = alarm_time[6:8]
alarm_period = alarm_time[9:11].upper()

print('Setting up alarm...')

while True:
    now = datetime.now()
    cur_hour = now.strftime('%I')
    cur_min = now.strftime('%M')
    cur_sec = now.strftime('%S')
    cur_period = now.strftime('%p')

    if alarm_period == cur_period:
        if alarm_hour == cur_hour:
            if alarm_min == cur_min:
                if alarm_sec == cur_sec:
                    print('Wake Up!')
                    playsound('audio.wav')
                    break
