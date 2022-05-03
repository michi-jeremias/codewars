"""
https://www.codewars.com/kata/51fda2d95d6efda45e00004e
"""


class User:
    def __init__(self):
        self.rank = -8
        self.progress = 0

    def inc_progress(self, rank):
        ranks = [-8, -7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8]
        try:
            rank_diff = ranks.index(rank) - ranks.index(self.rank)
        except ValueError as e:
            print(e)

        score_progression = {0: 3, -1: 1}
        score = 0

        if rank_diff <= 0:
            if rank_diff in score_progression.keys():
                score = score_progression[rank_diff]
        else:
            score = 10 * rank_diff * rank_diff

        self.update_user(score)

    def update_user(self, score):
        if self.rank < 8:
            self.update_progress(score)
            self.update_rank()

    def update_progress(self, score):
        self.progress += score

    def update_rank(self):
        ranks = [-8, -7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8]
        rank_progression = {
            -8: -7,
            -7: -6,
            -6: -5,
            -5: -4,
            -4: -3,
            -3: -2,
            -2: -1,
            -1: 1,
            1: 2,
            2: 3,
            3: 4,
            4: 5,
            5: 6,
            6: 7,
            7: 8,
            8: 8,
        }

        while True:
            if self.progress >= 100:
                self.progress -= 100
                self.rank = rank_progression[self.rank]
                if self.rank == 8:
                    self.progress = 0
            else:
                break

