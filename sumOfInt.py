def getSum():
    count = 1
    total = 0
    for i in range(5):
        while True:
            try:
                num = int(input("Enter an integer "+str(count)+": "))
                count+=1
                total += num
                break
            except ValueError:
                print("Invalid input. Please enter an int.")
    return total

result = getSum()
print("Your sum is:", result)