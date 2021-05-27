#Libraries needed
import os, sys
#can't use "~"
#Changes the current directory
os.chdir("/home/ad/Desktop/")

#os.getcwd returns the value of the current directory
print("Working in: %s" % os.getcwd() )

#os.open opens the directory inside of the current directory
fd = os.open("ArchivosUniversidad", os.O_RDONLY )
#This method is used to change the current working directory to the direcotry
#represented by the given file descriptor.
os.fchdir(fd)

print("working in: %s" % os.getcwd() )

#is used to close the given file descriptor, so that it no longer refers to any file
#or other resource and may be reused.
os.close(fd)
