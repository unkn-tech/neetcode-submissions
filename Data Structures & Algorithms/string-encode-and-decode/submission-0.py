class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded=""
        for word in strs:
            encoded+=str(len(word))+"#"+word
        return encoded
    def decode(self, s: str) -> List[str]:
        ans=[]
        i=0
        while i<len(s):
            j=i
            while s[j]!="#":
                j+=1
            length=int(s[i:j])
            j+=1
            word=s[j:j+length]
            ans.append(word)
            i=j+length
        return ans
