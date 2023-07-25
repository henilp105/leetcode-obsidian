class Solution:
    def intToRoman(self, num: int) -> str:
        v = {1:"I",5:"V",4:"IV",9:"IX",10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M',40:"XL",90:"XC",400:"CD",900:"CM"}
        s=''
        for i in reversed(sorted(v.keys())):
            s+=v[i]*int(num/i)
            num-=i*int(num/i)
        return s