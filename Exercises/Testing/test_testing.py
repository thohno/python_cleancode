import pytest
import testing

# run pytest ./Exercises/Testing/test_testing.py
@pytest.fixture
def mock_sleep(mocker):
    return mocker.patch('time.sleep', return_value=None)

def test_long_running_task(mock_sleep):
    testing.sleep_1h()
    mock_sleep.assert_called_with(3600)