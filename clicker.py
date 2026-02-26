import time
import threading
from pynput.mouse import Button, Controller

class AutoClicker(threading.Thread):
    def __init__(self, delay):
        super(AutoClicker, self).__init__()
        self.delay = delay
        self.running = False
        self.program_running = True
        self.mouse = Controller()

    def start_clicking(self):
        self.running = True

    def stop_clicking(self):
        self.running = False

    def exit(self):
        self.stop_clicking()
        self.program_running = False

    def set_delay(self, delay):
        self.delay = delay

    def run(self):
        while self.program_running:
            while self.running:
                self.mouse.click(Button.left)
                time.sleep(self.delay)
            time.sleep(0.1)  # Sleep briefly while paused to prevent high CPU usage
