def allcaps(func):
    def wrapper():
        function = func()
        uppercase = function.upper()
        return uppercase
    return wrapper