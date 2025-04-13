"""Во всех заданиях данной подгруппы предполагается, что исходные строки, определяющие
выражения, не содержат пробелов. При выполнении заданий не следует использовать оператор
цикла. Вывести значение целочисленного выражения, заданного в виде строки S. Выражение определяется следующим образом:
<выражение> ::= <терм> | <выражение> + <терм> | <выражение> − <терм>
<терм> ::= <цифра> | <терм> * <цифра>
"""


def parse_term(s):
    digit = s[0]
    result = int(digit)
    remaining_s = s[1:]

    if not remaining_s:
        return result, ""

    if remaining_s[0] == "*":
        remaining_s = remaining_s[1:]
        next_result, next_remaining_s = parse_term(remaining_s)
        return result * next_result, next_remaining_s
    else:
        return result, remaining_s


def parse_expression(s):
    term_result, remaining_s = parse_term(s)

    result = term_result
    if not remaining_s:
        return result

    operator = remaining_s[0]

    # if operator == '+' or operator == '-':
    #    remaining_s = remaining_s[1:]
    #    next_result = parse_expression(remaining_s)

    #    if operator == '+':
    #        return result + next_result
    #    else:
    #        return result - next_result

    if not (operator == "+" or operator == "-"):
        return  # FIXME: better to throw exception here

    remaining_s = remaining_s[1:]
    next_result = parse_expression(remaining_s)
    if operator == "+":
        return result + next_result
    else:
        return result - next_result


def evaluate_expression(s):
    return parse_expression(s)


def main():
    # print(evaluate_expression(str(input('Введите строку: '))))
    expression = input("Введите строку: ")
    result = evaluate_expression(expression)
    print(result)


if __name__ == "__main__":
    main()
