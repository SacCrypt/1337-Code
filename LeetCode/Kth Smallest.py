import pdb
import itertools
def bruh(mat, n):
    pdb.set_trace()
    _list = list(itertools.chain.from_iterable(mat))    
    for x in range(n-1):
	    _list.remove(min(_list))
    return _list[0]

print(bruh([[1,2],[1,3]], 2))

