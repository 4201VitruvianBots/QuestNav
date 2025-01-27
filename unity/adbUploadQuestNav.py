import os
from pathlib import Path

FILE_PATH = Path(__file__)
FOLDER_PATH = FILE_PATH.parent

ADB_PATH = Path(r"C:\bin\adb-platform-tools\adb.exe")

def main():
  apkPath = FOLDER_PATH / 'build/questNav_4201.apk'
  cmd = f"{ADB_PATH} install {apkPath}"

  print(f"Executing: {cmd}")
  os.system(f"{ADB_PATH} install {apkPath}")
  print("Done!")


if __name__ == '__main__':
  main()