averge = 0
sum = 0


for i in range(0,4):
     userinput = input("Number please...")
     usernum = int(userinput)
     sum = sum + usernum

averge = sum / 4
print("The average is: " + str(averge))
