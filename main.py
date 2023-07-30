from fbs import FBS
from problem_set import ProblemSet
from reporter import Reporter


def main():
    # Initialize a report generator.
    reporter = Reporter()

    # Initialize parameters.
    tau = 0.2
    step_size = 0.3
    max_steps = 10_000

    for problem in ProblemSet():
        M = problem.M
        y = problem.y
        starting_points = problem.starting_points

        for x in starting_points:
            # Initialize solver.
            fbs = FBS(M, y, x, tau, step_size)

            # Compute solution.
            solution, steps = fbs.solve(max_steps)

            # Append to report.
            reporter.append(M, y, x, solution, tau, step_size, steps)

    # Generate the report.
    reporter.generate_report()


if __name__ == '__main__':
    main()
