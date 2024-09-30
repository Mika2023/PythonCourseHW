"""https://leetcode.com/problems/
implement-trie-prefix-tree/submissions/
1404174640?envType=problem-list-v2&envId=string"""


class TrieNode:
    def __init__(self) -> None:
        self.child = []
        self.value = ""
        self.isWord = False


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def isInChild(self, temp: TrieNode, pres: TrieNode) -> int:
        for i in range(len(pres.child)):
            if (
                pres.child[i].value == temp.value
                and pres.child[i].isWord == temp.isWord
            ):
                return i
        return -1

    def isInChild_withoutBool(self, temp: TrieNode, pres: TrieNode) -> int:
        for i in range(len(pres.child)):
            if pres.child[i].value == temp.value:
                return i
        return -1

    def insert(self, word: str) -> None:
        pres = self.root
        for i in range(len(word)):

            temp = TrieNode()
            temp.value = word[i]
            temp.isWord = i == len(word) - 1

            res = self.isInChild_withoutBool(temp, pres)

            if res != -1:
                pres = pres.child[res]
            else:
                pres.child.append(temp)
                pres = pres.child[-1]

        pres.isWord = True

    def search(self, word: str) -> bool:
        pres = self.root
        for i in range(len(word)):

            temp = TrieNode()
            temp.value = word[i]
            temp.isWord = i == len(word) - 1

            res = self.isInChild_withoutBool(temp, pres)

            if res != -1:
                pres = pres.child[res]
            else:
                return False

        return pres.isWord

    def startsWith(self, prefix: str) -> bool:
        pres = self.root
        for i in range(len(prefix)):

            temp = TrieNode()
            temp.value = prefix[i]

            res = self.isInChild_withoutBool(temp, pres)

            if res != -1:
                pres = pres.child[res]
            else:
                return False

        return True


a = Trie()
a.insert("ab")
print(a.search("abc"), a.search("ab"), a.startsWith("abc"), a.startsWith("ab"))
a.insert("ab")
print(a.search("abc"), a.startsWith("abc"))
a.insert("abc")
print(a.search("abc"), a.startsWith("abc"))
