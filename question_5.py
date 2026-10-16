# 5) Create a basic quiz game that:

# Contains a list of 5–10 questions stored in a dictionary (or list of dictionaries [{}, {}] ).
# Ask the user each question and records their answers.
# At the end, displays:
# The user’s score (e.g., 7/10)
# Correct answers for any questions they got wrong

# Quiz Questions stored in a list of dictionaries
quiz_questions = [
    {
        "question": "What is the capital of France?",
        "options": ("1. London", "2. Paris", "3. Berlin"),
        "answer": "2"
    },
    {
        "question": "Which Python keyword is used to define a function?",
        "options": ("1. func", "2. define", "3. def"),
        "answer": "3"
    },
    {
        "question": "What data type is the result of 5 > 3?",
        "options": ("1. Integer", "2. Boolean", "3. String"),
        "answer": "2"
    },
    {
        "question": "Which symbol is used for single-line comments in Python?",
        "options": ("1. //", "2. /*", "3. #"),
        "answer": "3"
    },
    {
        "question": "How do you add an item to the end of a list in Python?",
        "options": ("1. .append()", "2. .add()", "3. .insert()"),
        "answer": "1"
    }
]

def run_quiz():
    score = 0
    all_answers = []
    wrong_answers = [] 
    
    # Loop through each question
    for q in quiz_questions:
        print("\n" + q["question"])
        
        # Display options
        for option in q["options"]:
            print(option)
            
        # Get valid user answer with input validation
        valid_choices = [str(i) for i in range(1, len(q["options"]) + 1)]
        while True:
            user_answer = input(f"Enter your choice ({', '.join(valid_choices)}): ").strip()
            if user_answer in valid_choices:
                break
            print(f"Invalid input! Please enter a valid option ({', '.join(valid_choices)}).")
        
        # Record user answer details
        user_idx = int(user_answer) - 1
        user_text = q["options"][user_idx]
        correct_idx = int(q["answer"]) - 1
        correct_text = q["options"][correct_idx]
        is_correct = (user_answer == q["answer"])
        
        all_answers.append({
            "question": q["question"],
            "user_choice": user_answer,
            "user_text": user_text,
            "correct_text": correct_text,
            "is_correct": is_correct
        })
        
        # Check answer
        if is_correct:
            print("Correct! 🎉")
            score += 1
        else:
            print(f"Wrong! The correct answer was option {q['answer']}.")
            # Store the missed question in our list
            wrong_answers.append({
                "question": q["question"],
                "user_text": user_text,
                "correct_answer": q["answer"],
                "correct_text": correct_text,
                "options": q["options"]
            })
            
    # Final Score Display
    print(f"\n==============================")
    print(f"QUIZ OVER! Your score: {score}/{len(quiz_questions)}")
    print(f"==============================")
    
    # Display correct answers for any questions they got wrong
    if wrong_answers:
        print("\n--- REVIEW: QUESTIONS YOU MISSED ---")
        for item in wrong_answers:
            print(f"\nQuestion: {item['question']}")
            print(f"Your Answer:    {item['user_text']}")
            print(f"Correct Answer: {item['correct_text']}")
    else:
        print("\nAmazing job! You got a perfect score! 🌟")

# Run the quiz game
if __name__ == "__main__":
    run_quiz()