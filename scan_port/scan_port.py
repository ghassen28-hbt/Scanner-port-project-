import socket 
#importing socket module to work with network connections
#A socket is a tool for accessing an IP address on a port

import tkinter as tk #importing tkinter module for GUI applications
from tkinter import messagebox



scanning = False

def start_scan():
    global scanning
    scanning = True
    scan_ports()

def stop_scan():
    global scanning
    scanning = False
    messagebox.showinfo("Info", "Stop scan ")
    window.quit()

#function to scan ports---------------------------------------------------------------------------------
def scan_ports():
    target = "127.0.0.1" #specifying the target IP address (localhost in this case)
    try:
        start_port = int(entry_start.get())
        end_port = int(entry_end.get())
    except ValueError:
        messagebox.showerror("Erreur", "ports should be integers")
        return

    if start_port > end_port:
        messagebox.showerror("Erreur", "Start port should be less than or equal to end port")
        return
    listbox.delete(0, tk.END)

    #scanning from port 20 to port 100 
    for port in range(start_port, end_port + 1):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)
        result = s.connect_ex((target, port))
        if result == 0:
             listbox.insert(tk.END, f"Port {port} is OPEN")
        s.close()

        

#Creating the main window for the GUI---------------------------------------------------------

window = tk.Tk()
window.title("Simple Port Scanner")
window.geometry("420x420")

# Title
tk.Label(window, text="Port Scanner", font=("Arial", 16)).pack(pady=10)

# Start port
tk.Label(window, text="Start Port").pack()
entry_start = tk.Entry(window)
entry_start.pack()

# End port
tk.Label(window, text="End Port").pack()
entry_end = tk.Entry(window)
entry_end.pack()

# Button to start scanning
tk.Button(window, text="Start Scan", command=start_scan).pack(pady=10)
tk.Button(window, text="Stop Scan", command=stop_scan).pack(pady=10)

# Listbox to display results
listbox = tk.Listbox(window, width=40, height=12)
listbox.pack()

# Running the main event loop
window.mainloop()
