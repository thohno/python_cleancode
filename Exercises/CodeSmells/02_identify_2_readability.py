# Identify the 2 code smells from the following list:
# Long methods
# Bad & redundant comments
# Bad variable/method naming
# Too many function arguments
# Conditional complexity
# Deeply nested control flow
# Cyclomatic complexity
# Temporary fields
# Side effects

def calculate(mylist, n):
    # calculate this
    r = 0
    i = 0
    while i < n:
        if mylist[i] % 2 == 0:
            r += mylist[i]
        i += 1

    # previous implementation: do not use anymore!
    # while i < n:
    #     if mylist[i] % 2 == 0 and mylist[i] == 0:
    #         print('This is 0')
    #         return

    return r


if __name__ == '__main__':
    pass