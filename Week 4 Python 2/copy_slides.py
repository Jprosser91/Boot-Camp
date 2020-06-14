## Copy Class Slides

# In the file called `copy_slides.py` with a function called `pptx_copy`
# Students will create a script that does the following:

# * Finds files in `~/Downloads` with the file extension `.pptx` or `.ppt`
# * Copies these files into the current working directory

# **Note**: This is another practical script you can use to move downloaded slides from class into your class notes directories.

#Import the os and shutil modules
import os, shutil

def pptx_copy(fileType):
#Setting the variable source equal to the Downloads floder using the expand user function
    source = os.path.expanduser("~/Downloads")
    #Setting the variable destination equal to the current working directory (which is November 23 for this homework example )
    destination = os.getcwd()
    
    #Nested print statements to test code
    # print (source)
    # print (destination)

    #Setting the variable files equal to the source variable using the listdir function
    files = os.listdir(source)
    
    #Nested end variable set to the destination variable to test code with more print statements
    # end = os.listdir(destination)
    # print (files)
    # print (end)

    #While f is in files    
    for f in files:
        #If f contains the string called in the main code
        if f.endswith(fileType) or f.endswith(fileType + "x"):
            #Set f = to the source plus f using the os.path.join command
            f = os.path.join(source, f)
            #Nested print statement to test code
            # print (f)
            #use the shutil copy command to copy the file over to the destination variable
            shutil.copy(f, destination)
            #nested return f to test code
            # return f

pptx_copy(".ppt")