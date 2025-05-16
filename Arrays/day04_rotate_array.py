class Solution:
    """
    Rotates the array to the left by d positions in place.
    Shifts elements to the left and moves the first d elements to the end,
    updating the original array without creating a new one.
    """
    def rotateArr(self, arr, d):
        n = len(arr)
        d = d % n
        arr[:] = arr[d:] + arr[:d]
        return arr
    
if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    d = 2
    obj = Solution()
    print(obj.rotateArr(arr, d))  # Output: [3, 4, 5, 1, 2]
    arr = [1]
    d = 1
    print(obj.rotateArr(arr, d))  # Output: [1]
    arr = []
    d = 0
    print(obj.rotateArr(arr, d))  # Output: []