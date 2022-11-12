#improve the way you print things
# make appealing
#fix exceptions

while True:
    vNumber=input("We will need your vehicle number if you are going to park here. Please enter your 5 digit vehicle: ")
    if not ( len(vNumber)==5 and vNumber.isnumeric() ):
        print("Your vehicle number is not 5 digits")
    else:
        break
    
while True:
    entry=(input("what is your entry time. example 9.30: "))
    if not("." in entry):
        print("please write time in a 24 hour format with a dot.")
    else:
        entry=float(entry)
        break
duration=float(input("how long would you like to park here. Every hour is 3$. example of how to write the time 2.00. We use 24 hour time: "))

bill=duration*3
print("any extra time you stay is 6$ a hour")
while True:
    checkIn=int(input("what is your vehicle number"))
    if(checkIn==vNumber):
        checkTime=float(input("What is the current time: "))
        
        if (checkTime-entry == duration):
            print("Your total bill for parking is", bill)
            break
        if(checkTime-duration>entry):
            actualDuration = checkTime-entry
            bill = duration * 3
            extraBill = ( actualDuration - duration ) * 6
            print("Your bill is ",bill ,"Your extra bill for staying longer is", extraBill)
    else:
            print("wrong number try again")
