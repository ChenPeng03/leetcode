class Solution(object):
    def getPermutation(self, n, k):
        temp = ''
        result = ''
        input_list = [i for i in range(n + 1)]
        k = k - 1
        fact = math.factorial(n - 1)
        for i in range(len(input_list) - 1, -1, -1):
            index = k / fact
            result += input_list[index]
            input_list = input_list[:i] + input_list[i + 1:]
            k = k % fact
            fact /= i
        return result
