import os
import subprocess
import tkinter as tk
from tkinter import messagebox
import webbrowser
import requests
from io import BytesIO
from PIL import Image, ImageTk
import sys

# Function to handle path for PyInstaller builds
def resource_path(relative_path):
    """ Get the absolute path to a resource, works for dev and for PyInstaller """
    try:
        base_path = sys._MEIPASS  # This is used when running the PyInstaller bundle
    except AttributeError:
        base_path = os.path.abspath(".")  # This is used when running the script normally

    return os.path.join(base_path, relative_path)

# Load image function
def load_image_from_url(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        img_data = response.content
        img = Image.open(BytesIO(img_data))
        return ImageTk.PhotoImage(img)
    except requests.RequestException as e:
        print(f"Error downloading image: {e}")
        return None

# Tkinter setup
root = tk.Tk()
root.title('Jayra1n Apple Hello screen Bypass')
root.geometry("800x600")
root.resizable(False, False)

frame = tk.Frame(root, width="800", height="600", bg="#1a1a1a")
frame.pack(fill=tk.BOTH, expand=True)

# Load the image
image_url = 'https://server.jessejesse.xyz/public/jesse.png'
jesse_image = load_image_from_url(image_url)

if jesse_image:
    root.iconphoto(False, jesse_image)

# Button creator function
def create_button(frame, text, command, color):
    return tk.Button(
        frame,
        text=text,
        command=command,
        font=("Helvetica", 12),
        fg="black",
        bg="black",
        activebackground=color,
        borderwidth=0,
        relief="raised",
        width=15,
        height=2,
        highlightthickness=0,
        bd=0,
        highlightcolor=color,
        highlightbackground=color,
        activeforeground="white",
        cursor="hand2",
        padx=20,
        pady=5
    )

LAST_CONNECTED_UDID = ""
LAST_CONNECTED_IOS_VER = ""

# Functions for UI and logic
def showDFUMessage():
    messagebox.showinfo("Step 1", "Put your iDevice into DFU mode.\n\nClick Ok once it's ready in DFU mode to proceed.")

def clear():
    palera1n_path = resource_path('./palera1n')
    folders_to_delete = [os.path.join(palera1n_path, 'blobs'), os.path.join(palera1n_path, 'work')]
    for folder in os.listdir(palera1n_path):
        if folder.startswith('boot'):
            folders_to_delete.append(os.path.join(palera1n_path, folder))
    for folder in folders_to_delete:
        if os.path.exists(folder):
            os.system(f'rm -rf {folder}')
            print(f'{folder} deleted.')
    messagebox.showinfo("Done", "Jayrain.py")

def quitProgram():
    print("Exiting...")
    root.quit()

def opentwitter(event):
    webbrowser.open('https://x.com/ilostmyipod', new=2)

def execute_command(command):
    try:
        result = subprocess.run(command, shell=True, check=True, text=True, capture_output=True)
        print(result.stdout)
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"Error executing command: {e}")
        messagebox.showerror("Error", f"An error occurred: {e.stderr.strip()}")

def startbypass():
    global LAST_CONNECTED_UDID, LAST_CONNECTED_IOS_VER
    print("Searching for connected device...")
    execute_command("idevicepair unpair")
    execute_command("idevicepair pair")
    device_path = resource_path('./device/ideviceinfo')
    output = execute_command(device_path)
    if "ERROR:" in output:
        print("ERROR: No device found!")
        messagebox.showinfo("No device detected!", "Try disconnecting and reconnecting your device.")
        return
    try:
        lines = output.splitlines()
        for line in lines:
            if "UniqueDeviceID:" in line:
                LAST_CONNECTED_UDID = line.split(': ')[1].strip()
            elif "ProductVersion:" in line:
                LAST_CONNECTED_IOS_VER = line.split(': ')[1].strip()
        if len(LAST_CONNECTED_UDID) > 38:
            print("Found UDID: " + LAST_CONNECTED_UDID)
            messagebox.showinfo("Apple Device Located", f"Found iDevice on iOS {LAST_CONNECTED_IOS_VER}")
        else:
            raise ValueError("something is missing")
    except Exception as e:
        print(e)
        messagebox.showinfo("Jayrain could not locate device", "I recommend reconnecting or swapping the cable")
    if len(LAST_CONNECTED_IOS_VER) < 2:
        messagebox.showinfo('Jailbreak Failed', 'I need the valid iOS version. example: 14.1')
    else:
        palera1n_path = resource_path('./palera1n/palera1n.sh')
        messagebox.showinfo('Ready to Jailbreak...', f'Ayeee, iOS {LAST_CONNECTED_IOS_VER}.\n\nJesse will now bypass iOS {LAST_CONNECTED_IOS_VER} Semi-Tethered.')
        print("Starting jailbreak...")
        execute_command("idevicepair unpair")
        execute_command("idevicepair pair")
        os.system(f"cd {resource_path('./palera1n/')} && ./palera1n.sh --tweaks --semi-tethered {LAST_CONNECTED_IOS_VER}")
        print("Device is bypassed!\n")
        messagebox.showinfo('Boom pow!', 'Apple lockscreen bypass brought to you by JesseJesse.xyz')

def enterRecMode():
    device_path = resource_path('./device/enterrecovery.sh')
    print("drip drop Recovery...")
    execute_command(device_path)

def exitRecMode():
    device_path = resource_path('./device/exitrecovery.sh')
    print("Knock Knock wake up...")
    execute_command(device_path)

def show_about():
    about_window = tk.Toplevel(root)
    about_window.title("Jayrain.py")
    about_window.configure(bg="#1a1a1a")
    about_text = (
        "Welcome to Jayrain! A Python Lockscreen and Jailbreak tool!\n"
        "\n"
        "checkm8 exploit and palera1n jailbreak\n"
        "\n"
        " 15.0 - 16.3"
    )
    about_label = tk.Label(about_window, text=about_text, font=('Helvetica', 12), bg="#1a1a1a", fg="white", justify="left")
    about_label.pack(padx=20, pady=20)
    image_url = 'https://server.jessejesse.xyz/public/jesse.png'
    jesse_image = load_image_from_url(image_url)
    if jesse_image:
        image_label = tk.Label(about_window, image=jesse_image, bg="#1a1a1a")
        image_label.image = jesse_image
        image_label.pack(pady=10)
    support_info = (
        "CASHAPP: $ilostmyipod\n"
        "\n"
        "ETH: 0x47aCF0718770f3E1a57e4cCEA7609aEd95E220b5\n"
        "\n"
        "BITCOIN: 32WfTVZTzoJXSTdgfLer1Ad3SMVvjokkbX\n"
        "\n"
        "beforeicloud@yahoo.com\n"
    )
    support_label = tk.Label(about_window, text=support_info, font=('Helvetica', 12), bg="#1a1a1a", fg="white", justify="left")
    support_label.pack(padx=20, pady=10)

# GUI layout
title_label = tk.Label(frame, text="Jayrain  Lockscreen Bypass ", font=("Helvetica", 22), bg="#1a1a1a", fg="#1E90FF")
title_label.pack(pady=20)

text_label = tk.Label(frame, text="iOS 15.0-16.3", font=("Helvetica", 18), bg="#1a1a1a", fg="white")
text_label.pack(pady=10)

start_button = create_button(frame, "Start Bypass", startbypass, "green")
start_button.pack(pady=10)

clear_button = create_button(frame, "Clear Files", clear, "orange")
clear_button.pack(pady=10)

rec_button = create_button(frame, "Enter Recovery", enterRecMode, "blue")
rec_button.pack(pady=10)

exit_rec_button = create_button(frame, "Exit Recovery", exitRecMode, "blue")
exit_rec_button.pack(pady=10)

about_button = create_button(frame, "More Info", show_about, "yellow")
about_button.pack(pady=10)

quit_button = create_button(frame, "Quit", quitProgram, "red")
quit_button.pack(pady=10)

twitter_label = tk.Label(frame, text="Jesse Twitter @ilostmyipod", font=("Helvetica", 12), bg="#1a1a1a", fg="white", cursor="hand2")
twitter_label.pack(pady=20)
twitter_label.bind("<Button-1>", opentwitter)

root.mainloop()











