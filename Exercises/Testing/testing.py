import time

def sleep_1h():
    print("Starting long-running task...")
    time.sleep(3600)  # Sleep for 1 hour
    print("Long-running task completed.")

def test_long_running_task(mock_sleep):
    sleep_1h()