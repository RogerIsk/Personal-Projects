import os                               #lets us use the system commands
import keyboard                         #lets us use the keyboard
import time                             #allows your program to use time / example: time.sleep(2) will make the program wait for 2 seconds
import random                           #allows your program to use random / example: random.randint(1, 10) will return a random number between 1 and 10

def clear_screen():                     #function to clear the screen that we will call multiple times / this is the reason we imported the 'os module'
    os.system('clear')                  #this command clears the screen
clear_screen()                          #calling t1he function to clear the screen



print('\n''Welcome to the Dati2ng App!') #print the welcome message
time.sleep(2)                           #wait for 2 seconds
clear_screen()                          #clear the screen

#a list of partners looking for love
partners = (['Marius', 'Panton', 'Ben 10', 'Edison', 'Burg', 'Desmond', 'Rolland', 'Romeo', 'Sandy', 'Haschwald'],
            ['Himber', 'Kilimari', 'Lady Gaga', 'Mariana', 'Merry', 'Katty', 'Perry', 'Samanta', 'Clover', 'Luna'])         
female = ['woman','female','women','females', 2]                   #we give the variable different values through the usage of a list
player = ''                                                        #we give the variable 'player' the value of an empty string

while True:                                                        #a while loop that will keep running until the user inputs a valid option
    print('\nViable options in this Demo are "1. Men" and "2. Women" for simplicity.\n') #print the message
    player = input('Choose your sex:\n\n').lower()                 # Convert input to lowercase for case-insensitive comparison
    if player in ['1', 'man', 'male', 'men', 'males']:             #if the user inputs a valid option
        player = 'man'                                             #we give the variable 'player' the value  
        clear_screen()                                             #clear the screen
        print('\nYou are a', player)                               #print the message
        time.sleep(2)                                              #wait for 2 seconds
        break                                                      #break the loop
    elif player in ['2', 'woman', 'female', 'women', 'females']:   #if the user inputs a valid option
        player = 'woman'                                           #we give the variable 'player' the value
        clear_screen()                                             #clear the screen
        print('\nYou are a', player)   
        time.sleep(2)                      #print the message
        break                                                      #break the loop
    else:                                                          #if the user inputs an invalid option
        print('\n Input a valid option! \n\n')                         #print the message
        time.sleep(2)                                              #wait for 2 seconds
        clear_screen()                                             #clear the screen
    


print('\n''Choose what do you want to date:''\n')
print('1. Men              ''2. Women               ''3. Both''\n')
male = ''    
female = ''                                                      #we give the variable 'player' the value of an empty string
while True:                                                      #a while loop that will keep running until the user inputs a valid option
    male = input('\n').lower()                                   # Convert input to lowercase for case-insensitive comparison
    if male in ['1', 'man', 'male', 'men', 'males']:             #if the user inputs a valid option     
        malepartners = ', '.join(map(str, partners[0]))                #we output to the screen the first row of the list 'partners' with commas inbetween them
        print('\n These are your potential male partners:', malepartners, '\n' )         
        break                                                      #break the loop
    elif partners in ['2', 'woman', 'female', 'women', 'females']:   #if the user inputs a valid option
    
        break                                                      #break the loop
    else:                                                          #if the user inputs an invalid option
        print('Input a valid option!\n\n')                         #print the message
        time.sleep(2)                                              #wait for 2 seconds
        clear_screen()                                             #clear the screen

