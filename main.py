import time
from menu import *
#from parkingLot import *
import parkingLot as parkingLot

if __name__ == "__main__":
    menu1()
    inputOption = input()
    if inputOption == "1":
        f =open("input.txt","r")
    
    """
        Counter = 0 
  
    #  Reading from input file 
        Content = f.readline() 
        CoList = Content.split("\n") 
  
         for line in Content: 
             if line: 
                 Counter += 1
             else:
                 continue
         print(Counter)
        """
        for i in range(16):
            time.sleep(1)
            lines = f.readline()
            if f.readline == None:
                break
            print (lines)
            
        #print(Counter)
        f.close()
        print("Output for the above inputs are : ")
        print()
        f = open("output.txt","r")
        time.sleep(1)
    
    '''
        Counter1 = 0
  
     # Reading from file 
         Contents = f.readline() 
         #CoList = Content.split("\n") 
  
         for line in Contents: 
             if line: 
                 Counter1 += 1
             else:
                 continue
    '''
    
        for lines in range(20):
            time.sleep(1) 
            linesOfOutputFile =f.readline()
            if f.readline == None:
                break
            print(linesOfOutputFile) 

        f.close()
        
    elif inputOption == "2" :
        size = int(input("What is the size of your parking Space? "))
        parking_place = parkingLot.parkingSpace(size)  
        
        menu2()
        while True:
            
            Options = input()

            if Options == "1":
                regNo = input("Please Enter the registration number: ")
                color = input("What is the color of your car? ")
                parking_place.parkCar(regNo,color)
            

            elif Options == "2":
                regNo = input("Please Enter the registration number: ")
                
                print(f"Your car with regNo - {regNo} is exited from slot no. {parking_place.exit(regNo)}")

            elif Options == "3":
                regNo = input("Please Enter the registration number of your car: ")
                parking_place.slotOfCarByRegNo(regNo)

        
            elif Options == "4":
                color = input("Please type the color of the car: ").lower()
                parking_place.slotsOfCarsByColor(color)

            elif Options.lower() == "quit" or Options.lower() == "exit":
                break

            else:
                print("Please select a valid option")
    