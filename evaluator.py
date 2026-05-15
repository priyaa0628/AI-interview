def evaluate_answers(questions, user_answers):

    score = 0
    results = []

    # Check each answer
    for i in range(len(questions)):

        correct_answer = questions[i]["correct_answer"]

        if user_answers[i] == correct_answer:

            score += 1
            results.append(f"Q{i+1}: Correct")

        else:

            results.append(
                f"Q{i+1}: Wrong!!!           |      Your Answer: {user_answers[i]}      |         Correct Answer: {correct_answer}"
            )

    return score, results