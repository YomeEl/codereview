# Во всех заданиях данной подгруппы предполагается, что исходные строки, определяющие
# # выражения, не содержат пробелов. При выполнении заданий не следует использовать оператор
# # цикла. Вывести значение целочисленного выражения, заданного в виде строки S. Выражение определяется следующим образом:
# <выражение> ::= <терм> | <выражение> + <терм> | <выражение> − <терм>
# <терм> ::= <цифра> | <терм> * <цифра>

# Вычисляет значение целочисленного выражения, заданного в виде строки
def evaluate_expression(s):

    # Разбирает терм
    def parse_term(s):
        digit = s[0]  # Первая цифра в терме
        result = int(digit)
        remaining_s = s[1:]  # Оставшаяся часть терма

        if not remaining_s:
            return result, "" #только одна цифра

        if remaining_s[0] == '*':  # Если есть умножение пропускаем
            remaining_s = remaining_s[1:]
            next_result, next_remaining_s = parse_term(remaining_s)
            return result * next_result, next_remaining_s
        else:
            return result, remaining_s  # Если нет умножения, возвращаем результат и оставшуюся часть строки

    # Разбирает выражение
    def parse_expression(s):
        term_result, remaining_s = parse_term(s) # Разбираем первый терм

        result = term_result
        if not remaining_s:
            return result # только один терм

        operator = remaining_s[0] # Оператор после первого терма
        if operator == '+' or operator == '-':
            remaining_s = remaining_s[1:]
            next_result = parse_expression(remaining_s) # Рекурсивный вызов для оставшейся части выражения

            if operator == '+':
                return result + next_result # Вычисляем результат с учетом оператора
            else:
                return result - next_result  # Вычисляем результат с учетом оператора


    return parse_expression(s)

print(evaluate_expression(str(input('Введите строку: '))))

