import subprocess
import re
import time

ADB = r"C:\scrcpy-win64-v3.3.1\adb.exe"
SCRCPY = r"C:\scrcpy-win64-v3.3.1\scrcpy.exe"

def run_adb(*args):
    return subprocess.run([ADB, *args], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

def try_scrcpy_wireless(ip=None):
    if not ip:
        result = run_adb("devices")
        for line in result.stdout.splitlines():
            if ":5555" in line and "device" in line:
                ip = line.split(":")[0]
                break
    if not ip:
        return False

    print(f"🌐 Trying scrcpy with {ip}...")
    result = subprocess.run([
        SCRCPY,
        "--video-bit-rate", "16M",
        "--max-fps", "60",
        "--stay-awake",
        "--turn-screen-off",
        "--always-on-top",
        "--no-audio",
        "--video-encoder", "OMX.qcom.video.encoder.avc",
        f"--tcpip={ip}"
    ])
    return result.returncode == 0

# 🔍 Try wireless scrcpy first
print("🔍 Checking if wireless scrcpy is already available...")

if try_scrcpy_wireless():
    print("✅ Wireless scrcpy succeeded.")
else:
    print("📴 Wireless scrcpy failed or not available.")
    
    # 🚫 Disconnect all devices to reset state
    print("🔌 Resetting ADB state (disconnecting all)...")
    run_adb("disconnect")
    time.sleep(1)

    input("🔌 Please connect your phone via USB and press Enter to continue...")

    # ♻️ Force reinit over USB
    print("🔄 Reinitializing ADB in USB mode...")
    run_adb("usb")
    time.sleep(1)

    # 🔁 Enable TCP/IP
    print("📡 Enabling ADB TCP/IP mode...")
    run_adb("tcpip", "5555")
    time.sleep(1)

    # 🌐 Get IP address
    print("🌐 Getting phone IP address...")
    route = run_adb("shell", "ip", "route")
    match = re.search(r"src (\d+\.\d+\.\d+\.\d+)", route.stdout)

    if not match:
        print("❌ Failed to detect IP from USB. Make sure device is connected.")
        print("📄 Output:", route.stdout)
        exit(1)

    ip = match.group(1)
    print(f"✅ Phone IP detected: {ip}")

    # 🔗 Connect wirelessly
    print(f"🔗 Connecting to {ip}:5555...")
    run_adb("connect", f"{ip}:5555")
    time.sleep(1)

    # 🚀 Launch scrcpy wirelessly
    print("🚀 Launching scrcpy wirelessly...")
    try_scrcpy_wireless(ip)
