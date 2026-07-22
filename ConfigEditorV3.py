import sys
from pathlib import Path
from tkinter.filedialog import askopenfilename
import os
import shutil

#globals
if getattr(sys, 'frozen', False):
    BASE_PATH = Path(sys.executable).parent
else:
    BASE_PATH = Path(__file__).resolve().parent

lineLength = 84
validInputs = ["0", "1", "2", "3", "4"]

#helper functions

#print header
def printHeader():
    print(
        "====================================================================================\n"
        "                           RPCS3 Configuration Tool\n"
        "===================================================================================="
    )

def printLine():
    print("=" * lineLength)

#clears console
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def getRpcs3Path():
    while True:
        clear()
        printHeader()
        print("Please locate rpcs3.exe in your rpcs3 folder, Example: Desktop\\rpcs3\\RPCS3\\rpcs3.exe")

        oldFilePath = askopenfilename(title="Locate your rpcs3.exe in your rpcs3 instalation folder",filetypes=[("exe", "*.exe")])
        newFilePath = oldFilePath.replace("/rpcs3.exe", "")

        if oldFilePath != newFilePath:
            return newFilePath
        else:
            clear()
            input(f"(ERROR) Failed to get rpcs3 path, press (ENTER) to continue")
            continue

#classes

class GameInfo:
    def __init__(self, gameId, defaultConfig, settings):
        self.gameId = gameId
        self.defaultConfig = defaultConfig
        self.settings = settings

class EbootManager:
    GAME_IDS = (
        "BLUS30464",
        "BLES00760",
    )

    def __init__(self, rpcs3Path):
        self.rpcs3Path = Path(rpcs3Path)
        self.defaultEboot = BASE_PATH / "Dependencies" / "EBOOT.BIN"

    def replaceEboots(self):
        for ebootPath in self.getEbootPaths():
            if ebootPath.exists():
                shutil.copy(self.defaultEboot, ebootPath)
                print(f"Replaced {ebootPath}")

    def getEbootPaths(self):
        ebootPaths = []

        for gameId in self.GAME_IDS:
            ebootPaths.append(self.getInstalledEbootPath(gameId))

            diskEbootPath = self.getDiskEbootPath(gameId)
            if diskEbootPath is not None:
                ebootPaths.append(diskEbootPath)

        return ebootPaths

    def getInstalledEbootPath(self, gameId):
        return self.rpcs3Path / "dev_hdd0" / "game" / gameId / "USRDIR" / "EBOOT.BIN"

    def getDiskEbootPath(self, gameId):
        gamesConfigPath = self.rpcs3Path / "config" / "games.yml"

        if not gamesConfigPath.exists():
            print("Cannot find games.yml")
            return None

        with gamesConfigPath.open("r") as file:
            for line in file:
                key, _, value = line.partition(":")

                if key.strip() == gameId:
                    return Path(value.strip()) / "PS3_GAME" / "USRDIR" / "EBOOT.BIN"

        return None

class ConfigEditor:
    def __init__(self, rpcs3Path):
        self.rpcs3Path = Path(rpcs3Path)

    def getValue(self, key : str, gameInfo : GameInfo) -> str:
        if key in gameInfo.settings:
            return(gameInfo.settings[key])
        else:
            return None
    
    def updateConfigSettings(self, configPath, gameInfo  : GameInfo):

        lines = []

        with open(configPath, 'r') as file:   

            for line in file:
                lines.append(line.rstrip())

            for i, line in enumerate(lines):

                key = line.split(":",maxsplit=1)[0]
                value = self.getValue(key, gameInfo)
                
                if value != None:
                    lines[i] = f"{key}: {value}"
                    print(value)

            with open(configPath,'w') as file:
                for line in lines:
                    file.write(line + "\n")

    def editConfig(self, gameInfo : GameInfo):
        configPath = Path(self.rpcs3Path / "config" / "custom_configs" / f"config_{gameInfo.gameId}.yml")

        if configPath.exists() == True:
            print(f"editing {configPath}")
            self.updateConfigSettings(configPath, gameInfo)

        else:
            try:
                print(f"Creating {configPath} because it does not exist")
                shutil.copy(gameInfo.defaultConfig, configPath)

            except shutil.SameFileError:
                    print("Source and destination represents the same file.")

            except PermissionError:
                print("Permission denied.")
            
            except FileNotFoundError:
                print("Default config was not found.")

#skate 3 BLUS versoin
skate_3_BLUS30464 = GameInfo(
    gameId = "BLUS30464",
    defaultConfig = BASE_PATH / "Dependencies" / "config_BLUS30464.yml",
    settings = {
        "  Internet enabled": "Connected",
        "  IP address": "0.0.0.0",
        "  Bind address": "0.0.0.0",
        "  DNS address": "8.8.8.8",             
        "  IP swap list": "gosredirector.ea.com==172.237.109.212&&downloads.skate.online.ea.com==172.237.109.212",
        "  UPNP Enabled": "true",
        "  PSN status": "RPCN",
        "  PSN Country": "us",
        "  Clans Enabled": "false",
        "  XFloat Accuracy": "Approximate",
        "  SPU loop detection": "false",
        "  PPU Decoder": "Recompiler (LLVM)",
        "  SPU Decoder": "Recompiler (LLVM)"
    }
)

#skate 3 BLES version
skate_3_BLES00760 = GameInfo(
    gameId = "BLES00760",
    defaultConfig = BASE_PATH / "Dependencies" / "config_BLES00760.yml",
    settings = {
        "  Internet enabled": "Connected",
        "  IP address": "0.0.0.0",
        "  Bind address": "0.0.0.0",
        "  DNS address": " 8.8.8.8",             
        "  IP swap list": "gosredirector.ea.com==172.237.109.212&&downloads.skate.online.ea.com==172.237.109.212",
        "  UPNP Enabled": "true",
        "  PSN status": "RPCN",
        "  PSN Country": "us",
        "  Clans Enabled": "false",
        "  XFloat Accuracy": "Approximate",
        "  SPU loop detection": "false",
        "  PPU Decoder": "Recompiler (LLVM)",
        "  SPU Decoder": "Recompiler (LLVM)"
    }
)

#skate 2 BLUS version
skate_2_BLUS30253 = GameInfo(
    gameId = "BLUS30253",
    defaultConfig = BASE_PATH / "Dependencies" / "config_BLUS30253.yml",
    settings = { 
        "  Internet enabled": "Connected",
        "  IP address": "0.0.0.0",
        "  Bind address": "0.0.0.0",
        "  DNS address": " 8.8.8.8",             
        "  IP swap list": "skate2-ps3.fesl.ea.com=172.237.109.212",
        "  UPNP Enabled": "true",
        "  PSN status": "RPCN",
        "  PSN Country": "us",
        "  Clans Enabled": "false",
        "  XFloat Accuracy": "Approximate",
        "  SPU loop detection": "false",
        "  PPU Decoder": "Recompiler (LLVM)",
        "  SPU Decoder": "Recompiler (LLVM)"
    }
)

#skate 2 BLES version
skate_2_BLES00461 = GameInfo(
    gameId = "BLES00461",
    defaultConfig = BASE_PATH / "Dependencies" / "config_BLES00461.yml",
    settings = { 
        "  Internet enabled": "Connected",
        "  IP address": "0.0.0.0",
        "  Bind address": "0.0.0.0",
        "  DNS address": " 8.8.8.8",             
        "  IP swap list": "skate2-ps3.fesl.ea.com=172.237.109.212",
        "  UPNP Enabled": "true",
        "  PSN status": "RPCN",
        "  PSN Country": "us",
        "  Clans Enabled": "false",
        "  XFloat Accuracy": "Approximate",
        "  SPU loop detection": "false",
        "  PPU Decoder": "Recompiler (LLVM)",
        "  SPU Decoder": "Recompiler (LLVM)"
    }
)

#skate 1 BLUS version
skate_1_BLUS30059 = GameInfo(
    gameId = "BLUS30059",
    defaultConfig = BASE_PATH / "Dependencies" / "config_BLUS30059.yml",
    settings = { 
        "  Internet enabled": "Connected",
        "  IP address": "0.0.0.0",
        "  Bind address": "0.0.0.0",
        "  DNS address": " 8.8.8.8",             
        "  IP swap list": "skate-ps3.fesl.ea.com=172.237.109.212&&downloads.skate.online.ea.com=172.237.109.212",
        "  UPNP Enabled": "true",
        "  PSN status": "RPCN",
        "  PSN Country": "us",
        "  Clans Enabled": "false",
        "  XFloat Accuracy": "Approximate",
        "  SPU loop detection": "false",
        "  PPU Decoder": "Recompiler (LLVM)",
        "  SPU Decoder": "Recompiler (LLVM)"
    }
)

#skate 1 BLES version
skate_1_BLES00124 = GameInfo(
    gameId = "BLES00124",
    defaultConfig = BASE_PATH / "Dependencies" / "config_BLES00124.yml",
    settings = { 
        "  Internet enabled": "Connected",
        "  IP address": "0.0.0.0",
        "  Bind address": "0.0.0.0",
        "  DNS address": " 8.8.8.8",             
        "  IP swap list": "skate-ps3.fesl.ea.com=172.237.109.212&&downloads.skate.online.ea.com=172.237.109.212",
        "  UPNP Enabled": "true",
        "  PSN status": "RPCN",
        "  PSN Country": "us",
        "  Clans Enabled": "false",
        "  XFloat Accuracy": "Approximate",
        "  SPU loop detection": "false",
        "  PPU Decoder": "Recompiler (LLVM)"
    }
)

def main():

    rpcs3Path = Path(getRpcs3Path())
    configEditor = ConfigEditor(rpcs3Path)
    ebootManager = EbootManager(rpcs3Path)

    while True:
        clear()
        printHeader()
        print("Please select a game to patch for online play")
        print("[1] Skate 1")
        print("[2] skate 2")
        print("[3] skate 3")
        print("[4] Patch all")
        print("[0] (EXIT)")
        printLine()

        userInput = input("Enter number here: ")

        if userInput not in validInputs:
            clear()
            input("(ERROR) you did not enter a valid number please press (ENTER) to continue ):")
            continue

        break

    printLine()

    if userInput == "0":
        quit(0)
    
    if userInput == "1":
        configEditor.editConfig(skate_1_BLUS30059)
        configEditor.editConfig(skate_1_BLES00124)
    
    if userInput == "2":
        configEditor.editConfig(skate_2_BLUS30253)
        configEditor.editConfig(skate_2_BLES00461)
    
    if userInput == "3":
        configEditor.editConfig(skate_3_BLUS30464)
        configEditor.editConfig(skate_3_BLES00760)
        ebootManager.replaceEboots()
    
    if userInput == "4":
        GAMES: list[GameInfo] = [skate_1_BLUS30059, skate_1_BLES00124, skate_2_BLUS30253, skate_2_BLES00461, skate_3_BLUS30464, skate_3_BLES00760]
        for gameInfo in GAMES:
            printLine()
            configEditor.editConfig(gameInfo)
        printLine()
        ebootManager.replaceEboots()
 
    printLine()
    print("All config files have been edited or created, you can now exit the program and proceed with the next instructions!!!")
    input()


if __name__ == '__main__':
    main()





