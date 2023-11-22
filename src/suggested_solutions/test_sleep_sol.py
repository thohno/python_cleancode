import pytest
import testing
# TODO
# run pytest ./Exercises/Testing/test_testing.py
# run pytest -k TestTesting::test_sleep_1h

class TestTesting:
    @pytest.fixture
    def mock_sleep(mocker):
        return mocker.patch('time.sleep', return_value=None)

    def test_sleep_1h(mock_sleep):
        testing.sleep_1h()
        mock_sleep.assert_called_with(3600)