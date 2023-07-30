from os.path import join, dirname
import numpy as np


def objective_func(M: np.ndarray, y: np.ndarray, x: np.ndarray, tau: float):
    return (0.5 * np.linalg.norm(np.matmul(M, x) - y)) + (tau * np.linalg.norm(x, ord=1))


def counter():
    count = 1
    while True:
        yield count
        count += 1


class Reporter:
    def __init__(self):
        self.problem_number = counter()
        self.report = ""

    def append(self,
               M: np.ndarray,
               y: np.ndarray,
               x: np.ndarray,
               solution: np.ndarray,
               tau: float,
               step_size: float,
               steps: list):

        # Calculate the objective function values.
        obj_sp = objective_func(M, y, x, tau)
        obj_sol = objective_func(M, y, solution, tau)

        self.report += 30 * "__" + "\n"
        self.report += f"Problem {next(self.problem_number)}\n"

        self.report += f"M = {M}\n"
        self.report += f"y = {y}\n"
        self.report += f"tau = {tau}\n"
        self.report += f"Step size = {step_size}\n\n"

        self.report += f"Starting Point                    : {np.round(x, 3)}\n"
        self.report += f"Objective value at starting point : {np.round(obj_sp, 3)}\n\n"

        self.report += f"Solution Point                    : {np.round(solution, 3)}\n"
        self.report += f"Objective value at solution point : {np.round(obj_sol, 3)}\n\n"

        self.report += f"No. Steps: {len(steps)}\n\n"

    def generate_report(self, write_to_file: bool = True):
        # Generate path to report file.
        filepath = join(dirname(dirname(__file__)), "reports", "report.txt")

        # Write the report to file.
        if write_to_file:
            with open(filepath, "w") as f:
                f.write(self.report)

        # Print the report to console.
        print(self.report)
