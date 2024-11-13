passer = 0
numlist = []
counter = 0

for x in range(5):
    num = int(input("Enter your grade: "))

    if num <= 39 or num >= 101:
        print("Invalid grade input. Grade must be between 40 and 100. Please try again, thank you!")
        break
    else:
        numlist.append(num)

    if num >= 75:
        passer += 1
        counter += 1
    else:
        counter += 1
    
    if counter == 5:
        print()
        numsum = sum(numlist)
        aveGrade = numsum / 5
        aveGrade = round(aveGrade, 2)

        pass_percent = (passer / len(numlist)) * 100
        pass_percent = round(pass_percent, 2)

        print("Grades: " + str(numlist))
        print("Average Grade: " + str(aveGrade))
        print("Number of people who passed the subject: " + str(passer))
        print("Percentage of people who passed the subject: " + str(pass_percent))