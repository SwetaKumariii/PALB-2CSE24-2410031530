def min_add_to_make_valid(s):
    balance = 0
    additions = 0

    for ch in s:
        if ch == '(':
            balance += 1
        else:
            if balance > 0:
                balance -= 1
            else:
                additions += 1

    return additions + balance


print(min_add_to_make_valid("(()("))
print(min_add_to_make_valid(")))"))
print(min_add_to_make_valid(")()()"))
