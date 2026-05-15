# question_generator.py

import ollama


def generate_questions(skills):
    """
    Generate structured MCQ questions from extracted skills
    """

    # Convert skills list into text
    skills_text = ", ".join(skills)

    # Strong prompt for consistent format
    prompt = f"""
Generate exactly 20 MCQ interview questions based ONLY on these skills:
{skills_text}

STRICT RULES:
1. Start every question with Question:
2. Give exactly 4 options:
A.
B.
C.
D.
3. Add Correct Answer:
4. Do NOT use numbering like 1. or 2.
5. Do NOT add explanations.
6. Do NOT repeat questions.
7. Different from each questions.

EXACT FORMAT:

Question: What is Python?
A. Snake
B. Programming Language
C. Car
D. Game
Correct Answer: B. Programming Language
"""

    # Generate response
    result = ollama.generate(
        model="llama3.2",
        prompt=prompt
    )

    output = result["response"]

    # Split lines
    lines = output.split("\n")

    questions = []
    current_question = {}
    options = []

    # Parse line by line
    for line in lines:

        line = line.strip()

        # New question
        if line.startswith("Question:"):

            # Save previous question
            if current_question and len(options) == 4:
                current_question["options"] = options
                questions.append(current_question)

            # Start new one
            current_question = {
                "question": line.replace("Question:", "").strip()
            }

            options = []

        # Options
        elif line.startswith(("A.", "B.", "C.", "D.")):
            options.append(line)

        # Correct answer
        elif line.startswith("Correct Answer:"):
            current_question["correct_answer"] = line.replace(
                "Correct Answer:",
                ""
            ).strip()

    # Add final question
    if current_question and len(options) == 4:
        current_question["options"] = options
        questions.append(current_question)

    return questions