#!/usr/bin/python

import subprocess, os, sys, shlex

(read_pipe, write_pipe) = os.pipe()

cmd = 'bash ./test.sh {0} {1}'.format(read_pipe, write_pipe)

proc= subprocess.Popen(shlex.split(cmd), stderr=subprocess.PIPE, stdout=subprocess.PIPE)
os.write(write_pipe, "hi there\n")
out, err = proc.communicate()

readback=os.read(read_pipe, 99999)

print("script read_pipe = {0}".format(readback))
print("script stdout    = {0}".format(out))
print("script stderr    = {0}".format(err))



