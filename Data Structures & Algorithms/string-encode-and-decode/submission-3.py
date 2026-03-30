class Solution:

    def encode(self, strs: List[str]) -> str:
        out = ""
        for s in strs:
            out += f"{len(s)}#{s}"
        return out

    def decode(self, s: str) -> List[str]:
        out = []
        i = 0
        while i < len(s):
            start = i
            while s[i] != "#":
                i += 1
            num = int(s[start:i])
            out.append(s[i+1:i+num+1])
            i += num + 1
        return out
