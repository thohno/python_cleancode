from src.exercises import sleep

class TestSleep:
    def test_sleep_1h(self):
        sleep.sleep_1h(3600)
        sleep.sleep_1h.assert_called_with(3600)