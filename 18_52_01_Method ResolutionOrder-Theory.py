class A: pass
class B: pass
class C: pass
class D(A,B): pass
class E(B,C): pass
class F(D,E,C): pass


print(A.mro()) #AO
print(B.mro()) #B,O
print(C.mro()) #C,O
print(D.mro()) #D,A,B,O
print(E.mro()) #E,B,C,O
print(F.mro()) #F,D,A,E,B,C,O
