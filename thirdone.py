def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def sum_odd_factorials():
    total = 0
    for i in range(1, 12, 2):  # Loop through odd numbers from 1 to 11
        total += factorial(i)
    return total

result = sum_odd_factorials()
print("The sum of factorials of odd numbers from 1 to 11 is:", result)
