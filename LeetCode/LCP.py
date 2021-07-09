from itertools import combinations
import operator


def longestCommonPrefix(strs):
    if 1 <= len(strs) <= 200 and 0 <= len([x for x in strs]) <= 200:
        res = [] 
        for x in combinations(strs, 2):
	        if len(res) < len([i for i in x[0] if i in x[1]]):
		        res = [i for i in x[0] if i in x[1]]
        return ''.join(res)



print(longestCommonPrefix(["dog", "racecar", "car"]))
