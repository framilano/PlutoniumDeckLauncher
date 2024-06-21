# PlutoniumDeckLauncher

A straightforward launcher mainly developed for Steam Deck, but can be used wherever Plutonium is supported.

The main objective is giving a shortcut to play offline Call of Duty Plutonium-supported titles.

![immagine](https://github.com/framilano/PlutoniumDeckLauncher/assets/28491164/345a3045-9b24-45e0-8c6f-35f3f5710c11)


Resolution is set at 1280x800.

## Requirements
- Game files (bought on Steam, due to Plutonium Steam Ownership verification)
- [Plutonium](https://cdn.plutonium.pw/updater/plutonium.exe)

## How to install
1. Download and extract the `PlutoniumDeckLauncher.zip` in Releases
2. Here's my folder structure in `/home/deck/NoLauncherGames/Plutonium`:

```
├── PlutoniumWAW    # Contains World at War game files
├── PlutoniumBO2    # Contains Black Ops 1 game files
├── PlutoniumBO1    # Contains Black Ops 2 game files
├── PlutoniumIW5    # Contains MW3 game files
├── plutonium.exe
└── PlutoniumDeckLauncher
    ├── configs
    ├── images
    └── PlutoniumDeckLauncher.exe
```
You can change this folder structure editing the `plutonium_deck_launcher.json` inside the `configs` folder, maybe you need to point to a different folder or drive to retrieve your game files.

3. Add PlutoniumDeckLauncher.exe as non-steam game in `Desktop Mode`.
4. Set `Proton Experimental` or `Proton-GE` in compatibility settings.
5. Add the following line on command launch arguments (fsync and esync are known to cause issues with BO1/2):

    `PROTON_NO_ESYNC=1 PROTON_NO_FSYNC=1 %command%` 

6. Back in `Gaming Mode` and open the newly created shortcut, if everything's okay, you should be able to see the Deck Launcher. You need to download the necessary Plutonium online files first, so just touch/click on CLASSIC PLUTONIUM on top and let it configure the proton bottle with all the necessary Plutonium files.
7. Eventually the download will end and the usual "official" Plutonium launcher should launch, login and setup the game paths from there if you need to play online.
8. Exit PlutoniumDeckLauncher and open it back, now all shortcuts are available to use!

## Configuration

There are some editable fields in configs/plutonium_deck_launcher.json:
- `player_ingame_name` set your ingame username while playing offline
- `t4/5/6/iw6_folder` set your game files path
- `plutonium_exe` set your plutonium.exe path
- `windows_user_folder` set your windows/bottle username (the launcher uses it to find Plutonium appdata files), on Steam Deck the default username is "steamuser"
- `quit_on_startup` exit the launcher when booting the game, or leave it in background so you can open it back later

