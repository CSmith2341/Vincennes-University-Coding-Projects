
#valid credentials for logging in
user = "Monty"
pw = "Python"


#the function we'll call back to to see if the input was valid
def askUser():
    username = input("Enter your username: ") 
    password = input("Enter your password: ")

    return username, password

#checking to see if the inputs match the valid login info
def checkPass():
    
    username, password = askUser() #calling back to the askUser() function

    if username == user and password == pw:
        print(f"Welcome {username}!")
        return True
    else:
        print("Your username and/or password was incorrect.")
        print()
        askUser() #if they entered the incorrect creds, this will ask them to login again
        
        
        

   
#our little menu if they login successfully
def getCommand():
    
    #asking which option they want
    cmd = input("Please enter one of the following commands: 'quit', 'log off', or 'messageMe' ")

    if cmd == 'quit':
        print("You have quit")
        exit()

    elif cmd == 'log off':
        print("You have logged off")
        exit()

    elif cmd == 'messageMe':
        print("Hello how are you?")
        getCommand() #if they choose this option, it'll let them put in another command after the message
        
    else:
        print("Unkown command")
        getCommand() #let's them try to enter a correct command

#our 2 call functions from earlier that will only work if the user/pw were entered correctly
checkPass() #when the correct creds are entered, this will terminate the checkPass() function and open the getCommand() function
getCommand()


