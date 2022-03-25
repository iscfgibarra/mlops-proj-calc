import re


def parse_input(operation: str):
    """
    Parsea una operacion y verifica que sea del tipo a (*|+|-|/) b.

    Parameters
    ----------
        operation: str :
            Es la expresion que representa una operacion

    Returns
    -------
        return:
            Ok y los elementos separados de la expresion
    """
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
    """
    Parsea un operador y lo convierte a un flotante

    Parameters
    ----------
        operator: str :
            La expresion que puede ser un operador

    Returns
    -------
        return
            Un numero flotante
    """
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


def suma(a, b):
    """
    Realiza la suma de 2 numeros

    Parameters
    ----------
        a :
            Operador a
        b :
            Operador b

    Returns
    -------
        return:
            La suma de a + b
    """
    return a + b


def multiplica(a, b):
    """
    Realiza la multiplicacion de 2 numeros

    Parameters
    ----------
        a :
            Operador a
        b :
            Operador b

    Returns
    -------
        return:
         Retorna el resultado de la mutiplicacion de a + b
    """
    return a * b
