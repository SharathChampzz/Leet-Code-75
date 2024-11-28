class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True

        bed_len = len(flowerbed)

        for i in range(bed_len):
            if flowerbed[i] != 0 or \
                (i > 0 and flowerbed[i-1] != 0) or \
                (i < (bed_len - 1) and flowerbed[i+1] != 0):
                continue
            
            n -= 1 # plant
            flowerbed[i] = 1

            if n == 0:
                return True

        return False
            