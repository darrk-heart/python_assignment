# 1. Please write a program to read a input string from the console, and substitute the characters like the  following
# before after 
# A Z
# B Y
# C X
# D W
# … …
# X C
# Y B
# Z A

def case1():
    return "Z"

def case2():
    return "Y"

def case3():
    return "X"

def case4():
    return "W"
def case5():
    return "..."
def case6():
    return "C"
def case7():
    return "B"
def case8():
    return "A"
def default_case():
    return "wrong Input"

# defined the switch cases as a python dictionary 
switch_cases = {
    'A': case1,
    'B': case2,
    'C': case3,
    'D': case4,
    '...': case5,
    'X': case6,
    'Y': case7,
    'Z': case8
}

def switch_case(case):
    return switch_cases.get(case, default_case)()

case_input = input("Enter the case value: ")

result = switch_case(case_input)
print(result)
