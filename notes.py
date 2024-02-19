#!python3.12.1
"""
Bloco de notas

$ notes.py new "Minha Nota"

tag: Tech
Text: ...
Anotação geral sobre carreira de tecnologia

$ notes.py read --tag=tech
...
...
"""

__version = "0.0.1"

import os
import sys
cmds = ("read", "new")

path = os.curdir
filepatch = os.path.join(path, "notes.txt")

arguments = sys.argv[1:]
if not arguments:
    print("Invalid usage")
    sys.exit(1)

if arguments[0] not in cmds:
    print(f"Invalid command {arguments[0]}")

if arguments[0] == "read":
    for line in open(filepatch):
        title, tag, text = line.split("\t")
        if tag.lower() == arguments[1].lower():
            print(f"title: {title}")
            print(f"text: {text}")
            print("-" * 30)
            print()

if arguments[0] == "new":
    title = arguments[1]
    text = [
        f"{titulo}",
        input("tag:").strip() + "\n",
        input("text:\n").strip(),
    ]
    with open(filepatch, "a") as file_:
        file_.write("\t".join(text) + "\n")