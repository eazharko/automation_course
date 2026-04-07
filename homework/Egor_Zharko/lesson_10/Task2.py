def decorator(func):
    def wrapper(*args, count=5, **kwargs):
        for x in range(count):
            func(*args, **kwargs)
    return wrapper

@decorator
def function_1(text):
    print(text)

function_1("Printing... :", count=15)
