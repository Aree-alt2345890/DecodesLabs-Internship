
print("===================================")
print("     THE GENERAL KNOWLEDGE QUIZ")
print("===================================")

score = 0

# Question 1
print("\n1. What is the capital of France?")
print("a) London")
print("b) Paris")
print("c) Rome")
print("d) Berlin")

answer1 = input("Enter your answer: ")

if answer1.lower() == "b" or answer1.lower() == "paris":
    print("Correct Answer!")
    score += 1
else:
    print("Wrong Answer! Correct answer is Paris.")

# Question 2
print("\n2. Which planet is known as the Red Planet?")
print("a) Earth")
print("b) Jupiter")
print("c) Mars")
print("d) Venus")

answer2 = input("Enter your answer: ")

if answer2.lower() == "c" or answer2.lower() == "mars":
    print("Correct Answer!")
    score += 1
else:
    print("Wrong Answer! Correct answer is Mars.")

# Question 3
print("\n3. Who invented the computer?")
print("a) Charles Babbage")
print("b) Newton")
print("c) Einstein")
print("d) Tesla")

answer3 = input("Enter your answer: ")

if answer3.lower() == "a" or answer3.lower() == "charles babbage":
    print("Correct Answer!")
    score += 1
else:
    print("Wrong Answer! Correct answer is Charles Babbage.")

# Question 4
print("\n4. What is the national language of Pakistan?")
print("a) English")
print("b) Arabic")
print("c) Urdu")
print("d) Persian")

answer4 = input("Enter your answer: ")

if answer4.lower() == "c" or answer4.lower() == "urdu":
    print("Correct Answer!")
    score += 1
else:
    print("Wrong Answer! Correct answer is Urdu.")

# Question 5
print("\n5. How many continents are there in the world?")
print("a) 5")
print("b) 6")
print("c) 7")
print("d) 8")

answer5 = input("Enter your answer: ")

if answer5.lower() == "c" or answer5 == "7":
    print("Correct Answer!")
    score += 1
else:
    print("Wrong Answer! Correct answer is 7.")

# Final Score
print("\n===================================")
print("           QUIZ RESULT")
print("===================================")

print("Your Final Score is:", score, "/5")

# Performance Message
if score == 5:
    print("Excellent! Perfect Score!")
elif score >= 3:
    print("Good Job!")
else:
    print("Keep Practicing!")

print("===================================")
