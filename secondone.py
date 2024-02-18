def print_integers_and_sum(A, B):
    current_sum = 0
    count = 0

    for i in range(A, B + 1):
        print(i, end=" ")
        current_sum += i
        count += 1
        if count % 5 == 0:
            print()
    print("\nSum of all integers:", current_sum)

A, B = map(int, input("Enter two numbers A and B separated by space (-100<=A<B<=100): ").split())


if -100 <= A < B <= 100:
    print("Integers from A to B (5 numbers per line):")
    print_integers_and_sum(A, B)
else:
    print("Invalid input range.")
