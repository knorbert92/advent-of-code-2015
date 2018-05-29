#!/usr/bin/env python3
# coding: utf-8

import os


def main():
    templateFile = ""
    newFile1 = ""
    newFile2 = ""
    
    dayNum = input("Please tell me which day is it (it is an integer between 1 and 25): ")
    while not dayNum.isdigit() and not (int(dayNum) < 1 or int(dayNum) > 25):
        print("That is an incorrect day number!")
        dayNum = input("Please tell me which day is it (it is an integer between 1 and 25): ")
    
    versionNum = input("Version number (2 or 3): ")
    while not versionNum.isdigit() and (int(versionNum) != "2" or int(versionNum) != 3):
        print("That is an incorrect version number!")
        versionNum = input("Version number (2 or 3): ")
    
    if int(versionNum) == 2:
        templateFile = "template2.py"
        newFile1 = dayNum + "_day_1_ver_2.py"
        newFile2 = dayNum + "_day_2_ver_2.py"
    elif int(versionNum) == 3:
        templateFile = "template3.py"
        newFile1 = dayNum + "_day_1_ver_3.py"
        newFile2 = dayNum + "_day_2_ver_3.py"
    else:
        print("Unexpected error happened!")

    os.system('cp ' + templateFile + ' ' + newFile1)
    os.system('cp ' + templateFile + ' ' + newFile2)


################################################################################

if __name__ == "__main__":
    main()

