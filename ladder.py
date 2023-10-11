
def my_steps(n: int):
    if n < 1 or n > 25
        raise ValueError("Interger n should be between 1 and 25")

    
    if n == 1:
        return 1
    elif n == 2:
        return 2
        
    return my_steps(n-1) + my_steps(n-2)
