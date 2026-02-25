import sys
from pathlib import Path
from tkinter.filedialog import askopenfilename
import json
import shutil

if getattr(sys, 'frozen', False):
    BASE_PATH = Path(sys.executable).parent
else:
    BASE_PATH = Path(__file__).resolve().parent

class Checker:
    def __init__(self):
        swaplist_path = BASE_PATH / "SwapList.json"
        with open(swaplist_path, "r") as f:
            data = json.load(f)

        self.swapListIP = data["swapListIP"]
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
            "  XFloat Accuracy": "  XFloat Accuracy: Approximate"
        }
    
    def getValue(self, key : str) -> str:
        if key in self.settings:
            return(self.settings[key])
        else:
            return None

class Parser:
    def editConfig(self, config: str):
        checker = Checker()
        lines = []

        with open(config, 'r') as file:   
            for line in file:
                lines.append(line.rstrip())

        for i, line in enumerate(lines):
            key = line.split(":",maxsplit=1)[0]
            value = checker.getValue(key)
            if value != None:
                lines[i] = value
                print(value)
    
        with open(config,'w') as file:
            for line in lines:
                file.write(line + "\n")
    
    def openfile(self):
        oldFilePath = askopenfilename(filetypes=[("exe", "*.exe")])
        newFilePath = oldFilePath.replace("/rpcs3.exe", "")
        if oldFilePath != newFilePath:
            return newFilePath
        else:
            print(f"ERROR you didnt select rpcs3.exe please select the right file")
            return None
    
    def checkRpcs3Path(self, path: str):
        if path == None:
            input()
            exit()

def main():
    parser = Parser()
    rpcs3Path = parser.openfile()
    parser.checkRpcs3Path(rpcs3Path)
    BLUS = Path(rpcs3Path + "/config/custom_configs/config_BLUS30464.yml")
    BLES = Path(rpcs3Path + "/config/custom_configs/config_BLES00760.yml")
    configs = [BLUS, BLES]
    BASE_DIR = Path(__file__).resolve().parent
    config_default = BASE_PATH / "config_default.yml"

    for config in configs:  
        path = Path(config)
        if path.exists():
            print(f"editing {path}")
            parser.editConfig(config)
        else:
            try:
                print(f"creating {path}")
                shutil.copy(config_default, path)
            except shutil.SameFileError:
                print("Source and destination represents the same file.")
            except PermissionError:
                print("Permission denied.")
    input()

if __name__ == '__main__':
    main()