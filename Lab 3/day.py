num = 0
while True:
    num = int(input("Enter a number between 1 and 7: "))
    if 1 <= num <= 7:
        break
    else:
        continue

days = {1: "Sunday", 2: "Monday", 3: "Tuesday", 4: "Wednesday", 5: "Thursday", 6: "Friday", 7: "Saturday"}

print("The day is", days[num])