def gcdOfStrings(str1: str, str2: str) -> str:
        tested={}
        
        for i in range (0,len(str2)):
            str2test=str2[0:i+1]
            tested[str2test]=str2.count(str2test)
        
        return sorted(tested.items(), key=lambda item: item[1])
            
            


print(gcdOfStrings("ABABAB","ABAB"))