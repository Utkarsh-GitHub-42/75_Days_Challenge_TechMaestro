class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s=''
        b=[]
        for i in digits:
                s+=str(i)
        s=int(s)+1
        for i in str(s):
                b.append(int(i))
        return b
                
                
        
