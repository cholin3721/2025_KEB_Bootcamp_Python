def log_decorator(func) :
    def wrapper(*args, **kwargs) :
        print(f'Function Name : {func.__name__}')
        print(f'Function Argument = {args}')
        print(f'Function Keyword Arguments = {kwargs}')
        result = func(*args, **kwargs)
        return result
    return wrapper

@log_decorator
def greet(name, greeting = '안녕하세요', age = None) :
    return f"{greeting}, {name}, {age}" if age else f"{greeting}, {name}"

print(greet("인하"))
print()
print(greet("인상", "안녕"))
print()
print(greet("James", "Hello"))
print()
print(greet("Gonzales",  greeting ="hola"))
print()
print(greet("Nakamura",  "gonniziwa", age=29))
print()
