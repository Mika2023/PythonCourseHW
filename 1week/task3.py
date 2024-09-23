"""https://leetcode.com/problems/decode-string/
submissions/1399353482?envType=problem-list-v2&envId=string"""


class Solution:
    def decodeString(self, s: str) -> str:
        # use stack?
        stack = [""]
        k = 0
        seq = ""
        for i in range(len(s)):
            if s[i] in "0123456789":
                k = k * 10 + int(s[i])
                if seq:
                    stack.append(seq)
                    seq = ""
            elif s[i] == "[":
                stack.append(k)
                k = 0
            elif s[i] == "]":
                if seq:
                    stack.append(seq)
                    seq = ""
                st = stack.pop()
                while type(stack[-1]) is not int:
                    st = stack.pop() + st
                count = stack.pop()
                stack.append(count * st)
                # k_stack = stack[-1]
                # prev = stack[-2]
                # if type(k_stack) is int:
                #     k_stack = stack.pop()
                #     if type(prev) is str:
                #         prev = stack.pop()
                #         stack.append(prev+k_stack*st)
                #     else: stack.append(k_stack*st)
                # elif type(k_stack) is str:
                #     while type(stack[-1]) is str:
                #         k_stack = stack.pop()
                #         st = k_stack+st

                #     stack.append(st)
            else:
                seq += s[i]
        while len(stack):
            seq = stack.pop() + seq
        return seq


a = Solution()
print(a.decodeString("3[z]2[2[y]pq4[2[jk]e1[f]]]ef"))
