large = 0



for i in range(0,4):
    userinput = input("Number please...")
    usernum = int(userinput)    
    if large < usernum:
        large = usernum
print("The largest number is: " + str(large ))