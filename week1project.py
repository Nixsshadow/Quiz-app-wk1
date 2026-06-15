import random

#1. Questions
quiz = [
    { 
        "question": "What is the capital of France?",
        "options": ["A) Berlin", "B) Madrid", "C) Paris", "D) Rome"],
        "answer": "C"   
        },
    {
        "question": "What is the largest planet in our solar system?",
        "options": ["A) Earth", "B) Jupiter", "C) Saturn", "D) Uranus"],
        "answer": "B"
    },
    { 
        "question": "Who wrote 'To Kill a Mockingbird'?",
        "options": ["A) Harper Lee", "B) J.K. Rowling", "C) Ernest Hemingway", "D) Mark Twain"],
        "answer": "A"
    }
    { 
        "question": "What is the chemical symbol for water?",
        "options": ["A) H2O", "B) CO2", "C) O2", "D) NaCl"],
        "answer": "A"
    }
]

#2. Shuffle the quiz questions

random.shuffle(quiz)

score = 0

#3. Loop through the quiz questions
for q in quiz:
    print(q["question"])
    for option in q["options"]:
        print(option)
    
    #4. Get user input
    answer = input("Enter your answer (A, B, C, or D): ").upper()
    
    #5. Check if the answer is correct
    if answer == q["answer"]:
        print("Correct!")
        score += 1
    else:
        print(f"Wrong! The correct answer is {q['answer']}.")
    
    print()  # Print a newline for better readability

print(f"Your final score is {score}/{len(quiz)}.")

percentage = (score / len(quiz)) * 100

if percentage >= 80:
    print("Excellent work!")
elif percentage >= 50:
    print("Good job!")
else:
    print("Better luck next time!")