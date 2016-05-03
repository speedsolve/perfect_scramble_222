# -*- coding: utf-8 -*-


class Check:

    count = 0;
    perfect = 0;

    def check(self, s, scramble):

        all_faces = [s.u_face, s.f_face, s.r_face, s.b_face, s.l_face, s.d_face]

        result = 0;
        for face in all_faces:
            result += self.validate(face)

        if result == 0:
            self.perfect += 1;
            print(scramble)

        # 件数インクリメント
        self.count += 1;

        #print("current: " + "perfect: " + str(self.perfect) + " all: " + str(self.count));

    def validate(self, face):

        if face[0] == face[1]:
            return 1
        elif face[1] == face[2]:
            return 1
        elif face[2] == face[3]:
            return 1
        elif face[3] == face[0]:
            return 1
        else:
            return 0
