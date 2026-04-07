def decorator(func):
    def wrapper(first, second, operation):
        if first < 0 or second < 0:
            operation = '*'
        elif first > second:
           operation = '-'
        elif second > first:
            operation = '/'
        elif first == second:
            operation = '+'
        return func(first, second, operation)
    return wrapper

@decorator
def calc(first, second, operation):
    if operation == '+':
        return first + second
    elif operation == '-':
        return first - second
    elif operation == '/':
        return first / second
    elif operation == '*':
        return first * second


print(calc(15,10, '-'))