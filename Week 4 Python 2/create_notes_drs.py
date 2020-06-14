## Class Notes Folder
# In the file called `create_notes_drs.py`. In the file, define and call a function called `main` that does the following:

# * Creates a directory called `CyberSecurity-Notes` in the current working directory
# * Within the `CyberSecurity-Notes` directory, creates 24 sub-directories (sub-folders), called `Week 1`, `Week 2`, `Week 3`, 
# and so on until up through `Week 24`

# * Within each week directory, create 3 sub-directories, called `Day 1`, `Day 2`, and `Day 3`

# **Bonus Challenge**: Add a conditional statement to abort the script if the directory `CyberSecurity-Notes` already exists.

# Define a function called main
def main(directory):
    #Import the os module
    import os
    
    #Check to see if CyberSecurity-Notes exists, if it does print "The directory already exists!"
    if os.path.isdir(directory) == True:
        print ("The directory already exists!")

    #else start creating the directories and it's subdirectories
    else:
        #create CyberSecurity-Notes
        os.mkdir(directory)

        #while w is within the range of 1-25 create Week + the number w is currently equal to
        #range is 1-25 to make sure the output is Week 1-24
        for w in range(1,25):
            os.mkdir(directory + "/Week " + str(w))

            #while d is within the range of 1-4 create + the number d is currently equal to
             #range is 1-4 to make sure the output is Day 1-3
            for d in range(1,4):
                os.mkdir(directory + "/Week " + str(w) + "/Day " + str(d))

main("./CyberSecurity-Notes/")