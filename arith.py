import random

def generate_integer_addition():
    problems = []
    for _ in range(6):
        num1 = random.randint(0, 99999)
        num2 = random.randint(0, 99999)
        problems.append((num1, num2, f"$$\\begin{{array}}{{r}} {num1} \\\\ + {num2} \\end{{array}}$$"))
    return problems

def generate_integer_subtraction():
    problems = []
    for _ in range(6):
        num1 = random.randint(0, 99999)
        num2 = random.randint(0, 99999)
        problems.append((num1, num2, f"$$\\begin{{array}}{{r}} {num1} \\\\ - {num2} \\end{{array}}$$"))
    return problems

def generate_integer_multiplication():
    problems = []
    for _ in range(6):
        num1 = random.randint(0, 99999)
        num2 = random.randint(1, 9)
        problems.append((num1, num2, f"{num1} * {num2}"))
    return problems

def generate_integer_4digit_multiplication():
    problems = []
    for _ in range(3):
        num1 = random.randint(0, 9999)
        num2 = random.randint(10, 99)
        problems.append((num1, num2, f"{num1} * {num2}"))
    return problems

def generate_integer_division():
    problems = []
    for _ in range(6):
        num1 = random.randint(1, 99999)
        num2 = random.randint(1, 9)
        problems.append((num1, num2, f"{num1} / {num2}"))
    return problems

def generate_mixed_problems():
    problems = []
    for _ in range(6):
        num1 = random.randint(0, 99999)
        num2 = random.randint(0, 99999)
        num3 = random.randint(1, 9)
        operation = random.choice(['+', '-', '*', '/'])
        if operation in ['+', '-']:
            problems.append((num1, num2, f"({num1} {operation} {num2})"))
        else:
            problems.append((num1, num3, f"({num1} {operation} {num3})"))
    return problems

def generate_markdown():
    addition_problems = generate_integer_addition()
    subtraction_problems = generate_integer_subtraction()
    integer_multiplication_problems = generate_integer_multiplication()
    integer_4digit_multiplication_problems = generate_integer_4digit_multiplication()
    division_problems = generate_integer_division()
    mixed_problems = generate_mixed_problems()

    markdown_content = "# Math Problems\n\n"

    markdown_content += "## Integer Addition\n"
    for i, (_, _, problem) in enumerate(addition_problems, 1):
        markdown_content += f"{i}. {problem}\n\n"

    markdown_content += "## Integer Subtraction\n"
    for i, (_, _, problem) in enumerate(subtraction_problems, 1):
        markdown_content += f"{i}. {problem}\n\n"

    markdown_content += "## Integer Multiplication\n"
    for i, (_, _, problem) in enumerate(integer_multiplication_problems, 1):
        markdown_content += f"{i}. {problem}\n\n"

    markdown_content += "## Integer Multiplication (4-digit by 2-digit)\n"
    for i, (_, _, problem) in enumerate(integer_4digit_multiplication_problems, 1):
        markdown_content += f"{i}. {problem}\n\n"

    markdown_content += "## Integer Division\n"
    for i, (_, _, problem) in enumerate(division_problems, 1):
        markdown_content += f"{i}. {problem}\n\n"

    markdown_content += "## Mixed Problems\n"
    for i, (_, _, problem) in enumerate(mixed_problems, 1):
        markdown_content += f"{i}. {problem}\n\n"

    return markdown_content

def generate_answers():
    addition_problems = generate_integer_addition()
    subtraction_problems = generate_integer_subtraction()
    integer_multiplication_problems = generate_integer_multiplication()
    integer_4digit_multiplication_problems = generate_integer_4digit_multiplication()
    division_problems = generate_integer_division()
    mixed_problems = generate_mixed_problems()

    answers_content = "# Math Problems Answers\n\n"

    answers_content += "## Integer Addition Answers\n"
    for i, (num1, num2, problem) in enumerate(addition_problems, 1):
        answers_content += f"{i}. {problem} = {num1 + num2}\n\n"

    answers_content += "## Integer Subtraction Answers\n"
    for i, (num1, num2, problem) in enumerate(subtraction_problems, 1):
        answers_content += f"{i}. {problem} = {num1 - num2}\n\n"

    answers_content += "## Integer Multiplication Answers\n"
    for i, (num1, num2, problem) in enumerate(integer_multiplication_problems, 1):
        answers_content += f"{i}. {problem} = {num1 * num2}\n\n"

    answers_content += "## Integer Multiplication (4-digit by 2-digit) Answers\n"
    for i, (num1, num2, problem) in enumerate(integer_4digit_multiplication_problems, 1):
        answers_content += f"{i}. {problem} = {num1 * num2}\n\n"

    answers_content += "## Integer Division Answers\n"
    for i, (num1, num2, problem) in enumerate(division_problems, 1):
        answers_content += f"{i}. {problem} = {round(num1 / num2, 2)}\n\n"

    answers_content += "## Mixed Problems Answers\n"
    for i, (num1, num2, problem) in enumerate(mixed_problems, 1):
        if '+' in problem:
            answers_content += f"{i}. {problem} = {num1 + num2}\n\n"
        elif '-' in problem:
            answers_content += f"{i}. {problem} = {num1 - num2}\n\n"
        elif '*' in problem:
            answers_content += f"{i}. {problem} = {num1 * num2}\n\n"
        elif '/' in problem:
            answers_content += f"{i}. {problem} = {round(num1 / num2, 2)}\n\n"

    return answers_content

if __name__ == "__main__":
    markdown_problems = generate_markdown()
    markdown_answers = generate_answers()
    
    with open("math_problems.md", "w") as file:
        file.write(markdown_problems)
        
    with open("math_problems_answers.md", "w") as file:
        file.write(markdown_answers)

    print("Markdown files 'math_problems.md' and 'math_problems_answers.md' generated successfully.")
