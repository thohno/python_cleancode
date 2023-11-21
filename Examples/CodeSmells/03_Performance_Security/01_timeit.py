from timeit import timeit
from time import sleep


def slow_function():
    sleep(0.1)


if __name__ == '__main__':
    repetitions = 20
    duration = timeit(slow_function, number=repetitions)
    print(f"Average Duration: {duration / repetitions}s")
    # Average Duration: 0.10045769704999999s
