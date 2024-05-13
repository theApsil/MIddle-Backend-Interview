'''
https://leetcode.com/problems/merge-similar-items
'''

from collections import defaultdict
from typing import List


def mergeSimilarItems(items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
    dd = defaultdict(int)
    mergred = items1 + items2
    temp = []

    for item in mergred:
        if item[0] not in temp:
            dd[item[0]] += item[1]
        else:
            dd[item[0]] = dd[item[0]] + item[1]

    for _ in sorted(dd): temp.append([_, dd[_]])
    return temp


items1 = [[1, 1], [4, 5], [3, 8]]
items2 = [[3, 1], [1, 5]]

print(mergeSimilarItems(items1, items2))
