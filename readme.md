# Overview
Hello! This is a tool designed to help with steganography tools in CTFs. There are a lot of tools to steganography, and it's tricky to remember all of them, so I figured I'd make a tool to help with this.

# How does it work?
You feed it a file, and the filetype, and it'll run relevant tools on it. For example, you cannot run ztseg on a jpg file.

# What tools does it run?
On everything? Strings, exiftool, binwalk

On PNG files? Zsteg

On JPG? Stegseek

# What tools do you still need to add?
More research needed. I'd like to add several modes of zsteg (checking for both MSB and LSB data). 
https://github.com/Pulho/sigBits

Maybe add support for audio files (WAVsteg, Sonic Visualizer), since those can be tricky, but not a lot can be done.

# What still needs to be done?
Better readme, as well as an installation guide for all of the tools, since it cannot reasonably be expected that the user has all of these tools done.