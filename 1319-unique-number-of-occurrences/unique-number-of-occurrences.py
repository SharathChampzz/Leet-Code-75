class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        mapping = Counter(arr)

        return len(mapping) == len(set(mapping.values()))
        