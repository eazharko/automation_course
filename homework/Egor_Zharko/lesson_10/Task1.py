def finisher (func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print("finished")
        return result
    return wrapper

@finisher
def to_be_decorated (x):
    print(2 + x * x)

@finisher
def to_be_decorated_text (t, named=" or do I?"):
    print("I love decorators" + t + named)

to_be_decorated(15)
to_be_decorated_text(" very much", named=" I really do!")
to_be_decorated_text(" very much")
