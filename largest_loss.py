from unittest import TestCase


def get_largest_loss(prices_list):
    min_value = prices_list[0]
    max_distance = 0
    for i in range(len(prices_list)):
        if prices_list[i] < min_value:
            min_value = prices_list[i]
        elif prices_list[i] - min_value > max_distance:
            max_distance = prices_list[i] - min_value
    return max_distance


class TestLargestPossibleLoss(TestCase):
    def test_largest_loss(self):
        data = [10, 20, 50, 60, 100]
        self.assertEqual(get_largest_loss(data), 90)
