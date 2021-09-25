import re


def arithmetic_arranger(problems, showSolutions=False):
    operand1s = []
    operand2s = []
    operators = []
    solutions = []

    if len(problems) > 5:
        return 'Error: Too many problems.'

    for problem in problems:
        splitProblem = re.findall('(\S+)\s?([+-/*])\s?(\S+)', problem)
        operand1 = splitProblem[0][0]
        operand2 = splitProblem[0][2]
        operator = splitProblem[0][1]
        if operator != '-' and operator != '+':
            return 'Error: Operator must be \'+\' or \'-\'.'
        elif len(operand1) > 4 or len(operand2) > 4:
            return 'Error: Numbers cannot be more than four digits.'
        elif (re.search('\D', operand1) is not None) or (re.search('\D', operand2) is not None):
            return 'Error: Numbers must only contain digits.'
        else:
            widthReqd = max(len(operand2), len(operand1)) + 2
            if showSolutions:
                solutions.append(str(eval(operand1 + operator + operand2)).rjust(widthReqd, ' '))
            operand1s.append(operand1.rjust(widthReqd, ' '))
            operand2s.append(operand2.rjust(widthReqd - 1, ' '))
            operators.append(operator)

    index = 0
    dashLines = []
    while index < len(problems):
        operators[index] = operators[index] + operand2s[index]
        dashesReqd = max(len(operand2s[index]), len(operand1s[index]))
        dashLine = ''.rjust(dashesReqd, '-')
        dashLines.append(dashLine)
        index += 1

    line1 = '    '.join(operand1s)
    line2 = '    '.join(operators)
    line3 = '    '.join(dashLines)

    if showSolutions:
        line4 = '    '.join(solutions)
        arranged_problems = line1 + '\n' + line2 + '\n' + line3 + '\n' + line4
    else:
        arranged_problems = line1 + '\n' + line2 + '\n' + line3

    return arranged_problems
