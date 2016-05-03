# -*- coding: utf-8 -*-


class Solver:

    def move(self, strings, scramble):

        for m in strings:
            if m == "U":
                scramble.move_u()
            elif m == "R":
                scramble.move_r()
            elif m == "F":
                scramble.move_f()
            elif m == "U'":
                scramble.move_u_rev()
            elif m == "R'":
                scramble.move_r_rev()
            elif m == "F'":
                scramble.move_f_rev()
            elif m == "U2":
                scramble.move_u2()
            elif m == "R2":
                scramble.move_r2()
            elif m == "F2":
                scramble.move_f2()

