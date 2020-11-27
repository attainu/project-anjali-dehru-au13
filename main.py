import time
from menu import *
#from parkingLot import *
import parkingLot as parkingLot

if __name__ == "__main__":
    menu1()
    inputOption = input()
    if inputOption == "1":
        inputFileName = input("Enter the file name for inputs: ")
        try:
            f =open(inputFileName,"r")
            while(1):
                time.sleep(1)
                lines = f.readline()
                if len(lines) == 0:
                    break
                print (lines)
            print()
            f.close()
        except:
            print("No such files exists")

        outputFileName = input("Enter the file name for ouput: ")
        try:

            print("Output for the above inputs are : ")
            print()
            f = open(outputFileName,"r")
            time.sleep(1)
        
            while(1):
                linesOfOutputFile = f.readline()
                if len(linesOfOutputFile) == 0:
                    break
                print(linesOfOutputFile) 

            f.close()
        except:
            print("No such files exists") 

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
    