import re


def parse_input(operation: str):
    reg_exp = r'(\d+.?\/?\d?)\s{0,10}(-|\+|\*|\/)\s{0,10}(\d+.?\/?\d?)'
    a = ""
    operator = ""
    b = ""

    match = re.match(reg_exp, operation)
    ok = match is not None
    if ok:
        numbers = re.findall(reg_exp, operation)
        a = numbers[0][0]
        operator = numbers[0][1]
        b = numbers[0][2]

    return ok, a, operator, b


def parse_float(operator: str):
    reg_exp = r'^(\d+)\/(\d+)'
    a = 0
    b = 0
    match = re.match(reg_exp, operator)
    if match is not None:
        numbers = re.findall(reg_exp, operator)
        a = float(numbers[0][0])
        b = float(numbers[0][1])
        return division(a, b)

    return float(operator)

def multiplica(a, b):
    return a * b
