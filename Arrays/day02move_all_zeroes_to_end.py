class Solution:
    """
    Move all the zeros in the array to the right end 
    while maintaining the relative order of the non-zero elements.
    """
    def push_zeros_to_end(self, arr):
        pos = 0
        for num in arr:
            if num != 0:
                arr[pos] = num
                pos += 1
        arr[pos:] = [0] * (len(arr) - pos)
        return arr

if __name__ == "__main__":
    arr = [0, 1, 0, 3, 12]
    obj = Solution()
    print(obj.push_zeros_to_end(arr))  # Output: [1, 3, 12, 0, 0]
    arr = [0, 0, 0]
    print(obj.push_zeros_to_end(arr))  # Output: [0, 0, 0]
    arr = [1, 2, 3]
    print(obj.push_zeros_to_end(arr))  # Output: [1, 2, 3]
    arr = []
    print(obj.push_zeros_to_end(arr))  # Output: []

