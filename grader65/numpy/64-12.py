import numpy as np
def f1(v): return np.array_equal(np.arange(0,v.shape[0],1),v) 

def f2(u, v): return np.add(u, np.flip(v))


def f3(M, v): return np.multiply(M,v)


#----- DON'T modify any of the following lines -----
for k in range(int(input())): exec(input().strip())


# exec("import dis\ndef has_loop(f):\n b = dis.Bytecode(f)\n for e in b:\n  ar = e.argrepr\n  if '<listcomp>' in ar or '<setcomp>' in ar or '<dictcomp>' in ar or (e.opname=='JUMP_ABSOLUTE' and e.argval<e.offset):\n   return True\n return False")
# # u = np.array([2, 4, 8, 9]); v = np.array([7,3,1,2])
# # print(f2(u,v).tolist(), f2(u,v[::-1]).tolist())

# if has_loop(f2): raise Exception('f2 has loops')
