import os
import argparse
import sys


def parse_args():
    parser = argparse.ArgumentParser(description="Steg Shotgun")

    parser.add_argument(
        "--filename", help="Name of the file to run tools on. Example: '--filename filename.png'"
    )

    parser.add_argument(
        "--filetype", help="Type of the file to run tools on (png or jpg). Example: `--filetype png'"
    )

    args = parser.parse_args()
    return args

#this will run tools that are generally useful on both jpg and png.

def main():
    args = parse_args()
    filename = args.filename
    fileType = args.filetype
    print("File chosen: " + filename)
    print("File type: " + fileType)
    universalTools(filename)

    if fileType == "png":
        pngTools(filename)
    else:

        jpgTools(filename)
        


def universalTools(filename):
    print("[*] Running Binwalk")
    binwalkCommand = "binwalk -e " + filename
    os.system(binwalkCommand)

    print("[*] Running exiftool, putting output into exifdata.txt")
    exiftoolCommand = "exiftool " + filename + " > exifdata.txt"
    os.system(exiftoolCommand)

    print("[*] Running strings, putting output into ImageStrings.txt")
    stringsCommand = "strings " + filename + " > ImageStrings.txt"
    os.system(stringsCommand)



def pngTools(filename):
    print("PNG detected, running PNG tools")
    print("[*] Running zsteg")
    zstegCommand = "zsteg -v -a " + filename

def jpgTools(filename):
    print("JPG detected, running JPG tools")
    print("[*] Running stegseek")
    stegseekCommand = "stegseek " + filename + " /usr/share/wordlists/rockyou.txt"
    os.system(stegseekCommand)

main()