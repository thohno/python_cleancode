import time

# run python ./Exercises/Testing/testing.py
def sleep_1h():
    print("Starting sleep...")
    time.sleep(3600)  # Sleep for 1 hour
    print("Sleep completed.")


if __name__ == '__main__':
    sleep_1h()

