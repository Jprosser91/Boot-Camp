# Nested Dictionaries inside of a list (listed dictionaries?) 1--------------------------
# Administrator accounts list
adminList = [
    {
        "username": "DaBigBoss",
        "password": "DaBest"
    },
    {
        "username": "root",
        "password": "toor"
    }
]

# Build your login functions below
# Function 2-------------------------
# Build a function to get unsername/ password and return userInfo to the main code
def getCreds ():
    # Get the username and the password from an input
    username = input("What is your user name? ")
    password = input("what is your password? ")
    # Store that info into a variable called userInfo
    userInfo = {
        "username" : username,
        "password" : password
    }
    # Return userInfo to main code
    return userInfo

# Function 3-----------------------
# Build a function to check to see if the Login Creds match the adminlist
def checkLogin (userInfo, adminList):
    # Create a for loop that checks that adminList against the userInfo
    for info in adminList:
        # If the info is correct set logdedIn to True and return it to main code
        if info["username"] == userInfo["username"] and info["password"] == userInfo["password"]:
            loggedIn = True
            return loggedIn
        # Else set loggedIn to False and return it to the main code
    else:
            loggedIn = False
            return loggedIn

# Main Code------------------------
# Create a new variable called run for my while loop to work with
run = False
# While run is false keep looping the code
while (run == False):
    # Exectute userInfo and then loggedIn
    userInfo = getCreds()
    loggedIn = checkLogin(userInfo, adminList)
    
    #3 print statements I was using to test the functions
    # print (adminList)
    # print (userInfo)
    # print (loggedIn)

    # If loggedIn equals true then print "you have logged in!!! and set run equal to True"
    if (loggedIn == True):
        print("You have logged in!!!")
        run = True
    # Else print "--------------" and set run equal to False
    else:
        print("---------------")
        run = False

# #End code---------------------