class CC1:
    def isUnique(self, str):
        d = self.str2hm(str)
        return not any(e>1 for e in d.values())
        
    def reverse(self, str):
        newstr = ''
        for i in range(len(str)-1,-1,-1):
            newstr = newstr + str[i]

        return newstr

    def isPerm(self, str1, str2):

        d1 = self.str2hm(str1);
        d2 = self.str2hm(str2);

        return d1==d2

    def str2hm(self, str):
        d = dict()
        for i in range(0, len(str)):
            if str[i] in d:
                d[str[i]] = d.get(str[i])+1
            else:
                d[str[i]] = 1

        return d

    def replaceSpaces(self, str, realLen):
        newStr = ''

        for i in range(0, realLen):
            if str[i] == ' ':
                newStr = newStr + '%20'
            else:
                newStr = newStr + str[i]

        return newStr

    def compressString(self, mystr):
        newStr = mystr[0]
        curCount = 1
        
        for i in range(1, len(mystr)):
            if mystr[i] == mystr[i-1]:
                curCount += 1
            else:
                if curCount == 1:
                    newStr = newStr + mystr[i]
                else:
                    newStr = newStr + str(curCount) + mystr[i]
                    curCount = 1

        if len(newStr) < len(mystr):
            return newStr
        else:
            return mystr

    def isSubstring(self, s1, s2):
        return s1 in s2

    def isRotation(self, s1, s2):
        if (len(s1) != len(s2)):
            return False

        return self.isSubstring(s2, s1+s1)
            
