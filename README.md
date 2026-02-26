# 🖱️ Dz Auto Clicker

An elegant and minimalist Auto-Clicker script built in Python with **CustomTkinter**.
Perfect for simulating continuous presence activity (e.g., avoiding the "Away" status on Microsoft Teams or Discord).

---

## 🚀 Features

* **Premium Interface**: A gorgeous, clean Dark Mode design with customizable accent colors (Green, Blue, Dark-Blue).
* **Easy to Use**: No complex configurations—just a giant Start/Stop button.
* **Customizable Interval**: Set the time between clicks in an instant (default: 30 seconds).
* **Random Mode (Anti-Bot)**: Varies the click interval dynamically by ±20% to avoid detection by strict monitoring software.
* **Anti-AFK Movement**: Performs a micro mouse movement before every click.
* **Always on Top**: Pin the application above all your other windows for quick access.
* **System Tray Mode**: Minimize the app to your notification area instead of closing it to keep it running invisibly.
* **Background Mode**: The clicking process works asynchronously without freezing the application interface.

## 📥 Installation

If you wish to use the source code directly, follow these steps:

1. Clone this repository.
   ```cmd
   git clone https://github.com/yacinus17/DZ-Auto-Clicker.git
   cd DZ-Auto-Clicker
   ```
2. Create a virtual environment (optional but recommended).
   ```cmd
   python -m venv venv
   .\venv\Scripts\activate
   ```
3. Install the required dependencies.
   ```cmd
   pip install -r requirements.txt
   ```

## 🎮 Usage

Simply run the source code:
```cmd
python main.py
```

> ⚠️ Place the application window in a corner, click "Start", and hover your cursor at the exact spot where you want the clicks to happen.

## 🛠️ Compiling to an Executable (.exe)

You can compile this project into a standalone `.exe` file to distribute it without needing to install Python.

Make sure you have `pyinstaller` installed (included in the `requirements.txt` environment):
```cmd
pip install pyinstaller
```

Compile the project by running:
```cmd
.\venv\Scripts\python -m PyInstaller --noconsole --onefile --windowed --name "Dz Auto Clicker" --collect-all customtkinter --hidden-import pystray._win32 main.py
```
The resulting `.exe` file will be located in the `dist/` folder.

## ⚙️ Dependencies

- `customtkinter`: For the modern graphical interface.
- `pynput`: For precise mouse control.

## 📝 License

This project is completely free and open for personal or commercial use.
