from solver import Solver
from io import IO

if __name__ == "__main__":
    io = IO()
    solver = Solver(io.get_strcalc())
    solver.calc()
    io.print_ans(solver.get_ans())