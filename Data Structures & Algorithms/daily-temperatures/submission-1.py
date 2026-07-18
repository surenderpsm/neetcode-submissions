class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        for i,t in enumerate(temperatures):
            
            for j in range(i+1, len(temperatures)):
                if temperatures[j] > t:
                    result[i] = j-i
                    break
        return result


# O(n^2) is allowed cause of constraints only 1000 is max length

# for each temperature, we can run through entire array to check until a bigger temp is found.


