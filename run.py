if __name__ == "__main__":

    from pprint import pprint
    from scramble import Scramble
    from solver import Solver
    from check import Check

    scramble = Scramble()
    s = Solver()
    c = Check()

    for line in open('./scramble.txt', 'r'):

        s.move(line.split(), scramble)
        c.check(scramble);