import threading
import time
mississippi = "Mississippi"
def my_callback():
    print("Timer finished! Executing callback...")

def start_timer(seconds, callback):
    def my_sleep():
        print("Timer started. Waiting for it to finish...")
        for i in range(1, seconds + 1):
            print(i, mississippi)
            time.sleep(1)
        callback()
    
    thread = threading.Thread(target=my_sleep)
    thread.start()

# Start a 5-second timer with a callback
start_timer(5, my_callback)


