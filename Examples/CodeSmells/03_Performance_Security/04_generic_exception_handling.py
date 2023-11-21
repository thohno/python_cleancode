# Code smell
reply = input("Enter a number:\n")
try:
    number = int(reply)
except:
    print("No valid number given!")

# Better
reply = input("Enter a number:\n")
try:
    number = int(reply)
except Exception:
    print("No valid number given!")

# Best:
reply = input("Enter a number:\n")
try:
    number = int(reply)
except ValueError:
    print("No valid number given!")


if __name__ == '__main__':
    pass