# Function to print countdown on the console
import time


def countdown(n):
    for i in range(n, 0, -1):
        print(f"Countdown: {i}")
        time.sleep(1)
    print("Executing...")
