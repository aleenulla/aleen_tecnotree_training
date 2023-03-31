import random

# Open the file containing the questions and answers
with open("questions.txt", "r") as file:
    data = file.readlines()

# Initialize the score and shuffle the questions
score = 0
random.shuffle(data)

# Loop through each question
for line in data:
    # Split the line into the question and the answer choices
    question, *choices, answer = line.split(",")
    # Display the question and the answer choices
    print(question)
    for i, choice in enumerate(choices):
        print(f"{i + 1}. {choice}")
    # Get the user's answer
    user_answer = input("Your answer: ")
    # Check if the answer is correct
    if user_answer == answer.strip():
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")
    print()

# Display the final score
print("Your final score is:", score)
