questions = [
    {
        "question": "1. What is the capital of India?",
        "options": ["A. Delhi", "B. Mumbai", "C. Chennai", "D. Kolkata"],
        "answer": "A"
    },
    {
        "question": "2. Which language is used for AI and ML?",
        "options": ["A. HTML", "B. Python", "C. CSS", "D. SQL"],
        "answer": "B"
    },
    {
        "question": "3. What is 10 + 20?",
        "options": ["A. 20", "B. 25", "C. 30", "D. 40"],
        "answer": "C"
    },
    {
        "question": "4. Which planet is known as the Red Planet?",
        "options": ["A. Earth", "B. Venus", "C. Mars", "D. Jupiter"],
        "answer": "C"
    },
    {
        "question": "5. Which is the largest ocean?",
        "options": ["A. Indian", "B. Pacific", "C. Atlantic", "D. Arctic"],
        "answer": "B"
    },
    {
        "question": "6. Which keyword is used to create a function in Python?",
        "options": ["A. function", "B. def", "C. fun", "D. define"],
        "answer": "B"
    },
    {
        "question": "7. Which symbol is used for comments in Python?",
        "options": ["A. //", "B. /*", "C. #", "D. --"],
        "answer": "C"
    },
    {
        "question": "8. How many days are there in a leap year?",
        "options": ["A. 364", "B. 365", "C. 366", "D. 367"],
        "answer": "C"
    },
    {
        "question": "9. Which data type stores True or False?",
        "options": ["A. int", "B. float", "C. bool", "D. string"],
        "answer": "C"
    },
    {
        "question": "10. Which loop is used to repeat a block of code?",
        "options": ["A. if", "B. while", "C. else", "D. break"],
        "answer": "B"
    }
]

correct = 0
wrong = 0

def start_quiz():
    global correct, wrong

    for q in questions:
        print("\n" + q["question"])

        for option in q["options"]:
            print(option)

        answer = input("Enter your answer (A/B/C/D): ").upper()

        if answer == q["answer"]:
            print("Correct!")
            correct = correct + 1
        else:
            print("Wrong!")
            print("Correct Answer:", q["answer"])
            wrong = wrong + 1

start_quiz()

total = len(questions)
percentage = (correct / total) * 100

if percentage >= 50:
    result = "Pass"
else:
    result = "Fail"

print("\n===== RESULT =====")
print("Total Questions :", total)
print("Correct Answers :", correct)
print("Wrong Answers :", wrong)
print("Percentage :", percentage)
print("Result :", result)