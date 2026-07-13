class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(s):
            return False
        sh={}
        th={}
        for i in s:
            if i in sh:
                sh[i]+=1
            else:
                sh[i]=1
        for j in t:
            if j in th:
                th[j]+=1
            else:
                th[j]=1
        if th==sh:
            return True
        else:
            return False
