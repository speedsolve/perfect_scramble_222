# -*- coding: utf-8 -*-

if __name__ == "__main__":

    from scramble import Scramble
    from solver import Solver
    from check import Check

    s = Solver()
    c = Check()

    for line in open('./scramble.txt', 'r'):

        scramble = Scramble()
        s.move(line.split(), scramble)
        c.check(scramble, line)
