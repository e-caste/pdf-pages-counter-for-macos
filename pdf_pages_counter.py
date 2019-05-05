#!/usr/bin/env python3

# IMPORTANT: PATH MUST BE GIVEN BETWEEN SINGLE QUOTES '/path/to/folder/'
# OTHERWISE \ BACKSLASHES GET ESCAPED AND IF THE PATH CONTAINS SPACES IT WON'T WORK

# IMPORTANT: mdls is a macOS specific utility

import subprocess as sp
import sys

usage = "Usage: ./pdf_pages_counter.py '/path/to/folder' - path must be given between single quotes"

if len(sys.argv[1:]) != 1:
    print(usage)
    exit(-1)

path = sys.argv[1] + "/*.pdf"
# print(path)
sum = 0

cmd = "mdls -name kMDItemFSName -name kMDItemNumberOfPages " + path + " | cut -d= -f 2 | paste - - | cut -f 2"
with sp.Popen(cmd, shell=True, stdout=sp.PIPE, stderr=sp.STDOUT) as p:
    out = p.communicate()[0].decode("ascii")
    try:
        for line in out.splitlines():
            sum += int(line)
        print("The total number of pages of all PDFs in the given directory is " + str(sum))
    except ValueError:
        print(usage)
