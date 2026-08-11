class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k = k % len(nums)

        news = nums[-k:]
        del nums[-k:]

        nums[:] = news + nums