from tkinter import Tk, Button, PhotoImage
from subprocess import Popen
import json


json_file = json.load(open("configs/plutonium_deck_launcher_config.json", "r"))

#JSON Variables
user_folder = json_file["windows_user_folder"]
player_ingame_name = json_file["player_ingame_name"]
t4_folder = json_file["t4_folder"]
t5_folder = json_file["t5_folder"]
t6_folder = json_file["t6_folder"]
iw5_folder = json_file["iw5_folder"]

bootstrapper_path = f"C:\\Users\\{user_folder}\\AppData\\Local\\Plutonium\\bin\\plutonium-bootstrapper-win32.exe"
plutonium_local_path = f"C:\\Users\\{user_folder}\\AppData\\Local\\Plutonium"

#TKinter Stuff

root = Tk()  # create a root widget
root.title("Plutonium Deck Launcher")
total_width = 1280
total_height = 800
root.geometry(f"{total_width}x{total_height}")
root.configure(background="#080808")
root.resizable(False, False)

photo_classic = PhotoImage(file = "images/classic.png")
photo_t4sp = PhotoImage(file = "images/t4sp.png")
photo_t4mp = PhotoImage(file = "images/t4mp.png")
photo_t5sp = PhotoImage(file = "images/t5sp.png")
photo_t5mp = PhotoImage(file = "images/t5mp.png")
photo_t6zm = PhotoImage(file = "images/t6zm.png")
photo_t6mp = PhotoImage(file = "images/t6mp.png")
photo_iw5mp = PhotoImage(file = "images/iw5mp.png")


def launch_classic():
    Popen([json_file["plutonium_exe"]])
    root.quit()
   
def launch_offline_game(game_name):
    game_folder = ""
    if (game_name == "t4sp" or game_folder == "t4mp"): game_folder = t4_folder
    elif (game_name == "t5sp" or game_folder == "t5mp"): game_folder = t5_folder
    elif (game_name == "t6zm" or game_folder == "t6mp"): game_folder = t6_folder
    elif (game_name == "iw5mp"): game_folder = iw5_folder

    print([bootstrapper_path, game_name, game_folder, "+name", player_ingame_name, "-lan"])
    Popen([bootstrapper_path, game_name, game_folder, "+name", player_ingame_name, "-lan"], cwd=plutonium_local_path)
    root.quit()

def define_buttons():
    classic_button = Button(root, command = launch_classic, image=photo_classic, highlightthickness = 0, bd = 0)
    classic_button.grid(row = 0, column = 0, columnspan=2)

    #T4
    t4sp_button = Button(root, command = lambda: launch_offline_game("t4sp"), image=photo_t4sp, highlightthickness = 0, bd = 0)
    t4sp_button.grid(row = 1, column = 0, columnspan=1)
    
    t4mp_button = Button(root, command = lambda: launch_offline_game("t4mp"), image=photo_t4mp, highlightthickness = 0, bd = 0)
    t4mp_button.grid(row = 1, column = 1, columnspan=1)

    #T5
    t5sp_button = Button(root, command = lambda: launch_offline_game("t5sp"), image=photo_t5sp, highlightthickness = 0, bd = 0)
    t5sp_button.grid(row = 2, column = 0, columnspan=1)
    
    t5mp_button = Button(root, command = lambda: launch_offline_game("t5mp"), image=photo_t5mp, highlightthickness = 0, bd = 0)
    t5mp_button.grid(row = 2, column = 1, columnspan=1)

    #T6
    t6zm_button = Button(root, command = lambda: launch_offline_game("t6zm"), image=photo_t6zm, highlightthickness = 0, bd = 0)
    t6zm_button.grid(row = 3, column = 0, columnspan=1, sticky='ewsn')
    
    t6mp_button = Button(root, command = lambda: launch_offline_game("t6mp"), image=photo_t6mp, highlightthickness = 0, bd = 0)
    t6mp_button.grid(row = 3, column = 1, columnspan=1, sticky='ewsn')

    #IW5
    iw5mp_button = Button(root, command = lambda: launch_offline_game("iw5mp"), image=photo_iw5mp, highlightthickness = 0, bd = 0)
    iw5mp_button.grid(row = 4, column = 0, columnspan=2, sticky='ewsn')

define_buttons()

root.mainloop()