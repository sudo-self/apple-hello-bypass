#jayrain.py 

import os
import subprocess
import tkinter as tk
from tkinter import messagebox
import webbrowser


root = tk.Tk()
root.title('Jayra1n Apple Hello screen Bypass')


root.geometry("800x600")
root.resizable(False, False) 


frame = tk.Frame(root, width="800", height="600", bg="#1a1a1a")
frame.pack(fill=tk.BOTH, expand=True)


root.iconphoto(False, tk.PhotoImage(file='./jesse.png'))


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


def showDFUMessage():
    messagebox.showinfo("Step 1", "Put your iDevice into DFU mode.\n\nClick Ok once it's ready in DFU mode to proceed.")


def clear():
    folders_to_delete = ['./palera1n/blobs', './palera1n/work']
    for folder in os.listdir('./palera1n'):
        if folder.startswith('boot'):
            folders_to_delete.append(f'./palera1n/{folder}')

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

    output = execute_command("./device/ideviceinfo")

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
        messagebox.showinfo('Ready to Jailbreak...', f'Ayeee, iOS {LAST_CONNECTED_IOS_VER}.\n\nJesse will now bypass iOS {LAST_CONNECTED_IOS_VER} Semi-Tethered.')
        print("Starting jailbreak...")
        execute_command("idevicepair unpair")
        execute_command("idevicepair pair")

        os.system(f"cd ./palera1n/ && ./palera1n.sh --tweaks --semi-tethered {LAST_CONNECTED_IOS_VER}")
        print("Device is bypassed!\n")
        messagebox.showinfo('Boom pow!', 'Apple lockscreen bypass brought to you by JesseJesse.xyz')


def enterRecMode():
    print("drip drop Recovery...")
    execute_command("./device/enterrecovery.sh")


def exitRecMode():
    print("Knock Knock wake up...")
    execute_command("./device/exitrecovery.sh")


def show_about():
    about_window = tk.Toplevel(root)
    about_window.title("Jayrain.py")
    about_window.configure(bg="#1a1a1a")


    about_text = (
        "Welcome to Jayrain! A Python Lockscreen and Jailbreak tool!\n"
        "\n"
        "checkm8 exploit and palera1n jailbreak\n"
        "\n"
        " 1.05 - 163."
    )

    about_label = tk.Label(about_window, text=about_text, font=('Helvetica', 12), bg="#1a1a1a", fg="white", justify="left")
    about_label.pack(padx=20, pady=20)

 
    jesse_image = tk.PhotoImage(file='./jesse.png')
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


twitter_label = tk.Label(frame, text="@ilostmyipod", font=("Helvetica", 20), fg="gold", bg="#1a1a1a", cursor="hand2")
twitter_label.pack(pady=10)
twitter_label.bind("<Button-1>", opentwitter)

root.mainloop()









