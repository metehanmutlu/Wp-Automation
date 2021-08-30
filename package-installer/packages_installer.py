import subprocess
import sys
import json

with open("packages.json", encoding="utf-8") as file:
    packages_file = json.load(file)
    packages = packages_file['packages']


class Installer():
    def __init__(self, packages: list):
        self.packages = packages

    def install(self):
        for package in self.packages:
            subprocess.check_call(
                [sys.executable, "-m", "pip", "install", package])
        else:
            print('Packages installed!')


installer = Installer(packages=packages)
installer.install()
input('Click Enter to Close....')
