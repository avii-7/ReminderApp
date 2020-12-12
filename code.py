import time
from pygame import mixer
from datetime import datetime
import os
import re

def timer(t):
    while t:
        minute, seconds = divmod(t, 60)
        print(f"{minute:02}:{seconds:02}", end="")
        time.sleep(1)
        print("\b\b\b\b\b", end="")
        t -= 1

def ind_time():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    s = datetime.strptime(f'{current_time}', "%H:%M:%S")
    z = (s.strftime("%r"))
    return z

def only_date():
    named_tuple = time.localtime()  # get struct_time
    time_string = time.strftime("%d/%m/%Y", named_tuple)
    return time_string

def play_music(song_file):
    mixer.init()
    mixer.music.load(song_file)
    mixer.music.play(-1)
    while True:
        x = input()
        if 'Stop' == x.title() :
            mixer.music.stop()
            break
        elif 'Exit' == x.title():
            exit()
        else:
            print('Invalid Input..\nTry Again')
            time.sleep(0.5)

def log(log_file,da,uname):
    if os.path.isdir('D:\ReminderApp\LogFiles'):
        pass
    else:
        os.makedirs('D:\ReminderApp\LogFiles')
    if os.path.isfile(rf'D:\ReminderApp\LogFiles\{log_file}'):
        with open(rf'D:\ReminderApp\LogFiles\{log_file}') as fp:
            logfile = fp.read()
            x = re.findall(rf'{only_date()}', logfile)  # Return List
            if len(x) == 0:
                fp = open(rf'D:\ReminderApp\LogFiles\{log_file}','a')
                fp.write(f'Date: {only_date()}' + f' -- {uname}' + '\n\n')
    else:
        fp = open(rf'D:\ReminderApp\LogFiles\{log_file}', 'a')
        fp.write(f'{only_date()}' + f' -- {uname}' + '\n\n')
    with open(rf'D:\ReminderApp\LogFiles\{log_file}','a') as fp:
        fp.write(f'{da}' + f'{ind_time()}' + '\n')
        fp.close()

if __name__ == '__main__':
    uname = input('Enter Your Name: ')
    print(f'Welcome To Reminder App 2.0, {uname}.')
    while True:
        total_task = input('How Many Tasks You Want To Remind ? (Max 3)\n:>')
        if total_task == '1':
            time.sleep(0.2)
            print('Enter The Names of The Task You Want To Remind.')
            time.sleep(0.2)
            remind1 = input('Task Name: ')
            while True:
                try:
                    remind1_at_every = int(input(f'Enter The Time Intervals of {remind1} In Seconds: '))
                    break
                except Exception as e:
                    print('Only Numbers Are Allowed !!')
            time.sleep(0.2)
            print('OKAY..!!')
            time.sleep(0.2)
            print('Relax And Do Your Work .. ')
            time.sleep(0.2)
            print('I Will Remind Your Task On Time.')
            remind1_done_at = time.time()
            i = 0
            while True:
                if time.time() - remind1_done_at > remind1_at_every:
                    print(f'It\'s Time For {remind1}')
                    print('Type \' Stop \' To Stop Sound And \' Exit \' To Exit The Program.')
                    play_music('sound.mp3')
                    remind1_done_at = time.time()
                    i += 1
                    z = f'{i} {remind1} Performed At '
                    log('Task1_log.txt',z,uname)
        elif(total_task == '2'):
            time.sleep(0.3)
            print('Enter The Names of The Tasks You Want To Remind')
            time.sleep(0.3)
            remind1 = input('Task 1 Name: ')
            remind2 = input('Task 2 Name: ')
            while True:
                try:
                    remind1_at_every = int(input(f'Enter The Time Intervals of {remind1} In Seconds: '))
                    remind2_at_every = int(input(f'Enter The Time Intervals of {remind2} In Seconds: '))
                    break
                except Exception as e:
                    print('Only Numbers Are Allowed !!')
            print('OKAY..!!')
            time.sleep(0.2)
            print('Relax And Do Your Work .. ')
            time.sleep(0.2)
            print('I Will Remind Your Tasks On Time.')
            remind1_done_at = time.time()
            remind2_done_at = time.time()
            i = 0
            j = 0
            while True:
                if time.time() - remind1_done_at > remind1_at_every:
                    print(f'It\'s Time For {remind1}')
                    print('Type \' Stop \' To Stop Sound And \' Exit \' To Exit The Program.')
                    play_music('sound.mp3')
                    remind1_done_at = time.time()
                    i += 1
                    z = f'{i} {remind1} Performed At '
                    log('Task1_log.txt',z,uname)
                if time.time() - remind2_done_at > remind2_at_every:
                    print(f'It\'s Time For {remind2}')
                    print('Type \' Stop \' To Stop Sound And \' Exit \' To Exit The Program.')
                    play_music('sound.mp3')
                    remind2_done_at = time.time()
                    j += 1
                    z = f'{j} {remind2} Performed At '
                    log('Task2_log.txt',z,uname)
        elif total_task == '3':
            time.sleep(0.3)
            print('Enter The Names of The Tasks You Want To Remind')
            time.sleep(0.3)
            remind1 = input('Task 1 Name: ')
            remind2 = input('Task 2 Name: ')
            remind3 = input('Task 3 Name: ')
            while True:
                try:
                    remind1_at_every = int(input(f'Enter The Time Intervals of {remind1} In Seconds: '))
                    remind2_at_every = int(input(f'Enter The Time Intervals of {remind2} In Seconds: '))
                    remind3_at_every = int(input(f'Enter The Time Intervals of {remind3} In Seconds: '))
                    break
                except Exception as e:
                    print('Only Numbers Are Allowed !!')
            print('OKAY..!!')
            time.sleep(0.2)
            print('Relax And Do Your Work .. ')
            time.sleep(0.2)
            print('I Will Remind Your Tasks On Time.')
            remind1_done_at = time.time()    #   <--
            remind2_done_at = time.time()    #   <--  *--->   Automatic Capture Starting Time
            remind3_done_at = time.time()    #   <--
            i = 0
            j = 0
            k = 0
            while True:
                if time.time() - remind1_done_at > remind1_at_every:
                    print(f'It\'s Time For {remind1}')
                    print('Type \' Stop \' To Stop Sound And \' Exit \' To Exit The Program.')
                    play_music('sound.mp3')
                    remind1_done_at = time.time()
                    i += 1
                    z = f'{i} {remind1} Performed At '
                    log('Task1_log.txt',z,uname)
                if time.time() - remind2_done_at > remind2_at_every:
                    print(f'It\'s Time For {remind2}')
                    print('Type \' Stop \' To Stop Sound And \' Exit \' To Exit The Program.')
                    play_music('sound.mp3')
                    remind2_done_at = time.time()
                    j += 1
                    z = f'{j} {remind2} Performed At '
                    log('Task2_log.txt',z,uname)
                if time.time() - remind3_done_at > remind3_at_every:
                    print(f'It\'s Time For {remind3}')
                    print('Type \' Stop \' To Stop Sound And \' Exit \' To Exit The Program.')
                    play_music('sound.mp3')
                    remind3_done_at = time.time()
                    k += 1
                    z = f'{k} {remind3} Performed At '
                    log('Task3_log.txt',z,uname)
        else:
            print('Invalid Input..')
            time.sleep(0.4)
