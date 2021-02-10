class Solution:
    def sortArray(self, nums):
        """
        :type nums:List[int]
        :rtype: List[int]
        """
        if len(nums) <= 1:
            return nums

        mid_point = int(len(nums) / 2)

        left, right = self.sortArray(
            nums[:mid_point]), self.sortArray(nums[mid_point:])

        return merge(left, right)


def merge(left, right):
    result = []
    left_pointer = right_pointer = 0

    while left_pointer < len(left) and right_pointer < len(right):
        if left[left_pointer] < right[right_pointer]:
            result.append(left[left_pointer])
            left_pointer += 1
        else:
            result.append(right[right_pointer])
            right_pointer += 1
    result.extend(left[left_pointer:])
    result.extend(right[right_pointer:])

    return result
