import numpy as np
## 
# print(np.zero_one((3,3), dtype=int)) # no this module
# print(np.identity(3, dtype=int)) # correct
# np.diag_one(3,dtype=int) # no this module
# print(np.arrayone((3,3), dtype=int))) # no this module

d = np.ones((5,5), dtype = int)
# d[::2] = 0
# d[:2] = 0
# d[,::2] = 0 # error
# d[,:2] = 0 # error
d[:,::2] = 0 # change only columb
print(d)
