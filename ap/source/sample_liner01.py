#liner01.py
#
#点A(Ax,Ay),B(Bx,By)を通る直線上の点で、点Cについて、Cxの値が決まった時のCyを求める。
#

#
#点A(Ax,Ay),
#  B(Bx,By)
#   2 5
#   3 7
#
#点C(Cx)
#    4
#
#
# ●連立方程式を立てる
#    5=2a+b
#    7=3a+b
#
# ●行列で書く
#    (     )(   )=(   )
#      2,1    a     5
#      3,1    b     7
#
#
# ●逆行列で行列式を解くことで、a,b(傾き,Y切片)を求める
#   (逆行列)*(     )(   )=(逆行列)*(   )
#             2,1    a    -1,1     5
#             3,1    b     3,-2    7
#
#   (   )=(答)
#     a    2
#     b    1
#
# ●直線の方程式にXcを代入しYcを求める
#   Yc=aXc+b
#   YC=2*4+1=9


import numpy as np
from numpy.linalg import inv


class getpoint():
    def get(self,Ax,Ay,Bx,By,Cx):
        a = np.array([[Ax,1], [Bx,1]])
        ainv = inv(a)
        #print(ainv)
        amatmul=np.matmul(ainv,np.array([[Ay],[By]]))
        #print(amatmul)

        rtn= amatmul[0]*Cx+amatmul[1]
        return rtn[0]


a=getpoint().get(2,5,3,7,4)
print("a",a)
