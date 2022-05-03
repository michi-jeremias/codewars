import unittest
from codewars_ranking import User


class TestUser(unittest.TestCase):
    def test_init(self):
        user = User()
        self.assertEqual(user.rank, -8)
        self.assertEqual(user.progress, 0)

    def test_inc_progress(self):
        user = User()
        user.inc_progress(-7)
        self.assertEqual(user.progress, 10)

        user = User()
        user.inc_progress(-8)
        self.assertEqual(user.progress, 3)

        user = User()
        user.inc_progress(-8)
        user.inc_progress(-8)
        self.assertEqual(user.progress, 6)

        user = User()
        user.inc_progress(-6)
        self.assertEqual(user.progress, 40)

        user = User()
        user.inc_progress(-5)
        self.assertEqual(user.progress, 90)

    def test_inc_progress_to_new_rank(self):
        user = User()
        user.inc_progress(-4)
        self.assertEqual(user.rank, -7)
        self.assertEqual(user.progress, 60)

    def test_next_rank_one(self):
        user = User()
        user.rank = -1
        user.progress = 99
        user.inc_progress(-1)
        self.assertEqual(user.rank, 1)

    def test_progress_into_rank_eight(self):
        user = User()
        user.rank = 7
        user.progress = 99
        user.inc_progress(8)
        self.assertEqual(user.progress, 0)
        self.assertEqual(user.rank, 8)

    def test_rank_eight(self):
        user = User()
        user.rank = 8
        user.inc_progress(8)
        self.assertEqual(user.progress, 0)
        self.assertEqual(user.rank, 8)

    def test_progress_two_ranks(self):
        user = User()
        user.rank = -8
        user.inc_progress(-3)
        self.assertEqual(user.progress, 50)
        self.assertEqual(user.rank, -6)
