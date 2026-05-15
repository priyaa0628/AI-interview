import ollama


def generate_aptitude_questions(category="Quantitative Aptitude"):
    """
    Generate aptitude MCQ questions using LLaMA/Ollama
    """

    prompt = f"""
Generate exactly 5 beginner-friendly aptitude MCQ questions from this category:
{category}

CATEGORIES:
- Quantitative Aptitude
- Logical Reasoning
- Verbal Ability

STRICT RULES:
1. Start every question with Question:
2. Give exactly 4 options:
A.
B.
C.
D.
3. Add Correct Answer:
4. No explanations
5. No numbering

EXACT FORMAT:

Question: What is 20% of 500?
A. 50
B. 100
C. 150
D. 200
Correct Answer: B. 100
"""

    result = ollama.generate(
        model="llama3",
        prompt=prompt
    )

    output = result["response"]

    lines = output.split("\n")

    questions = []
    current_question = {}
    options = []

    for line in lines:

        line = line.strip()

        if line.startswith("Question:"):

            if current_question and len(options) == 4:
                current_question["options"] = options
                questions.append(current_question)

            current_question = {
                "question": line.replace("Question:", "").strip()
            }

            options = []

        elif line.startswith(("A.", "B.", "C.", "D.")):
            options.append(line)

        elif line.startswith("Correct Answer:"):
            current_question["correct_answer"] = line.replace(
                "Correct Answer:",
                ""
            ).strip()

    if current_question and len(options) == 4:
        current_question["options"] = options
        questions.append(current_question)

    return questions