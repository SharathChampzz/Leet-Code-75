class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if not n:
            return True

        bed_len = len(flowerbed)

        for i in range(bed_len):
            if flowerbed[i] != 0 or \
                (i > 0 and flowerbed[i-1] != 0) or \
                (i < (bed_len - 1) and flowerbed[i+1] != 0):
                continue
            n -= 1
            print(f'Placing flower at {i}')
            flowerbed[i] = 1

            if not n:
                return True

        return False
            