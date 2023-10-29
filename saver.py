import os
import shutil


def create_folder(save_path: str):
    if not os.path.exists(save_path):
        os.mkdir(save_path)


def copy_saves(saves_path: str, save_path: str):
    create_folder(save_path)
    shutil.copytree(saves_path, save_path, dirs_exist_ok=True)
