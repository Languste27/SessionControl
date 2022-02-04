import os
import shutil
import glob
import time

# Configure These

# can't contain spaces
start_delay = 30  # time it takes for your instances to start up (in seconds)
macro_delay = 10  # time it take for the macro to resize and rename your instances (in seconds)
instance_format = "instance"  # The name format of your instances (i have instance1 instance2 etc so its 'instance')
instance_count = 8  # Change to match instance count
instance_folder = 'C:\\MultiMC\\instances'  # The Folder your instances are located in
mmc = "C:\\MultiMC"  # Change this to match your MultiMc location

#  can contain spaces, put double backslash
ninja_bot = "C:\\Users\\Max Afemann\\Desktop\\Speedrun stuff\\Ninjabrain"  # location of your ninja bot, rename it to calc.jar
reset_tracker = "C:\\Users\\Max Afemann\\Desktop\\Speedrun stuff\\Reset tracker"  # location of your tracker, has to be named resetTracker.exe
wall_script = "C:\\Users\\Max Afemann\\Desktop\\Speedrun stuff\\TheWall"  # location of your wall script, has to be named TheWall.ahk
obs_exe = "C:\\Program Files\\obs-studio\\bin\\64bit"  # location of your obs.exe, probably same as mine

# Don't configure these
taskkillmc = 'taskkill /IM javaw.exe /F'
taskkillahk = 'taskkill /IM AutoHotkey.exe /F'
taskkillmcl = 'taskkill /IM MultiMC.exe /F'
taskkillcmd = 'taskkill /IM cmd.exe /F'


def world_deletion():  # Stole specnr's code lol
    deleted_worlds = 0
    files = glob.glob(f'{instance_folder}/*/.minecraft/saves/*')
    for f in files:
        if "New World" in f or "Speedrun #" in f:
            shutil.rmtree(f)
            print('deleted', f)
            deleted_worlds += 1

    msg = f'Deleted {deleted_worlds} worlds, press Enter to exit'
    leave = input(msg)


def kill():
    os.system(taskkillmc)
    os.system(taskkillahk)
    os.system(taskkillmcl)
    os.system(taskkillcmd)


def instance_startup():  # stole even more of his code lmao
    for i in range(1, instance_count + 1):
        print(f"Starting {instance_format}{i}")
        os.system(f"{mmc}\\MultiMC.exe -l {instance_format}{i}")


def start():
    os.system(f'start {mmc}\\MultiMC.exe')
    os.system(f'start /d "{ninja_bot}" "" calc.jar')
    os.system(f'start /d "{reset_tracker}" "" resetTracker.exe')
    time.sleep(3)
    instance_startup()
    time.sleep(start_delay)
    os.system(f'start /d "{wall_script}" TheWall.ahk')
    time.sleep(macro_delay)
    os.system(f'start /d "{obs_exe}" "" obs64.exe')
    end()


def end():
    a = input('Press enter to end session')
    kill()
    world_deletion()
    exit()


start()

# Common issues and how to fix:

# Only works for windows i think so if you have mac you r unlucky

# Nnjabrain doesn't open
# Download jarfix and run it

# file can not be found
# Make sure to have backslashes and type everything correctly
# Also don't paste the paths to the actual files, just the folder they are located in

# For other issues or questions just dm me, RadioaktiveLanguste#0672
