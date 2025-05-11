class Solution:
    """
    Returns the second largest distinct element in the array.
    If it doesn't exist (e.g., all elements are equal or the array has fewer than 2 elements), returns -1.
    """
    def getSecondLargest(self, arr):
        n = len(arr)
        largest = -1
        second_largest = -1
        
        if n < 2:
            return -1

        for i in range(n):
            if arr[i] > largest:
                second_largest = largest
                largest = arr[i]
            if arr[i] < largest and arr[i] > second_largest:
                second_largest = arr[i]
        
        return second_largest

if __name__ == "__main__":
    arr = [2, 3, 1, 4, 5]
    obj = Solution()
    print(obj.getSecondLargest(arr))  # Output: 4
    arr = [1]
    print(obj.getSecondLargest(arr))  # Output: -1
    arr = [1, 2]
    print(obj.getSecondLargest(arr))  # Output: 1
    arr = [2, 2, 2]
    print(obj.getSecondLargest(arr))  # Output: -1