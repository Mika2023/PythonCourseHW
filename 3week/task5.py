"""https://leetcode.com/problems/count-primes/
submissions/1414573190?envType=problem-list-v2&envId=array"""


class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2:
            return 0

        sieve = [i for i in range(2, n)]

        i = 0
        num = sieve[i]
        # while i<len(sieve):
        #     j = i
        #     while j<len(sieve):
        #         if sieve[j]!=-1 and sieve[j]%sieve[i]==0: sieve[j] = -1
        #         j+=1
        #     res.append(sieve[i])
        #     i+=1

        while num * num < n:
            if num != -1:
                for j in range(i + num, len(sieve), num):
                    sieve[j] = -1
            i += 1
            num = sieve[i]

        c = 0
        for j in range(len(sieve)):
            if sieve[j] != -1:
                c += 1

        return c


a = Solution()
print(a.countPrimes(499979))
