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


def universalTools(filename):
    print("[*]Running Binwalk")
    binwalkCommand = "binwalk -e " + filename
    system.os(filename)
main()