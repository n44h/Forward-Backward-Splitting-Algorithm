import numpy as np


class FBS:
    def __init__(self,
                 M: np.ndarray,
                 y: np.ndarray,
                 x: np.ndarray,
                 tau=0.2,
                 step_size=0.3):

        # Initialize the class attributes.
        self.M = M
        self.y = y
        self.x = x
        self.tau = tau
        self.step_size = step_size

    def _prox(self, x):
        y = np.sign(x)
        y[y > self.tau] = self.tau
        y[y < -self.tau] = -self.tau
        y = y - self.tau * np.maximum((np.abs(x) - self.tau), 0)
        return y

    def _gradient(self) -> float:
        c = (self.M @ self.x) - self.y

        return 0.5 * self.M.T @ c / np.linalg.norm(c)

    def _forward(self):
        return self.x - (self.step_size * self._gradient())

    def _backward(self, x_k1):
        return self._prox(x_k1)

    def solve(self, max_iter: int = 1000, tol: float = 1e-6) -> (np.ndarray, list):
        # Log every value of x.
        log = []

        # k keeps track of number of iterations.
        k: int = 0
        distance: float = np.inf

        while k < max_iter and distance > tol:
            # Log the current value of x.
            log.append(self.x)

            # Perform forward backward operations.
            x_k1 = self._backward(self._forward())

            # Compute step length.
            distance = np.linalg.norm(self.x - x_k1)

            # Update x.
            self.x = x_k1

            # Increment the iteration count.
            k += 1

        # Return the optimal x and the steps taken to reach there.
        return self.x, log
