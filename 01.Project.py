length = input("Type in the time in days")

lengthInInt = int(length)

print("The length of time in days you typed in is " + length)

years = lengthInInt // 365

lengthInInt = lengthInInt - ( years * 365)

weeks = lengthInInt // 7

lengthInInt = lengthInInt - ( weeks * 7)

days = lengthInInt


print("Number of years:" + str(years))

print("Number of years:" + str(weeks))

print("Number of years:" + str(days))