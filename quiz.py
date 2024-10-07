questions = (
        "Which planet is known as the Red Planet?",
        "Who wrote the play 'Romeo and Juliet'?",
        "What is the capital city of Japan?",
        "What is the largest mammal in the world?",
        "Which element is represented by the symbol 'O' on the periodic table?",
        "Who painted the Mona Lisa?",
        "What is the main ingredient in guacamole?",
        "In which year did World War II end?",
        "Which is the smallest continent by land area?",
        "Which language has the most native speakers worldwide?"
)


options = (
    ("a) Mars", "b) Venus", "c) Jupiter", "d) Saturn"),
    ("a) William Shakespeare", "b) Charles Dickens", "c) Jane Austen", "d) Leo Tolstoy"),
    ("a) Beijing", "b) Seoul", "c) Tokyo", "d) Bangkok"),
    ("a) Elephant", "b) Blue Whale", "c) Giraffe", "d) Orca"),
    ("a) Gold", "b) Oxygen", "c) Osmium", "d) Ozone"),
    ("a) Pablo Picasso", "b) Vincent van Gogh", "c) Leonardo da Vinci", "d) Michelangelo"),
    ("a) Tomato", "b) Avocado", "c) Onion", "d) Cucumber"),
    ("a) 1941", "b) 1945", "c) 1939", "d) 1950"),
    ("a) Europe", "b) Antarctica", "c) Australia", "d) South America"),
    ("a) English", "b) Mandarin Chinese", "c) Hindi", "d) Spanish")
    )


answers = ("a", "a", "c", "b", "b", "c", "b", "b", "c", "b")

guesses = []
score = 0
question_num = 0

for question in questions:
    print("-------------------------")
    print(question)
    for option in options[question_num]:
        print(option) 
        
    guess = input('Enter Your option(a/b/c/d): ').lower()
    guesses += [guess]
    if guess == answers[question_num]:
        print('CORRECT!')
        score += 10
    elif guess == answers[question_num]:
        print(f'{answers[question_num]} is the correct answer!')
    else:
        print(f'You have entered the wroung input and you have been exited from the quiz.')
    question_num += 1


print("-------------------------")
print('        Results          ')
print("-------------------------")


print('Answers: ', end=' ')
for answer in answers:
    print(answer, end=" ")
print() 

print('Your Guesses: ', end=' ')
for guessed in guesses:
    print(guessed, end=" ")
print() 


#scores = int(score / len(questions) * 100)
print(f'Your score is : {score}%')