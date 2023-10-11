
def my_steps(self, n: int):
    if n == 0 or n == 1:
        return 1
    elif n == 2:
        return 2
        
    return self.my_steps(n-1) + self.my_steps(n-2)
