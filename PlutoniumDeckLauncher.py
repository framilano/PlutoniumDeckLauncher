import random
from tkinter import Frame, Tk, Button, PhotoImage
from subprocess import Popen
import json
from pygame import mixer

class Config():

    def __init__(self):
        self.json_file = json.load(open("configs/plutonium_deck_launcher_config.json", "r"))

        #JSON Variables
        self.user_folder = self.json_file["windows_user_folder"]
        self.player_ingame_name = self.json_file["player_ingame_name"]
        self.list_of_songs = self.json_file["list_of_songs"]
        self.background_music_enabled = self.json_file["background_music_enabled"]

        self.t4_folder = self.json_file["t4_folder"]
        self.t5_folder = self.json_file["t5_folder"]
        self.t6_folder = self.json_file["t6_folder"]
        self.iw5_folder = self.json_file["iw5_folder"]

        self.bootstrapper_path = f"C:\\Users\\{self.user_folder}\\AppData\\Local\\Plutonium\\bin\\plutonium-bootstrapper-win32.exe"
        self.plutonium_local_path = f"C:\\Users\\{self.user_folder}\\AppData\\Local\\Plutonium"

class DeckLauncher(Frame):

    def on_enter(self, event):
        event.widget["bd"] = 10

    def on_leave(self, event):
        event.widget["highlightthickness"] = 0

    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

        self.load_images()

        #Classic Plutonium Launcher
        classic_button = Button(self, command = self.launch_classic, image=self.photo_classic, cursor="hand2", highlightthickness = 0, bd = 0)
        classic_button.grid(row = 0, column = 0, columnspan=2)

        #T4
        t4sp_button = Button(self, command = lambda: self.launch_offline_game("t4sp"), image=self.photo_t4sp, cursor="hand2", highlightthickness = 0, bd = 0)
        t4sp_button.grid(row = 1, column = 0, columnspan=1)
        t4mp_button = Button(self, command = lambda: self.launch_offline_game("t4mp"), image=self.photo_t4mp, cursor="hand2", highlightthickness = 0, bd = 0)
        t4mp_button.grid(row = 1, column = 1, columnspan=1)

        #T5
        t5sp_button = Button(self, command = lambda: self.launch_offline_game("t5sp"), image=self.photo_t5sp, cursor="hand2", highlightthickness = 0, bd = 0)
        t5sp_button.grid(row = 2, column = 0, columnspan=1)
        t5mp_button = Button(self, command = lambda: self.launch_offline_game("t5mp"), image=self.photo_t5mp, cursor="hand2", highlightthickness = 0, bd = 0)
        t5mp_button.grid(row = 2, column = 1, columnspan=1)

        #T6
        t6zm_button = Button(self, command = lambda: self.launch_offline_game("t6zm"), image=self.photo_t6zm, cursor="hand2", highlightthickness = 0, bd = 0)
        t6zm_button.grid(row = 3, column = 0, columnspan=1)
        t6mp_button = Button(self, command = lambda: self.launch_offline_game("t6mp"), image=self.photo_t6mp, cursor="hand2", highlightthickness = 0, bd = 0)
        t6mp_button.grid(row = 3, column = 1, columnspan=1)

        #IW5
        iw5mp_button = Button(self, command = lambda: self.launch_offline_game("iw5mp"), image=self.photo_iw5mp, cursor="hand2", highlightthickness = 0, bd = 0)
        iw5mp_button.grid(row = 4, column = 0, columnspan=2)

        #Starts music
        if (config.json_file["background_music_enabled"]): self.start_music()

        total_width = 1280
        total_height = 800
        parent.title("Plutonium Deck Launcher")
        parent.geometry(f"{total_width}x{total_height}")
        parent.configure(background="#080808")
        parent.resizable(False, False)
    
    def load_images(self):
        self.photo_classic = PhotoImage(file = "assets/images/classic.png")
        self.photo_t4sp = PhotoImage(file = "assets/images/t4sp.png")
        self.photo_t4mp = PhotoImage(file = "assets/images/t4mp.png")
        self.photo_t5sp = PhotoImage(file = "assets/images/t5sp.png")
        self.photo_t5mp = PhotoImage(file = "assets/images/t5mp.png")
        self.photo_t6zm = PhotoImage(file = "assets/images/t6zm.png")
        self.photo_t6mp = PhotoImage(file = "assets/images/t6mp.png")
        self.photo_iw5mp = PhotoImage(file = "assets/images/iw5mp.png")
        

    @staticmethod
    def start_music():
        mixer.init()
        song_index = random.randint(0, len(config.list_of_songs) - 1)
        mixer.music.load(f"assets/music/{config.list_of_songs[song_index]}.mp3")
        mixer.music.set_volume(0.2)
        mixer.music.play(-1)

    @staticmethod
    def launch_classic():
        if (config.json_file["background_music_enabled"]): mixer.music.stop()
        Popen([config.json_file["plutonium_exe"]])
        if (config.json_file["quit_on_startup"]): root.quit()
    
    @staticmethod
    def launch_offline_game(game_name):
        game_folder = ""
        if (game_name == "t4sp" or game_name == "t4mp"): game_folder = config.t4_folder
        elif (game_name == "t5sp" or game_name == "t5mp"): game_folder = config.t5_folder
        elif (game_name == "t6zm" or game_name == "t6mp"): game_folder = config.t6_folder
        elif (game_name == "iw5mp"): game_folder = config.iw5_folder

        if (config.json_file["background_music_enabled"]): mixer.music.stop()
        
        Popen([config.bootstrapper_path, game_name, game_folder, "+name", config.player_ingame_name, "-lan"], cwd=config.plutonium_local_path)
        if (config.json_file["quit_on_startup"]): root.quit()
        


if __name__ == "__main__":
    config = Config()
    root = Tk()
    launcher = DeckLauncher(root)
    launcher.pack()

    root.mainloop()