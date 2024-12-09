"""https://leetcode.com/problems/find-k-closest-elements/
submissions/1474573798"""

from typing import List

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        if len(arr) == k: return arr
        if x <= arr[0]: return arr[:k]
        if x >= arr[-1]: return arr[-k:]

        firstClosest = self.binarySearch(arr, x)
        left = firstClosest - 1
        right = left + 1

        while right - left - 1 < k:
            if left < 0:
                right += 1
                continue

            if right == len(arr) or abs(arr[left] - x) <= abs(arr[right] - x):
                left -= 1
            else:
                right += 1

        return arr[left + 1 : right]

    def binarySearch(self, array: List[int], target: int) -> int:
        left, right = 0, len(array) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if array[mid] == target:
                return mid
            if array[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return left


    
a = Solution()
a.findClosestElements([1,1,2,2,2,2,2,3,3],3,3)