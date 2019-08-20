class Solution:
    def __init__(self):
        self.array = []

    def Insert(self, num):
        # write code here
        self.array.append(num)
        self.array.sort()

    def GetMedian(self, M):
        # write code here
        length = len(self.array)
        if length % 2 == 1:
            return self.array[length // 2]
        return (self.array[length // 2] + self.array[length // 2 - 1]) / 2.0


class Solution1:
    def __init__(self):
        self.left = []
        self.right = []
        self.count = 0

    def Insert(self, num):
        if self.count & 1 == 0:
            self.left.append(num)
        else:
            self.right.append(num)
        self.count += 1

    def GetMedian(self, M):
        if self.count == 1:
            return self.left[0]
        self.maxHeap(self.left)
        self.minHeap(self.right)
        if self.left[0] > self.right[0]:
            self.left[0], self.right[0] = self.right[0], self.left[0]
        self.maxHeap(self.left)
        self.minHeap(self.right)
        if self.count & 1 == 0:
            return (self.left[0] + self.right[0]) / 2.0
        else:
            return self.left[0]

    def maxHeap(self, arr):
        n = len(arr)
        for i in range(n, -1, -1):
            self.max_heapify(arr, n, i)

    def max_heapify(self, arr, n, i):
        largest = i
        l = 2 * i + 1  # left = 2*i + 1
        r = 2 * i + 2  # right = 2*i + 2

        if l < n and arr[i] < arr[l]:
            largest = l

        if r < n and arr[largest] < arr[r]:
            largest = r

        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]  # 交换

            self.max_heapify(arr, n, largest)

    def minHeap(self, arr):
        n = len(arr)
        for i in range(n, -1, -1):
            self.min_heapify(arr, n, i)

    def min_heapify(self, arr, n, i):
        minimum = i
        l = 2 * i + 1  # left = 2*i + 1
        r = 2 * i + 2  # right = 2*i + 2

        if l < n and arr[i] > arr[l]:
            minimum = l

        if r < n and arr[minimum] > arr[r]:
            minimum = r

        if minimum != i:
            arr[i], arr[minimum] = arr[minimum], arr[i]  # 交换
            self.min_heapify(arr, n, minimum)
