def is_prime(fn):
    def wrapper(*args):
        res = fn(*args)
        a = 2
        while sum(args) % a != 0:
            a += 1
        if a == sum(args):
            print("Простое")
        else:
            print("Составное")
        return res
    return wrapper



@is_prime
def sum_three(*args):
    return sum(args)

result = sum_three(2, 3, 6)
print(result)

# Консоль
# Простое
# 11



