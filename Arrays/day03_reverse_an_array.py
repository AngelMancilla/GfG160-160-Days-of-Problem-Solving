class Solution:
    """
    Reverses the given array in place.

    This function swaps the elements from the beginning and the end of the 
    array, iterating only through the first half of the array. It modifies
    the array in place, meaning it does not use any extra space for another array.
    """

    def reverseArray(self, arr):
        half = len(arr) / 2
        for i in range(int(half)):
            arr[i], arr[len(arr) - 1 - i] = arr[len(arr) - 1 - i], arr[i]
        return arr

if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    obj = Solution()
    print(obj.reverseArray(arr))  # Output: [5, 4, 3, 2, 1]
    arr = [1]
    print(obj.reverseArray(arr))  # Output: [1]
    arr = []
    print(obj.reverseArray(arr))  # Output: []