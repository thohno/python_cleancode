# Iterate with enumerate() instead of range(len())
import sys

# not cool
data = [1, 2, -4, -3]
for i in range(len(data)):
    if data[i] < 0:
        data[i] = 0

print(data)

# cool
data = [1, 2, -4, -3]
for idx, num in enumerate(data):
    if num < 0:
        data[idx] = 0

print(data)


# Use list comprehension

# not cool
squares = []
for i in range(10):
    squares.append(i * i)

print(squares)

# cool
squares = [i * i for i in range(10)]
print(squares)


# Save memory with generators

# not cool
my_list = [i for i in range(10000)]
print(sum(my_list))
print(sys.getsizeof(my_list), "bytes")

# cool
my_gen = (i for i in range(10000))
print(sum(my_gen))
print(sys.getsizeof(my_gen), "bytes")


# format string

#cool
name = "Alex"
my_string = f"Hello {name}"
print(my_string)

i = 10
print(f"{i} squared is {i*i}")


# join string

# cool
list_of_strings = ["Hello", "my", "friend"]
my_string = " ".join(list_of_strings)
print(my_string)
