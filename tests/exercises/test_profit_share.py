import unittest

from src.exercises.profit_share import calc_profit_share, Employer


class ProfitShareTest(unittest.TestCase):
    def test_scientist_normal(self):
        normal_scientist = Employer("Garry", 3)

        profit_share = calc_profit_share(1, normal_scientist, 10000)

        self.assertEqual(250, profit_share)

    def test_scientist_advanced(self):
        normal_scientist = Employer("Garry", 10)

        profit_share = calc_profit_share(1, normal_scientist, 10000)

        self.assertEqual(500, profit_share)

    def test_developer_advanced(self):
        advanced_developer = Employer("Garry", 8)

        profit_share = calc_profit_share(2, advanced_developer, 10000)

        self.assertEqual(1500, profit_share)

    def test_developer_expert(self):
        expert_developer = Employer("Garry", 11)

        profit_share = calc_profit_share(2, expert_developer, 10000)

        self.assertEqual(2000, profit_share)

    def test_developer_normal(self):
        normal_developer = Employer("Garry", 3)

        profit_share = calc_profit_share(2, normal_developer, 10000)

        self.assertEqual(1000, profit_share)

    def test_developer_normal_high_salary(self):
        normal_developer = Employer("Garry", 3)

        profit_share = calc_profit_share(2, normal_developer, 300000)

        self.assertEqual(15000, profit_share)

    def test_boss(self):
        boss = Employer("Garry", 30)

        profit_share = calc_profit_share(3, boss, 100000)

        self.assertEqual(20000, profit_share)

    def test_it_guy(self):
        poor_guy = Employer("Garry", 30)

        profit_share = calc_profit_share(4, poor_guy, 100000)

        self.assertEqual(0, profit_share)