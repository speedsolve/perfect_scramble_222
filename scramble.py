# -*- coding: utf-8 -*-

class Scramble:

    # キューブを定義する
    u_face = ["w", "w", "w", "w"]
    f_face = ["g", "g", "g", "g"]
    r_face = ["r", "r", "r", "r"]
    b_face = ["y", "y", "y", "y"]
    l_face = ["o", "o", "o", "o"]
    d_face = ["d", "d", "d", "d"]

    def move_u(self):

        tmp_u_face = self.u_face[:]
        tmp_f_face = self.f_face[:]
        tmp_r_face = self.r_face[:]
        tmp_b_face = self.b_face[:]
        tmp_l_face = self.l_face[:]

        tmp_u_face[0] = self.u_face[3]
        tmp_u_face[1] = self.u_face[0]
        tmp_u_face[2] = self.u_face[1]
        tmp_u_face[3] = self.u_face[2]

        tmp_f_face[0] = self.r_face[0]
        tmp_f_face[1] = self.r_face[1]

        tmp_r_face[0] = self.b_face[0]
        tmp_r_face[1] = self.b_face[1]

        tmp_b_face[0] = self.l_face[0]
        tmp_b_face[1] = self.l_face[1]

        tmp_l_face[0] = self.f_face[0]
        tmp_l_face[1] = self.f_face[1]

        self.u_face = tmp_u_face
        self.f_face = tmp_f_face
        self.r_face = tmp_r_face
        self.b_face = tmp_b_face
        self.l_face = tmp_l_face

    def move_r(self):

        tmp_u_face = self.u_face[:]
        tmp_f_face = self.f_face[:]
        tmp_r_face = self.r_face[:]
        tmp_b_face = self.b_face[:]
        tmp_d_face = self.d_face[:]

        tmp_u_face[1] = self.f_face[1]
        tmp_u_face[2] = self.f_face[2]

        tmp_f_face[1] = self.d_face[1]
        tmp_f_face[2] = self.d_face[2]

        tmp_r_face[0] = self.r_face[3]
        tmp_r_face[1] = self.r_face[0]
        tmp_r_face[2] = self.r_face[1]
        tmp_r_face[3] = self.r_face[2]

        tmp_b_face[0] = self.u_face[2]
        tmp_b_face[3] = self.u_face[1]

        tmp_d_face[1] = self.b_face[3]
        tmp_d_face[2] = self.b_face[0]

        self.u_face = tmp_u_face
        self.f_face = tmp_f_face
        self.r_face = tmp_r_face
        self.b_face = tmp_b_face
        self.d_face = tmp_d_face

    def move_f(self):

        tmp_u_face = self.u_face[:]
        tmp_f_face = self.f_face[:]
        tmp_r_face = self.r_face[:]
        tmp_l_face = self.l_face[:]
        tmp_d_face = self.d_face[:]

        tmp_u_face[2] = self.l_face[1]
        tmp_u_face[3] = self.l_face[2]

        tmp_f_face[0] = self.f_face[3]
        tmp_f_face[1] = self.f_face[0]
        tmp_f_face[2] = self.f_face[1]
        tmp_f_face[3] = self.f_face[2]

        tmp_r_face[0] = self.u_face[3]
        tmp_r_face[3] = self.u_face[2]

        tmp_l_face[1] = self.d_face[0]
        tmp_l_face[2] = self.d_face[1]

        tmp_d_face[0] = self.r_face[3]
        tmp_d_face[1] = self.r_face[0]

        self.u_face = tmp_u_face
        self.f_face = tmp_f_face
        self.r_face = tmp_r_face
        self.l_face = tmp_l_face
        self.d_face = tmp_d_face

    def move_u_rev(self):
        self.move_u()
        self.move_u()
        self.move_u()

    def move_r_rev(self):
        self.move_r()
        self.move_r()
        self.move_r()

    def move_f_rev(self):
        self.move_f()
        self.move_f()
        self.move_f()

    def move_u2(self):
        self.move_u()
        self.move_u()

    def move_r2(self):
        self.move_r()
        self.move_r()

    def move_f2(self):
        self.move_f()
        self.move_f()


if __name__ == "__main__":

    from pprint import pprint

    s = Scramble()
    s.move_f_rev()
    s.move_u2()
    s.move_r()
    s.move_u()
    s.move_r_rev()
    s.move_f()
    s.move_u()
    s.move_f()
    s.move_r()
    s.move_u_rev()
    s.move_r_rev()

    pprint(s.u_face)
    pprint(s.f_face)
    pprint(s.r_face)
    pprint(s.b_face)
    pprint(s.l_face)
    pprint(s.d_face)
