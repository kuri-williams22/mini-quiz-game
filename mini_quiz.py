# python mini quiz game

print("Welcome to the Video Game mini quiz!")
# questions stored in tuple
questions = ("Which iconic Nintendo player is known for trying to rescue a princess?: ",
             "Who is the main character of the newly adapted HBO show 'The Last of Us'?: ",
             "What animal is Tom Nook from Animal Crossing?: ",
             "What is the name of Link's horse from The Legend of Zelda series?: ")
             

# options stored as different elements in the tuple
options = (("a. Luigi", "b. Bowser", "c. Mario", "d. Ted"),
           ("a. Joel", "b. Andrew", "c. Tess", "d. Bob"), 
           ("a. Rabbit", "b. Tanuki", "c. Dog", "d. Eagle"), 
           ("a. Midna", "b. Zelda", "c. Aryll", "d. Epona"))

# correct answers to each question stored in tuple
answers = ("c", "a", "b", "d")

#  create a list for the guesses
guesses = []
score = 0
questions_num = 0

# iterate through each question and print
for question in questions:
    print("--------------------------------------------")
    print(question)
    
    # iterate through each option
    for option in options[questions_num]:
        print(option)

    # user input will automatically change to lowercase
    guess = input("Enter your choice (a, b, c, d): ").lower()
    # the user's guess will be appenced to the guesses list
    guesses.append(guess)
    # if user's guess matches answers tuple -> print correct and +1 to score
    if guess == answers[questions_num]:
        score += 1
        print("Correct!")
    # else print incorrect and continue
    else:
        print("Incorrect!")

    # increment question number
    questions_num += 1

# quiz complete and print user's score in percentage
print("-------------------------------------------")
print("Quiz completed!")
score = int(score / len(questions) * 100)
print(f"Score: {score}%")
print("-------------------------------------------")
