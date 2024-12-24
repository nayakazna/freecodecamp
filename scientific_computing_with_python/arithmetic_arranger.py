import re

def process_input(inp: str):
    # Split the input into operands and operator
    terms = inp.split()
    
    # Input validation
    if not re.match(r'^\d{1,4} [+-] \d{1,4}$', inp):
        if not re.match(r'^[+-]$', terms[1]):
            return ("Error: Operator must be '+' or '-'.")
        elif not re.match(r'^\d+ [+-] \d+$', inp):
            return ('Error: Numbers must only contain digits.')
        # Validate the operator using regex
        elif len(terms[0]) > 4 or len(terms[2]) > 4:
            return ('Error: Numbers cannot be more than four digits.')
        return []
    
    
    # Perform the arithmetic operation
    operand1 = int(terms[0])
    operator = terms[1]
    operand2 = int(terms[2])
    
    if operator == '+':
        answer = operand1 + operand2
    else: # operator == '-'
        answer = operand1 - operand2
    
    # Return the result
    res = [operand1, operator, operand2, answer]
    return res

def format_output(problems: list, show_answers: bool) -> str:
    if problems == []:
        return ""
    # Preparation
    line1 = ""
    line2 = ""
    line3 = ""
    line4 = ""
    for problem in problems:

        operand1, operator, operand2, answer = problem
        max_len = max(len(str(operand1)), len(str(operand2)))
    
        # Format the output
        line1 += " " * (max_len + 2 - len(str(operand1))) + str(operand1)
        line2 += operator + " " * (max_len + 1 - len(str(operand2))) + str(operand2)
        line3 += "-" * (max_len + 2)
        line4 += " " * (max_len + 2 - len(str(answer))) + str(answer)

        # Spacing between problems
        if problem != problems[-1]:
            line1 += "    "
            line2 += "    "
            line3 += "    "
            line4 += "    "
        
    # Now, join them all togetherrrr
    formatted_res = line1 + "\n" + line2 + "\n" + line3
    if show_answers:
        formatted_res += "\n" + line4
    
    return formatted_res

def arithmetic_arranger(problems, show_answers=False):
    processed_problems = []
    if len(problems) > 5:
        return ('Error: Too many problems.')
    for problem in problems:
        result = process_input(problem)
        if type(result) is str:
            return result
        else:
            processed_problems.append(result)
    formatted_res = format_output(processed_problems, show_answers)
    return formatted_res


# TESTING!!!
print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))
print(); print()
print(arithmetic_arranger(["3801 - 2", "123 + 49"]))
print(); print()
print(arithmetic_arranger(["1 + 2", "1 - 9380"]))
print(); print()
print(arithmetic_arranger(["3 + 855", "3801 - 2", "45 + 43", "123 + 49"]))
print(); print()
print(arithmetic_arranger(["11 + 4", "3801 - 2999", "1 + 2", "123 + 49", "1 - 9380"]))
print(); print()
print(arithmetic_arranger(["44 + 815", "909 - 2", "45 + 43", "123 + 49", "888 + 40", "653 + 87"]))
print(); print()
print(arithmetic_arranger(["3 / 855", "3801 - 2", "45 + 43", "123 + 49"]))
print(); print()
print(arithmetic_arranger(["24 + 85215", "3801 - 2", "45 + 43", "123 + 49"]))
print(); print()
print(arithmetic_arranger(["98 + 3g5", "3801 - 2", "45 + 43", "123 + 49"]))
print(); print()
print(arithmetic_arranger(["3 + 855", "988 + 40"], True))
print(); print()
print(arithmetic_arranger(["32 - 698", "1 - 3801", "45 + 43", "123 + 49", "988 + 40"], True))

