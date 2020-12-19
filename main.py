import random

questions = []
score = 0

file = open("questions.txt", 'r')

for line in file:
    line = line.rstrip()
    questions.append(line)

for q in questions:
    i = q.split(",")

    print(i[0])
    print("Please enter your answer")
    answer = input(" : ")

    if answer.lower() == i[1].lower():
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")

print("")
print("")
print(f"Done! Your score was {score}")
