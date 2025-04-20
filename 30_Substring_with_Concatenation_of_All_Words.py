class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        
    
        
        checkset=words.copy()
        l=0
        result=[]
        listlen=len(words)
        wordlen=len(words[0])
        concat=-1
        initial=0
        resultcount=0
        
        

        
        for r in range(0, len(s)):
            #print(checkset)
            #print(s[l:r+1])
            #print(words)
            #print(checkset)
            

            if r-l== wordlen:
                l+=1
            
            
            if s[l:r+1] in words:
                
                checkset.remove(s[l:r+1])   
                initial=l
                l=r+1
                concat=r
                for x in range(r,len(s)):

                    if s[l:x+1] in words:
                
                        if s[l:x+1] in checkset:
                            if l==concat+1:
                                checkset.remove(s[l:x+1])
                                concat=x
                                l=x+1
                            
                
                if len(checkset)==0:
                    result.append(initial)
                    resultcount+=1
                checkset=words.copy()
                #print(words)
                #print(checkset)
                l=initial  

              

        return result
        