import unittest
import random
import sorting

class TestSort(unittest.TestCase):

    random_list = [ random.randrange(1, 30) for ind in range(1, 20) ]

    def test_sorting_algorithm(self):
        self.assertEquals(sorting.merge_sort(self.random_list),sorted(self.random_list))

    def test_encode_tree(self):
        pass
