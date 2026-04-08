import sys
from pathlib import Path
from tkinter.filedialog import askopenfilename
import json
import shutil

if getattr(sys, 'frozen', False):
    BASE_PATH = Path(sys.executable).parent
else:
    BASE_PATH = Path(__file__).resolve().parent

class EbootManager:
    def __init__(self, configPath : str):
        self.configPath = configPath
        self.defaultEboot = BASE_PATH / "Dependencies" / "EBOOT.BIN"
        self.blusEbootPath = Path(configPath + "/dev_hdd0/game/BLUS30464/USRDIR/EBOOT.BIN")
        self.blesEbootPath = Path(configPath + "/dev_hdd0/game/BLES00760/USRDIR/EBOOT.BIN")
        self.diskBlusEbootPath = self.getDiskEbootPath("BLUS30464")
        self.diskBlesEbootPath = self.getDiskEbootPath("BLES00760")
        self.ebootPaths = [self.blusEbootPath, self.blesEbootPath,]

        if self.diskBlesEbootPath != None:
            self.ebootPaths.append(self.diskBlesEbootPath)

        if self.diskBlusEbootPath != None:
            self.ebootPaths.append(self.diskBlusEbootPath)

    def replaceEboots(self):
        for ebootPath in self.ebootPaths:
            if ebootPath.exists():
                print(f"Replaced {ebootPath}")
                shutil.copy(self.defaultEboot, ebootPath)

    def getDiskEbootPath(self, version) -> str:
        gameConfigPath = Path(self.configPath + "/games.yml")
        if gameConfigPath.exists():
            with open(gameConfigPath, "r") as f:
                for line in f:
                    buffer = line.split(":", 1)
                    if buffer[0] == version:
                        diskPath = Path(buffer[1].strip())
                        ebootPath = diskPath / "PS3_GAME" / "USRDIR" / "EBOOT.BIN"
                        return ebootPath
        else:
            print("Cannot find games config path")


class ConfigEditor:
    def __init__(self, configPath):
        self.configPath = configPath
        self.swapListIP_Path = BASE_PATH / "Dependencies" / "SwapList.json"
        self.swapListIP = self.getSwapListIP(self.swapListIP_Path)
        self.settings = {
            "  Internet enabled": "  Internet enabled: Connected",
            "  IP address": "  IP address: 0.0.0.0",
            "  Bind address": "  Bind address: 0.0.0.0",
            "  DNS address": "  DNS address: 8.8.8.8",
            "  IP swap list": self.swapListIP,
            "  UPNP Enabled": "  UPNP Enabled: true",
            "  PSN status": "  PSN status: RPCN",
            "  PSN Country": "  PSN Country: us",
            "  Clans Enabled": "  Clans Enabled: false",
            "  XFloat Accuracy": "  XFloat Accuracy: Approximate",
            "  SPU loop detection": "  SPU loop detection: false"
        }

    def getSwapListIP(self, swapListIP_Path : str) -> str:
        with open(swapListIP_Path, "r") as f:
            data = json.load(f)
        return data["swapListIP"]

    def getValue(self, key : str) -> str:
        if key in self.settings:
            return(self.settings[key])
        else:
            return None

    def changeConfigSettings(self, config: str):
        lines = []
        with open(config, 'r') as file:
            for line in file:
                lines.append(line.rstrip())
        for i, line in enumerate(lines):
            key = line.split(":",maxsplit=1)[0]
            value = self.getValue(key)
            if value != None:
                lines[i] = value
                print(value)
        with open(config,'w') as file:
            for line in lines:
                file.write(line + "\n")

    def editConfigs(self):
        if self.configPath == None:
            print("Invalid path or no path was selected")
            exit()
        else:
            defaultConfig = BASE_PATH / "Dependencies" / "config_default.yml"
            BLUS = Path(self.configPath + "/custom_configs/config_BLUS30464.yml")
            BLES = Path(self.configPath + "/custom_configs/config_BLES00760.yml")
            configs = [BLUS, BLES]

            for config in configs:
                path = Path(config)
                if path.exists():
                    print("-----------------------------------------------------------------------------------------------------------------")
                    print(f"Editing {path}")
                    self.changeConfigSettings(config)
                else:
                    try:
                        print(f"Creating {path} because it does not exist")
                        path.parent.mkdir(parents=True, exist_ok=True)
                        shutil.copy(defaultConfig, path)
                    except shutil.SameFileError:
                        print("Source and destination represents the same file.")
                    except PermissionError:
                        print("Permission denied.")

def getRPCS3ConfigPath():
    oldFilePath = askopenfilename(title="Locate your rpcs3.exe in your rpcs3 installation folder",filetypes=[("exe", "*.exe")])
    newFilePath = oldFilePath.replace("/rpcs3.exe", "")
    if oldFilePath != newFilePath:
        return newFilePath
    else:
        print(f"ERROR You didn't select rpcs3.exe. Please select the right file")
        return None

def main():
    configPath = getRPCS3ConfigPath()
    configEditor = ConfigEditor(configPath)
    configEditor.editConfigs()
    print("-----------------------------------------------------------------------------------------------------------------")
    ebootManager = EbootManager(configPath)
    ebootManager.replaceEboots()
    print("-----------------------------------------------------------------------------------------------------------------")
    print("Config files have been edited/created, you can now exit the program and proceed with the next instructions!")
    input()

if __name__ == '__main__':
    main()
