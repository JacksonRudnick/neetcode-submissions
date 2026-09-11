class Solution:
    def isValid(self, s: str) -> bool:
        o = ['[', '{', '(']
        c = [']', '}', ')']

        m = []

        for i in s:
            if i in o:
                m.append(i)
            elif len(m) == 0:
                return False
            else:
                try:
                    idx = c.index(i)
                    if m[-1] == o[idx]:
                        m.pop()
                    else:
                        return False
                except ValueError:
                    continue

        if len(m) > 0:
            return False
        return True