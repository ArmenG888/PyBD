import os
import sys
import winreg

def add_to_registry(key_name, script_path):
    try:
        # Open the registry key
        key = winreg.HKEY_CURRENT_USER
        sub_key = r"Software\Microsoft\Windows\CurrentVersion\Run"
        with winreg.OpenKey(key, sub_key, 0, winreg.KEY_WRITE) as registry_key:
            # Add the entry
            winreg.SetValueEx(registry_key, key_name, 0, winreg.REG_SZ, script_path)
        print(f"Added '{key_name}' to the Windows Registry startup.")
    except Exception as e:
        print(f"Error adding to the Windows Registry: {e}")

if __name__ == "__main__":
    script_path = os.path.abspath(sys.argv[0])
    key_name = "MyPythonApp"  # Change this to a suitable name for your application
    add_to_registry(key_name, script_path)