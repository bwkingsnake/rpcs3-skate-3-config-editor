\# RPCS3 Configuration Tool



A simple tool that automatically configures RPCS3 for playing the \*\*Skate\*\* series online.



The tool edits RPCS3's per-game configuration files, applies the required networking settings, and replaces the Skate 3 EBOOT when necessary.



\---



\# Tutorial



\## Requirements



Before using this tool, make sure you have:



\- RPCS3 installed

\- One or more of the following games installed:

&#x20; - Skate

&#x20; - Skate 2

&#x20; - Skate 3

\- RPCN configured and working inside RPCS3



\---



\## Step 1 - Download the Tool



Download the latest release and extract it anywhere on your computer.



\---



\## Step 2 - Launch the Program



Run:



```

RPCS3 Configuration Tool.exe

```



The program will ask you to locate your RPCS3 installation.



\---



\## Step 3 - Select `rpcs3.exe`



Browse to your RPCS3 folder and select:



```

rpcs3.exe

```



Example:



```

Desktop

└── RPCS3

&#x20;   └── rpcs3.exe

```



The tool automatically detects the rest of your RPCS3 installation from this location.



\---



\## Step 4 - Choose Which Game to Patch



You'll see a menu similar to:



```

\[1] Skate 1

\[2] Skate 2

\[3] Skate 3

\[4] Patch All

\[0] Exit

```



Choose the game you want to configure.



\---



\## Step 5 - Let the Tool Finish



The tool will automatically:



\- Create missing custom RPCS3 configuration files

\- Update existing configuration files

\- Apply all required networking settings

\- Patch Skate 3 EBOOT files (if applicable)



Once complete, you'll see a confirmation message.



\---



\## Step 6 - Launch RPCS3



Start RPCS3 normally and launch your game.



Your configuration is now ready for online play.



\---



\# Features



\- Automatically creates missing custom configuration files

\- Updates existing configuration files

\- Supports both US (BLUS) and European (BLES) game versions

\- Automatically patches Skate 3 EBOOT files

\- Detects both installed and disc-based games

\- Simple command-line interface

\- No manual YAML editing required



\---



\# Supported Games



| Game | BLUS | BLES |

|------|------|------|

| Skate | ✅ BLUS30059 | ✅ BLES00124 |

| Skate 2 | ✅ BLUS30253 | ✅ BLES00461 |

| Skate 3 | ✅ BLUS30464 | ✅ BLES00760 |



\---



\# What the Tool Changes



The program automatically configures the required RPCS3 networking settings, including:



\- Internet Enabled

\- IP Address

\- Bind Address

\- DNS Address

\- IP Swap List

\- UPnP

\- RPCN Status

\- PSN Country

\- XFloat Accuracy

\- SPU Loop Detection

\- Clan Settings



For Skate 3, the required EBOOT is also replaced automatically.



\---



\# Project Structure



```

RPCS3 Configuration Tool

│

├── Dependencies/

│   ├── EBOOT.BIN

│   ├── config\_BLUS30059.yml

│   ├── config\_BLES00124.yml

│   ├── config\_BLUS30253.yml

│   ├── config\_BLES00461.yml

│   ├── config\_BLUS30464.yml

│   └── config\_BLES00760.yml

│

└── RPCS3 Configuration Tool.exe

```



\---



\# How It Works



The tool:



1\. Locates your RPCS3 installation.

2\. Finds each game's custom configuration file.

3\. Creates missing configuration files from templates.

4\. Updates only the required settings.

5\. Replaces Skate 3 EBOOT files where necessary.

6\. Leaves all other configuration options untouched.



\---



\# Notes



\- Existing RPCS3 settings unrelated to online play are preserved.

\- Running the tool multiple times is safe.

\- Missing configuration files are created automatically.

\- Skate 3 EBOOTs are only replaced if they are found.



\---



\# Building From Source



Requirements:



\- Python 3.11+

\- Standard Library only



Clone the repository:



```bash

git clone https://github.com/YourUsername/RPCS3-Configuration-Tool.git

```



Run:



```bash

python main.py

```



To build an executable using PyInstaller:



```bash

pyinstaller --onefile main.py

```



\---



\# License



This project is released under the MIT License.



\---



\# Credits



Created to simplify configuring RPCS3 for online play in the Skate series without requiring users to manually edit YAML configuration files.

