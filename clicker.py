import time
import threading
import random
from pynput.mouse import Button, Controller

class AutoClicker(threading.Thread):
    def __init__(self, delay):
        super(AutoClicker, self).__init__()
        self.delay = delay
        self.running = False
        self.program_running = True
        self.mouse = Controller()
        
        # New Feature Flags
        self.random_mode = False
        self.anti_afk_mode = False

    def start_clicking(self):
        self.running = True

    def stop_clicking(self):
        self.running = False

    def exit(self):
        self.stop_clicking()
        self.program_running = False

    def set_delay(self, delay):
        self.delay = delay
        
    def set_options(self, random_mode, anti_afk_mode):
        self.random_mode = random_mode
        self.anti_afk_mode = anti_afk_mode

    def run(self):
        while self.program_running:
            while self.running:
                # 1. Anti-AFK Micro-Movement
                if self.anti_afk_mode:
                    current_position = self.mouse.position
                    # Move 1 pixel away then back instantly
                    self.mouse.position = (current_position[0] + 1, current_position[1])
                    time.sleep(0.01)
                    self.mouse.position = current_position
                    
                # 2. Click
                self.mouse.click(Button.left)
                
                # 3. Calculate Delay
                current_delay = self.delay
                if self.random_mode:
                    # Vary the delay between -20% and +20%
                    variance = current_delay * 0.20
                    min_delay = max(0.1, current_delay - variance)
                    max_delay = current_delay + variance
                    current_delay = random.uniform(min_delay, max_delay)
                    
                time.sleep(current_delay)
                
            time.sleep(0.1)  # Sleep briefly while paused to prevent high CPU usage
