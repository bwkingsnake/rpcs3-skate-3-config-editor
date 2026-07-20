# RPCS3 Configuration Tool — Tutorial

A tool for automatically configuring RPCS3 for online play with the **Skate** series.

## ✅ Requirements

Before using this tool, make sure you have:

- [x] RPCS3 installed
- [x] One or more of the following games installed: `Skate` · `Skate 2` · `Skate 3`
- [x] RPCN configured and working inside RPCS3

---

## 🚀 Setup Steps

### Step 1 — Run the tool
Launch `RPCS3 Configuration Tool.exe`

### Step 2 — Locate RPCS3
The program will ask you to locate your RPCS3 installation.

### Step 3 — Select `rpcs3.exe`
Browse to your RPCS3 folder and select `rpcs3.exe`.

```
Desktop
└── RPCS3
      └── rpcs3.exe
```

> The tool automatically detects the rest of your RPCS3 installation from this location.

### Step 4 — Choose which game to patch
Select the Skate game you want to configure.

### Step 5 — Let the tool finish
The tool will automatically:

- Create missing custom RPCS3 configuration files
- Update existing configuration files
- Apply all required networking settings
- Patch Skate 3 EBOOT files *(if applicable)*

Once complete, you'll see a confirmation message.

### Step 6 — Launch RPCS3
Start RPCS3 normally and launch your game.

**Your configuration is now ready for online play.** 🎉

---

## ✨ Features

- Automatically creates missing custom configuration files
- Updates existing configuration files
- Supports both **US (BLUS)** and **European (BLES)** game versions
- Automatically patches Skate 3 EBOOT files
- Detects both installed and disc-based games

## 🎮 Supported Games

| Game | Supported |
|------|:---------:|
| Skate 1 | ✅ |
| Skate 2 | ✅ |
| Skate 3 | ✅ |

## 🌐 Networking Settings Configured

The program automatically configures the required RPCS3 networking settings, including:

- Internet Enabled
- IP Address
- Bind Address
- DNS Address
- IP Swap List
- UPnP
- RPCN Status
- PSN Country
- XFloat Accuracy
- SPU Loop Detection
- Clan Settings

> For **Skate 3**, the required EBOOT is also replaced automatically.