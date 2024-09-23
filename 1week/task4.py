"""https://leetcode.com/problems/bulls-and-cows/submissions/1394755662?envType=problem-list-v2&envId=string"""


class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = cows = 0
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bulls += 1
                if i < len(secret) - 1:
                    secret = secret[:i] + "b" + secret[i + 1 :]
                else:
                    secret = secret[:i] + "b"

                if i < len(guess) - 1:
                    guess = guess[:i] + "B" + guess[i + 1 :]
                else:
                    guess = guess[:i] + "B"

        for i in range(len(secret)):
            if guess[i] in secret:
                cows += 1
                ind = secret.find(guess[i])
                if ind < len(secret) - 1:
                    secret = secret[:ind] + "c" + secret[ind + 1 :]
                else:
                    secret = secret[:ind] + "c"
        return f"{bulls}A{cows}B"


a = Solution()
print(a.getHint("11", "10"))
