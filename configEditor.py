import sys
from pathlib import Path
from tkinter.filedialog import askopenfilename
import json
import shutil

if getattr(sys, 'frozen', False):
    BASE_PATH = Path(sys.executable).parent
else:
    BASE_PATH = Path(__file__).resolve().parent

class Parser:
    def __init__(self):
        self.swapListIP_Path = BASE_PATH / "SwapList.json"
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

    def editConfig(self, config: str):
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
    
    def openfile(self):
        oldFilePath = askopenfilename(title="Locate your rpcs3.exe in your rpcs3 instalation folder",filetypes=[("exe", "*.exe")])
        newFilePath = oldFilePath.replace("/rpcs3.exe", "")
        if oldFilePath != newFilePath:
            return newFilePath
        else:
            print(f"ERROR you didnt select rpcs3.exe please select the right file")
            return None
            
def main():
    print("Locate your rpcs3.exe in your rpcs3 instalation folder")    
    parser = Parser()
    rpcs3Path = parser.openfile()

    if rpcs3Path == None:
        print("INVALID RPCS3 PATH")
        exit()
    else:

        defaultConfig = BASE_PATH / "config_default.yml"
        BLUS = Path(rpcs3Path + "/config/custom_configs/config_BLUS30464.yml")
        BLES = Path(rpcs3Path + "/config/custom_configs/config_BLES00760.yml")
        configs = [BLUS, BLES]

        for config in configs:  
            path = Path(config)
            if path.exists():
                print("-----------------------------------------------------------------------------------------------------------------")
                print(f"Editing {path}")
                parser.editConfig(config)
            else:
                try:
                    print(f"Creating {path} because it does not exist")
                    path.parent.mkdir(parents=True, exist_ok=True)
                    shutil.copy(defaultConfig, path)
                except shutil.SameFileError:
                    print("Source and destination represents the same file.")
                except PermissionError:
                    print("Permission denied.")
        print("-----------------------------------------------------------------------------------------------------------------")
        print("Config files have been edited/created, you can now exit the program and proceed with the next instructions!")
        input()

if __name__ == '__main__':
    main()