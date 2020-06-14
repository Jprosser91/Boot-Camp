 ## Copying Student Exercises

# So far you've used a few different Python modules, but for the rest of the homework, you will need to familiarize yourself with a new one. 
# The `shutil` module is a Python module used for high-level file operations like moving and copying. Read [this beforehand]
# (https://www.journaldev.com/20536/python-shutil-module) to get familiar with `shutil` and make sure to use the [documentation]
# (https://docs.python.org/3.5/library/shutil.html#module-shutil) while you're working through the homework. 

# In the file called `copy_activities.py` with a function called `stu_activities` that does the following:

# * Finds files in `~/Downloads` that contain the string `readme`
# * Copies these files into the current working directory

# **Note**: This isn't just a challenge to complete for the sake of it, this is a practical script you can run to move any downloaded files from class
#  into your class notes directories, screenshots into a folder, or whatever you'd like it to be. You can alter the script after submitting your 
#  homework to make it work for whatever you'd like it to.

 #Import os and shutil
import os, shutil

#Create the Function stu_activities
def stu_activities(fileName):
    
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
        if f.__contains__ ("_"+ fileName):
            #Set f = to the source plus f using the os.path.join command
            f = os.path.join(source, f)
            #Nested print statement to test code
            # print (f)
            #use the shutil copy command to copy the file over to the destination variable
            shutil.copy(f, destination)
            #nested return f to test code
            # return f

#MAIN CODE---------
#exucute stu_activities with the parameter "README"
stu_activities("README")
#Nested print statement to test code
# print (fileName)