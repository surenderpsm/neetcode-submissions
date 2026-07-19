class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = [(position[i], speed[i]) for i in range(0,len(position)) ]
        pairs.sort(reverse=True)

        stack = deque()
        for pair in pairs:
            p,s = pair

            t = (target-p)/s

            if stack and t <= stack[-1]:
                pass
                # dontn need to push
            else:
                stack.append(t)
        return len(stack)



# # number of hops is less than target. 

# 1 --- 4 --- 7 --- 10
# 2 ---- 7 ---- 10

# 4 -- 6 -- 9 -- 11
# 1 -- 3 -- 6 -- 9 -- 11
# 0 - 1 - 2 - 3 - 4
# 7 - 8 - 9 - 10

# # after 


# 7 4 1 0
# 1 2 2 1'

# 3/1 6/2 9/2 10/2
# 3   3   4    5

# 8 7 6 5 4 3 
# 4 4 4 4 4 4 
# 0.5 0.75 

