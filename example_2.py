import os

#Home directory in linux distributions.
home_dir = os.system("cd ~")
#Code 0 means no problems, while any other number means an error.
print("'cd ~' ran with exit code %d" % home_dir)
unkown_dir = os.system("cd doesnotexist")
print("'cd doesnotexist' ran with exit code %d" % unkown_dir)
