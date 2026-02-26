import customtkinter as ctk
from clicker import AutoClicker
import threading
import pystray
from PIL import Image, ImageDraw

# Default CustomTkinter parameters
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("green")

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Main window configuration
        self.title("Auto Clicker Premium")
        self.geometry("450x550")
        self.resizable(False, False)
        
        # Logic vars
        self.delay = 30.0
        
        # Init click thread
        self.click_thread = AutoClicker(self.delay)
        self.click_thread.start()
        
        # Tray icon reference
        self.icon = None
        
        # Build UI
        self.setup_ui()

    def setup_ui(self):
        # 1. Main Title
        self.title_label = ctk.CTkLabel(
            self, 
            text="AUTO CLICKER", 
            font=ctk.CTkFont(family="Inter", size=32, weight="bold")
        )
        self.title_label.pack(pady=(20, 5))

        # 2. Status Label
        self.status_label = ctk.CTkLabel(
            self, 
            text="Ready. Waiting...", 
            font=ctk.CTkFont(size=14),
            text_color="gray"
        )
        self.status_label.pack(pady=(0, 20))

        # 3. Interval Configuration
        self.interval_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.interval_frame.pack(pady=5)

        self.interval_label = ctk.CTkLabel(
            self.interval_frame, 
            text="Interval (seconds):", 
            font=ctk.CTkFont(size=16)
        )
        self.interval_label.pack(side="left", padx=(0, 10))

        self.interval_entry = ctk.CTkEntry(
            self.interval_frame, 
            width=80,
            justify="center",
            font=ctk.CTkFont(size=16)
        )
        self.interval_entry.insert(0, str(int(self.delay)))
        self.interval_entry.pack(side="left")

        # 4. Premium Options Frame
        self.options_frame = ctk.CTkFrame(self)
        self.options_frame.pack(pady=20, padx=40, fill="x")
        
        self.options_label = ctk.CTkLabel(
            self.options_frame, 
            text="Settings", 
            font=ctk.CTkFont(size=14, weight="bold")
        )
        self.options_label.pack(pady=(10, 5))

        # 4a. Always on Top Switch
        self.topmost_var = ctk.BooleanVar(value=False)
        self.topmost_switch = ctk.CTkSwitch(
            self.options_frame, 
            text="Always on Top", 
            variable=self.topmost_var,
            command=self.toggle_topmost
        )
        self.topmost_switch.pack(pady=5, padx=20, anchor="w")

        # 4b. Sub-Tray Switch
        self.tray_var = ctk.BooleanVar(value=False)
        self.tray_switch = ctk.CTkSwitch(
            self.options_frame, 
            text="Minimize to Tray instead of closing", 
            variable=self.tray_var
        )
        self.tray_switch.pack(pady=5, padx=20, anchor="w")

        # 4c. Random Mode Switch
        self.random_var = ctk.BooleanVar(value=False)
        self.random_switch = ctk.CTkSwitch(
            self.options_frame, 
            text="Random Interval (Bot Anti-Detection)", 
            variable=self.random_var
        )
        self.random_switch.pack(pady=5, padx=20, anchor="w")

        # 4d. Anti-AFK Switch
        self.afk_var = ctk.BooleanVar(value=False)
        self.afk_switch = ctk.CTkSwitch(
            self.options_frame, 
            text="Anti-AFK Mouse Movement", 
            variable=self.afk_var
        )
        self.afk_switch.pack(pady=(5, 10), padx=20, anchor="w")

        # 5. Main Button
        self.action_button = ctk.CTkButton(
            self,
            text="▶ START",
            command=self.toggle_clicking,
            font=ctk.CTkFont(size=20, weight="bold"),
            height=60,
            width=250,
            corner_radius=30,
            fg_color="#2E8B57", # Soft Green
            hover_color="#226B42"
        )
        self.action_button.pack(pady=10)

        # 6. Theme Selector
        self.theme_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.theme_frame.pack(pady=(10, 0))

        self.theme_label = ctk.CTkLabel(self.theme_frame, text="Accent Color:")
        self.theme_label.pack(side="left", padx=5)

        self.theme_menu = ctk.CTkOptionMenu(
            self.theme_frame, 
            values=["Green (Default)", "Blue", "Dark-Blue"],
            command=self.change_theme,
            width=140
        )
        self.theme_menu.pack(side="left")

    def toggle_topmost(self):
        self.attributes("-topmost", self.topmost_var.get())

    def change_theme(self, choice):
        if "Green" in choice:
            ctk.set_default_color_theme("green")
            self.action_button.configure(fg_color="#2E8B57", hover_color="#226B42")
        elif "Dark-Blue" in choice:
            ctk.set_default_color_theme("dark-blue")
            self.action_button.configure(fg_color="#1f538d", hover_color="#14375e")
        elif "Blue" in choice:
            ctk.set_default_color_theme("blue")
            self.action_button.configure(fg_color="#3a7ebf", hover_color="#325882")
            
        # Hard override if currently stopped/started to keep visual logic
        if self.click_thread.running:
            self.action_button.configure(fg_color="#CD5C5C", hover_color="#A52A2A")

    def get_delay_from_entry(self):
        try:
            val = float(self.interval_entry.get())
            if val <= 0:
                val = 0.1
            return val
        except ValueError:
            self.interval_entry.delete(0, 'end')
            self.interval_entry.insert(0, str(int(self.delay)))
            return self.delay

    def toggle_clicking(self):
        if not self.click_thread.running:
            # Start
            self.delay = self.get_delay_from_entry()
            self.click_thread.set_delay(self.delay)
            self.click_thread.set_options(self.random_var.get(), self.afk_var.get())
            self.click_thread.start_clicking()
            
            # Update UI
            self.action_button.configure(
                text="⏹ STOP",
                fg_color="#CD5C5C", # Soft Red
                hover_color="#A52A2A"
            )
            
            mode_text = f"Running: Click every {self.delay}s"
            if self.random_var.get():
                mode_text = f"Running (~{self.delay}s Random)"
                
            self.status_label.configure(
                text=mode_text,
                text_color="#CD5C5C"
            )
            self.interval_entry.configure(state="disabled")
            
            # Disable options while running
            self.random_switch.configure(state="disabled")
            self.afk_switch.configure(state="disabled")
        else:
            # Stop
            self.click_thread.stop_clicking()
            
            # Check current theme to revert correctly
            theme_choice = self.theme_menu.get()
            self.change_theme(theme_choice)
            self.action_button.configure(text="▶ START")
            
            self.status_label.configure(
                text="Paused.",
                text_color="gray"
            )
            self.interval_entry.configure(state="normal")
            
            # Enable options
            self.random_switch.configure(state="normal")
            self.afk_switch.configure(state="normal")
            
    # System Tray Logic
    def create_image(self):
        # Generate a simple blank black image for the tray icon
        image = Image.new('RGB', (64, 64), color=(0, 0, 0))
        draw = ImageDraw.Draw(image)
        draw.rectangle((16, 16, 48, 48), fill=(46, 139, 87)) # Green square
        return image

    def on_show_window(self, icon, item):
        self.icon.stop()
        self.after(0, self.deiconify)

    def on_exit(self, icon, item):
        self.icon.stop()
        self.click_thread.exit()
        self.destroy()

    def hide_window(self):
        # Hide the main window
        self.withdraw()
        
        # Create and show System Tray icon
        image = self.create_image()
        menu = pystray.Menu(
            pystray.MenuItem('Show AutoClicker', self.on_show_window, default=True),
            pystray.MenuItem('Exit', self.on_exit)
        )
        self.icon = pystray.Icon("AutoClicker", image, "AutoClicker Premium", menu)
        
        # Run tray in a separate non-blocking way relative to tkinter
        threading.Thread(target=self.icon.run, daemon=True).start()

    def on_closing(self):
        # If user checked "Minimize to Tray", we hide it instead of closing
        if self.tray_var.get():
            self.hide_window()
        else:
            self.click_thread.exit()
            self.destroy()

if __name__ == "__main__":
    app = App()
    app.protocol("WM_DELETE_WINDOW", app.on_closing)
    app.mainloop()
