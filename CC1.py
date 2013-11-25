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
