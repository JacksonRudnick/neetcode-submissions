class Solution:
    def encode(self, strs: List[str]) -> str:
        master = ""

        for i in strs:
            master += str(len(i)) + '/' + i

        return master

    def decode(self, s: str) -> List[str]:
        master = []

        while len(s) > 0:
            pos = s.find('/')
            length = int(s[0:pos])
            master.append(s[pos+1:length+pos+1])
            s = s[length+pos+1:]

        return master
        