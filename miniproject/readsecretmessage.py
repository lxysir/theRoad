# -*- encoding = utf-8 -*-

import os


def rename_files():
    # get all the file names in a folder
    file_list = os.listdir(r"C:\Users\frank.li\Desktop\Python\takeAbreak\prank")
    saved_path = os.getcwd()
    os.chdir(r"C:\Users\frank.li\Desktop\Python\takeAbreak\prank")
    #print(os.getcwd())
    # for each file, rename filename
    for filename in file_list:
        os.rename(filename, filename.translate(None, '0123456789'))
    #print(file_list)
    os.chdir(saved_path)
    #print(os.getcwd())

rename_files()
