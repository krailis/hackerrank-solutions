import re

s = input()
m = re.match(r'M{0,3}(C[MD]|D?C{0,3})(X[CL]|L?X{0,3})(I[VX]|V?I{0,3})$', s)
if m:
    print(True)
else:
    print(False)
