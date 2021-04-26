sudo rm -rf dist
sudo rm -rf build
sudo pyinstaller src/main.py --onefile --hidden-import pygame