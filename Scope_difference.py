# Find the maximum absolute value between any two elements in an array a. 
# Sample Input:
# 3       __elements[] size N = 3
# 1 2 5   __elements = [1, 2, 5]

# Sample Output:
# 4

class Difference:
    def __init__(self, a):
        self.__elements = a
        self.maximumDifference = None

    def computeDifference(self):
        differences = []
        for i in range(len(self.__elements)):
            for j in range(i+1, len(self.__elements)):
                differences.append(abs(a[i]-a[j]))
        self.maximumDifference = max(differences)
    
_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)