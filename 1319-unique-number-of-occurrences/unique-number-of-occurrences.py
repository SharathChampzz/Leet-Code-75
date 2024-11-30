class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        mapping = defaultdict(int)

        for num in arr:
            mapping[num] += 1 # build mapping

        return len(mapping) == len(set(mapping.values()))
        