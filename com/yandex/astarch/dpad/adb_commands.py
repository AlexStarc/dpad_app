import os

import usb1
from adb_shell.adb_device import AdbDeviceUsb
from pathlib import Path
from adb_shell.auth.sign_pythonrsa import PythonRSASigner


def execute_eventkey_command(signer, key):
    device = AdbDeviceUsb()
    device.connect(rsa_keys=[signer], auth_timeout_s=1)
    device.shell('input keyevent ' + str(key))
    device.close()


def send_adb_keyevent(key):
    home = str(Path.home())
    # Load the public and private keys
    adbkey = home + '/.android/adbkey'
    with open(adbkey) as f:
        priv = f.read()
    with open(adbkey + '.pub') as f:
        pub = f.read()
    signer = PythonRSASigner(pub, priv)

    try:
        execute_eventkey_command(signer, key)
    except usb1.USBError:
        os.system("adb kill-server")
        execute_eventkey_command(signer, key)

    print("Pressed key " + str(key))
