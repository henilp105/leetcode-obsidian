class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data = []
    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if not self.data or x < self.data[-1][1]: self.data.append([x, x])
        else: self.data.append([x, self.data[-1][1]])
    def pop(self):
        """
        :rtype: void
        """
        self.data.pop()
    def top(self):
        """
        :rtype: int
        """
        return self.data[-1][0]
    def getMin(self):
        """
        :rtype: int
        """
        return self.data[-1][1]