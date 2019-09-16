import sympy
from sympy import pprint
f,d =sympy.symbols("f d")  ##define f and d as symbols

##problem 1
print("PROBLEM #1")
convex= sympy.Matrix([[1,0],[-1/f,1]])

concave= sympy.Matrix([[1,0],[1/f,1]])

distance= sympy.Matrix([[1,d],[0,1]])

system1=concave*distance*convex
pprint(system1)
print(sympy.latex(system1), "\n")

#PROBLEM 2
print("PROBLEM #2")

M1=sympy.Matrix([[1,0],[-1/f,1]])
M2=sympy.Matrix([[1,3*d],[0,1]])

T=M1*M2
pprint(T)

