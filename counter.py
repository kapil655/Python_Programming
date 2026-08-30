import time
import os


hrs, minutes, sec = map(int, input("Enter time (hh:mm:ss): ").split(":"))

while True:
    os.system("cls" if os.name == "nt" else "clear")

    print(f"{hrs:02d}:{minutes:02d}:{sec:02d}")

    time.sleep(1)

    sec += 1

    if sec >= 60:
        sec = 0
        minutes += 1

    if minutes >= 60:
        minutes = 0
        hrs += 1

    if hrs >= 24:  
        hrs = 0