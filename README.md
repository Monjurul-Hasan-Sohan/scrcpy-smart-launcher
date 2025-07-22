# scrcpy Smart Launcher

A flexible launcher for [scrcpy](https://github.com/Genymobile/scrcpy) that allows the user to choose between **wireless** and **USB** mirroring using ADB. This project includes:

- ✅ A Python script (`import_subprocess.py`) that prompts user to select Wi-Fi or USB mode
- ✅ A batch file (`scrcpy_launcher.bat`) that launches the script
- ✅ An optional `.ico` file for a custom desktop shortcut

---

## 📦 Requirements

- Windows 10/11
- [scrcpy](https://github.com/Genymobile/scrcpy) (installed and extracted)
- Python 3.8+
- ADB must be in the `scrcpy` folder or added to your system PATH

---

## 🚀 Usage

### 1. Clone the repository:

```bash
git clone https://github.com/yourusername/scrcpy-smart-launcher.git
cd scrcpy-smart-launcher
```

### 2. Run the launcher

You can either:

- Double-click `scrcpy_launcher.bat`

**OR**

- Run manually in terminal:

```bash
python import_subprocess.py
```

---

## 🖼️ Optional: Create Desktop Shortcut with Icon

1. Right-click `scrcpy_launcher.bat` → Send to → Desktop (create shortcut)
2. Right-click the desktop shortcut → Properties → Change Icon
3. Browse to `scrcpy.ico` (included in this repo)
4. Click OK → Apply

---

## 🧠 How It Works

- If you select **Wi-Fi**, the script will:
  - Try connecting to existing wireless ADB
  - If not available, prompt you to connect via USB, then switch to TCP/IP and reconnect wirelessly

- If you select **USB**, the script will:
  - Disconnect wireless ADB if active
  - Reconnect using direct USB and launch scrcpy

---

## 📂 Files Included

| File                   | Description                                 |
|------------------------|---------------------------------------------|
| `import_subprocess.py` | Main Python launcher                        |
| `scrcpy_launcher.bat`  | Batch file to run the script from Windows   |
| `scrcpy.ico`           | (Optional) Custom icon for desktop shortcut |
| `README.md`            | You're reading it!                          |

---

## 🧑‍💻 Author

Maintained by [Your Name](https://github.com/yourusername)

Feel free to contribute or fork the project!
