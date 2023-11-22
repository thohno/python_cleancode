import pytest
from src.exercises import sleep

class TestSleep:
    @pytest.fixture
    def mock_sleep(mocker):
        return mocker.patch('time.sleep', return_value=None)

    def test_sleep_1h(mock_sleep):
        sleep.sleep_1h()
        mock_sleep.assert_called_with(3600)