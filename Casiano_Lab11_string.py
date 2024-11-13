animals = []
count = 0
matching = []

print("What are the animals can be found in the Philippines?")

while count < 10:
    animal = input(f"Enter the animal {count + 1}: ")
    animals.append(animal)
    count += 1

num = int(input("Enter a number of letters should be filtered out: "))

for animal in animals:
    if len(animal) == num:
        matching.append(animal)

if matching:
    print("Animals with", num , "letters:", ", ".join (matching))
else:
    print("No matched result")