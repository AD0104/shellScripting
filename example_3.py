#Gives the flexibility to suppres the output of shell commands or chain inputs
#and outputs of various commands together.
import subprocess

"""
    subprocess.run() requires a list of string as input instead of a single string.
    The first item of the list is the name of the command. The remaining items of the
    list are the flags and the arguments of the command.
"""
list_files =subprocess.run(["ls", "-l"])
print("The exit code was: %d" % list_files.returncode)

create_file = subprocess.run(["touch", "hello.py"])
print("The exit code was: %d" % create_file.returncode) 
