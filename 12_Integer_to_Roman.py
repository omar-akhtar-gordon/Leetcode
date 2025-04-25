class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        value = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
        symbol=["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        pos=0
        roman=""

        while num!=0:
            if num>=value[pos]:
                roman+=symbol[pos]
                num-=value[pos]
            else:
                pos+=1

        return roman        
