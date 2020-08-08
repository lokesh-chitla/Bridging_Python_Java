#!/usr/bin/python

import subprocess

p = subprocess.Popen(["java", "MyWriteClass"], stdout=subprocess.PIPE)
line = p.stdout.readline()
while(line != "Yes\n"):
        print line
        line = p.stdout.readline()
