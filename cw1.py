

Array = input("podaj liczby oddzielone przecinkiem: ")
stringArray = Array.split(",")
numbersArray = [];
for i in range(0, len(stringArray)):
    numbersArray.append(int(stringArray[i]))

max = numbersArray[0]
min = numbersArray[0]
for i in range(0, len(numbersArray)):
    if(numbersArray[i]>max):
        max = numbersArray[i]
    if(numbersArray[i]<min):
        min = numbersArray[i]

print("max: "+ str(max))
print("min: "+str(min))