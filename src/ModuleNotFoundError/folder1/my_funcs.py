from datetime import datetime
import time


def show_message(message):
    # import debugpy

    # # Allow other computers to attach to debugpy at this IP address and port.
    # debugpy.listen(('10.4.21.34', 5678))

    # # Pause the program until a remote debugger is attached
    # debugpy.wait_for_client()
    print(str(datetime.now()) + ": " + str(message))


def sleep(secs):
    time.sleep(secs)
