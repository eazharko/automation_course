def decorator(func):
    def wrapper(*args, count=5, **kwargs):
        for x in range(count):
            func(*args, **kwargs)
    return wrapper

@decorator
def function_1(text="Printing... :",):
    print(text)

function_1(count=5)
function_1(text="Being printed...:", count=10)
