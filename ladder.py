
def my_steps(n: int):
    if n == 0 or n == 1:
        return 1
    elif n == 2:
        return 2
        
    return my_steps(n-1) + my_steps(n-2)
