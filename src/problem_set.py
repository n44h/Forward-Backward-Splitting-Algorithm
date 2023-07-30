import numpy as np


class Problem:
    def __init__(self,
                 m: int,
                 n: int,
                 num_sp: int,
                 q: float = 10,
                 M: np.ndarray = None):
        # Initialize Random Number Generator.
        rng = np.random.default_rng(seed=m + n)

        # Generate (m x n) Matrix if not provided.
        self.M = M if M is not None else rng.uniform(-q, q, size=(m, n))

        # Generate y vector.
        self.y = rng.uniform(-q, q, size=m)

        # Generate starting points.
        self.starting_points = [rng.uniform(-q, q, size=n) for _ in range(num_sp)]

    def __repr__(self):
        return f"M: {self.M.shape}, y: {self.y.shape}, no. starting points: {len(self.starting_points)}"


class ProblemSet:
    def __init__(self):
        self.problems = [
            Problem(1, 2, num_sp=3),  # problem 1
            Problem(2, 4, num_sp=3),  # problem 2
            Problem(3, 6, num_sp=3),  # problem 3
            Problem(4, 8, num_sp=3),  # problem 4
            Problem(5, 10, num_sp=3),  # problem 5
            Problem(10, 20, num_sp=5,  # problem 6
                    M=np.array([
                        [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1]
                    ])
                    )
        ]

    def __getitem__(self, item: int):
        return self.problems[item]
