
def my_steps(self, n: int) -> int:
    if n == 0 or n == 1:
        return 1
    return self.my_steps(n-1) + self.my_steps(n-2)
