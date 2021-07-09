class Solution:
    def reverse(self, x: int) -> int:
        signedint = [-2**31, 2 ** 31 -1]
        if x > 0 and x < signedint[1]:
            _list = list(str(x))
            return int(''.join(str(x) for x in list(reversed(_list))))
        elif x < 0 and x > signedint[0]:
            _list = list(str(x))
            _list.remove('-')
            _list.reverse()
            _list.insert(0, '-')
            return int(''.join(_list))
