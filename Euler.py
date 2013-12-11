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

    def nthPrime(self, num):
        #168713
        i = 0;
        p = 0;
        while p < num+1:
            if self.isPrime(i):
                print `p` + ":" + `i`
                p += 1
               
            i += 1

    def isPrime(self, n):
        if n<=0:
            return False
        if n<=2:
            return True
        if n%2==0:
            return False
        for i in range(3, int(n**0.5)+1, 2):
            if n%i == 0:
                return False

        return True

    def prodInSeries(self, n):
        #149695
        n = str(n)
        x = 0
        for i in range(0, len(n)-5):
            tmp = int(n[i]) * int(n[i+1]) * int(n[i+2]) * int(n[i+3]) * int(n[i+4])
            if tmp > x:
                x = tmp
                print x
        return x

    def pythagTriplet(self, n):
        for a in range(1,n):
            for b in range(1,n):
                c_s = (a**2 + b**2)
                if self.isPerfectSquare(c_s):
                    print `c_s` + "(" + `a` + "," + `b` + ")"
                    if a + b + (c_s**0.5) == n:
                        break
            if a + b + (c_s**0.5) == n:
                break
        return a * b * (c_s ** 0.5)

    def sumPrimes(self, n):
        sum = 0
        for i in range(2,n):
            if self.isPrime(i):
                sum += i
                print i

        return sum

    def divTriNumber(self, n):
        #92021
        curTri = 0
        i = 1
        numDiv = 0
        while numDiv < n:
            curTri += i
            numDiv = self.numDivisors(curTri)
            print `i` + ": curTri = " + `curTri` + ", numFactors = " + `numDiv`
            i += 1

    def numDivisors(self, n):
        # Get prime factors
        curRes = n
        curFac = 2
        numFac = -1
        factors = []
        powers = []
        p = -1
        while not self.isPrime(curRes):
            if curRes % curFac == 0:
                curRes = curRes / curFac
                factors.append(curFac)
                numFac += 1
                if len(factors)>1 and factors[numFac] == factors[numFac-1]:
                    powers[p] += 1
                else:
                    powers.append(1)
                    p += 1
                    
            else:
                curFac += 1
                while not self.isPrime(curFac):
                    curFac += 1
                    
        factors.append(curRes)
        numFac += 1
        if len(factors)>1 and factors[numFac] == factors[numFac-1]:
            powers[p] += 1
        else:
            powers.append(1)

        res = 1
        for i in range(0,len(powers)):
            res = res * (powers[i]+1)

        return res
    
    def isPerfectSquare(self, n):
        if (n**0.5 % 1 == 0):
            return True
        else:
            return False
        
