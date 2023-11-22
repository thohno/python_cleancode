import unittest
import pytest
import pandas as pd
import numpy as np
from src.exercises import refactoring

# run pytest ./tests/exercises/test_refactoring.py
class TestRefactoring:
    @pytest.fixture
    def data(self):
        df = pd.DataFrame({'day1': [1, 2, 3, 4, 5], 'day2': [4, 16, 36, 64, 100]})
        data = df['day2']
        return data

    def test_mean(self, data):
        output = refactoring.process_data(data, 0)
        assert output == 44.0, 'Incorrect mean'

    def test_median(self, data):
        output = refactoring.process_data(data, 1)
        assert output == 36, 'Incorrect median'

    def test_squares(self, data):
        output = refactoring.process_data(data, 2)
        assert (output == np.array([16, 256, 1296, 4096, 10000])).all(), 'Incorrect squares'

    def test_mean_squares(self, data):
        output = refactoring.process_data(data, 3)
        assert output == 3132.8, 'Incorrect mean squares'

    def test_root(self, data):
        output = refactoring.process_data(data, 4)
        assert (output == np.array([1.98, 3.98, 5.98, 7.98, 9.98])).all(), 'Incorrect root'