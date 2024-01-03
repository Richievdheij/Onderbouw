import tkinter as tk
window = tk.Tk()
import os.path

if not os.path.exists('actions.log'):
    with open('.gitignore', 'w') as gitignore:
        gitignore.write('actions.log')
    
    gitignore.close()


action_log = open('actions.log', 'a')


# Makes the button
def make_button():
    button = tk.Button(text='Switch light on', bg="white", fg="black", command = switch_light) # Add the button
    button.pack(pady = 20, padx = 20) # Window size
    window['bg'] = "black" 

    return button


# Button input reaction
def switch_light():
    # If light is off
    if button['text'] == "Switch light off":
        button['text'] = "Switch light on" # Change button text
        window['bg'] = "black" # Change window background color
        print("Light is off")
    
    # If light is on
    else:
        button['text'] = "Switch light off"
        window['bg'] = "yellow" # Change window background color
        print("Light is on") # Change button text


if __name__ == "__main__":
    button = make_button()
    window.mainloop()