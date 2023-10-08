import os
import time
import random
import pywintypes
import win32file
import win32con
import tkinter as tk
from tkinter import ttk

def create_files():
    # Disable the "Run" button to prevent multiple runs
    run_button.config(state="disabled")
    
    # Change the label text to "Running..." and show the circular loading indicator
    status_label.config(text="Running...")

    # get the folder path and number of files from the entry widgets
    folder_path = folder_path_entry.get()
    num_files = int(num_files_entry.get())

    # Define a function to change the file creation time
    def changeFileCreationTime(fname, newtime):
        wintime = pywintypes.Time(newtime)
        winfile = win32file.CreateFile(
            fname, win32con.GENERIC_WRITE,
            win32con.FILE_SHARE_READ | win32con.FILE_SHARE_WRITE | win32con.FILE_SHARE_DELETE,
            None, win32con.OPEN_EXISTING,
            win32con.FILE_ATTRIBUTE_NORMAL, None)
        win32file.SetFileTime(winfile, wintime, None, None)
        winfile.close() 

    # Function to generate a random timestamp
    def randomTimestamp():
        current_time = time.time()
        two_years_ago = current_time - (2 * 365 * 24 * 60 * 60)  # Two years in seconds
        return random.randint(int(two_years_ago), int(current_time))

    # Function to generate a random file size
    def randomFileSize():
        return random.randint(1024, 1024*1024)  # Adjust the range as needed

    extensionTypes = {"aif", "au", "avi", "bat", "bmp", "java", "csv", "cvs", "dbf", "dif", "doc", "docx", "eps", "exe", "fm3", "gif", "hqx", "htm", "html", "jpg", "jpeg", "mac", "map", "mdb", "mid", "midi", "mov", "qt", "mtb", "mtw", "pdf", "p65", "t65", "png", "ppt", "pptx", "psd", "psp", "qxd", "ra", "rtf", "sit", "tar", "tif", "txt", "wav", "wk3", "wks", "wpd", "wp5", "xls", "xlsx", "zip"}

    start_time = time.time()
    folpaths = [folder_path]  # Desired drive to destroy
    storepaths = set(folpaths)

    while folpaths:
        try:
            spath = folpaths.pop()
            file = os.listdir(spath)
            for i in file:
                if "." not in i:
                    new_path = os.path.join(spath, i)
                    folpaths.append(new_path)
                    storepaths.add(new_path)
        except (IndexError, FileNotFoundError):
            pass

    # Precompute random timestamps
    timestamps = [randomTimestamp() for _ in range(10)]

    for path in storepaths:
        for _ in range(int(num_files)):
            new_file_name = "".join(random.choice('abcdefghijklmnopqrstuvwxyz') for _ in range(15))
            file_extension = random.choice(list(extensionTypes))
            try:
                full_path = os.path.join(path, new_file_name + "." + file_extension)
                with open(full_path, "wb") as file:
                    file.seek(randomFileSize() - 1)
                    file.write(b'\0')
                
                # Set the modification and creation times to random timestamps
                new_mod_time = timestamps.pop()
                new_cre_time = new_mod_time
                os.utime(full_path, (new_mod_time, new_cre_time))
                changeFileCreationTime(full_path, new_cre_time)
            except Exception as e:
                print(f"{full_path} - something went wrong with this file: {e}")

    # Calculate and display the time taken
    end_time = time.time() - start_time
    status_label.config(text=f"Task complete. Time taken: {end_time:.2f} seconds")
    
    # Re-enable the "Run" button and stop the circular loading indicator
    run_button.config(state="normal")

# close the window
def exit_program():
    root.destroy()

# Create the main window
root = tk.Tk()
root.title("Directory Destroyer")

# Calculate the vertical and horizontal center of the window
window_width = 500
window_height = 300
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_position = (screen_width - window_width) // 2
y_position = (screen_height - window_height) // 2
root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

# Create a frame to contain the widgets
frame = ttk.Frame(root)
frame.place(relx=0.5, rely=0.5, anchor="center")

# Create label and entry for folder path
folder_path_label = ttk.Label(frame, text="Folder Path:")
folder_path_label.grid(row=0, column=0, sticky="e")

folder_path_entry = ttk.Entry(frame, width=30)
folder_path_entry.grid(row=0, column=1, padx=10)

# Create label and entry for number of files
num_files_label = ttk.Label(frame, text="Number of Files:")
num_files_label.grid(row=1, column=0, sticky="e")

num_files_entry = ttk.Entry(frame, width=30)
num_files_entry.grid(row=1, column=1, padx=10)

# Run button
run_button = ttk.Button(frame, text="Run", command=create_files)
run_button.grid(row=2, column=0, pady=20)

# Exit button
exit_button = ttk.Button(frame, text="Exit", command=exit_program)
exit_button.grid(row=2, column=1, pady=20)

# Display status
status_label = ttk.Label(frame, text="")
status_label.grid(row=3, column=0, columnspan=2)

root.mainloop()