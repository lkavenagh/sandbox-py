from fractions import gcd
class Euler:
    def largestPalindromeProduct(self, digits):
        curLargest = 0;
        x = '1'
        y = '9'
        for i in range(1, digits):
            x = x + '0'
            y = y + '9'

        x = int(x)
        y = int(y)
        
        for i in range(x,y):
            for j in range(i,y):
                res = i * j
                if str(res) == str(res)[::-1] and res > curLargest:
                    curLargest = res

        return curLargest
            
    def smallestMultiple(self, maxint):
        #193945
        found = False
        curMult = maxint
        
        while (not found):
            found = True
            for i in range(1,maxint):
                if curMult % i != 0:
                    found = False
                    break

            curMult += maxint

        curMult -= maxint
        return curMult

    def squareSumDiff(self, num):
        #195498
        x = 0
        y = 0
        for i in range(1, num+1):
            x = x + i**2
            y = y + i

        y = y**2

        return y - x

    def selfPowers(self, num):
        #57451
        res = 0
        for i in range(num, 0, -1):
            resstr = str(res + i**i)[-10:]
            res = int(resstr)
            print(res)

        return res

    def lcm(self,numbers):
        return reduce(lambda x, y: (x*y)/gcd(x,y), numbers, 1)

    def A(self, n):
        ret = 0
        i = n
        while i > 0:
            ret = ret + self.lcm((n, i))
            i -= 1

        return ret / n

    def S(self, n):
        ret = 0
        i = n
        while i > 0:
            print i
            ret = ret + self.A(i)
            i -= 1

        return ret
        
