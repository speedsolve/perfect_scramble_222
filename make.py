# -*- coding: utf-8 -*-
import random


class Make:

    LENGTH = 20
    TURN = ("U", "R", "F", "U'", "R'", "F", "U2", "R2", "F2")

    scramble = "";

    def make(self):

        self.scramble = ""
        pre_turn = ""

        while len(self.scramble) < self.LENGTH:

            turn = random.choice(self.TURN);

            if turn.find("U") > -1 and pre_turn.find("U") > -1:
                continue
            elif turn.find("R") > -1 and pre_turn.find("R") > -1:
                continue
            elif turn.find("F") > -1 and pre_turn.find("F") > -1:
                continue
            else:
                self.scramble += turn + " "
                pre_turn = turn

        return self.scramble


if __name__ == "__main__":

    from scramble import Scramble
    from solver import Solver
    from check import Check

    s = Solver()
    c = Check()
    m = Make()

    for i in range(10000):

        alg = m.make()
        alg = alg.strip()
        alg = alg.rstrip()
        scramble = Scramble()
        s.move(alg.split(), scramble)
        c.check(scramble, alg)
