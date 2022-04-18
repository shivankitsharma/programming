"""
Two ways to do it:
Memoization: (top- down)
Tabulation: (bottom - up)
We generally prefer bottom-up tabulation over top down Memoization 

Classic DP problems
1. computing the nth Fibonacci number/solution/
2. computing C(n,k) (Classic 2D DP)

counting problems
1. Number of ways to climb up stairs (1D)
2. Number of paths from a top-left to bottom-right of a grid(2D)
"""

###Unique paths
### First row and first column is 1 values
### Then we add row - 1, col and row, col - 1 to get current value 
### m -1 and n-1 because python starts from 0,0
m = 3 #rows
n = 7 #columns
def uniquepaths(m,n):
    table = [ [1 for j in range(m)] for i in range(n)] #2D array
    
    for row in range(1, n):
        for col in range(1,m):
            table[row][col] = table[row-1][col] + table[row][col-1]            
    return table[n-1][m-1]

uniquepaths(m,n)
"""
1	1	1	1	1	1	1
1	2	3	4	5	6	7
1	3	6	10	15	21	28
"""

###Unique path with Obstacles
def uniquePathsWithObstacles (self, obstacleGrid):
    """
    :type obstacleGrid: List[List[int]] 
    :rtype: int
    """
    table = [ [0 for j in range(len(obstacleGrid[0]))] for i in range(len(obstacleGrid))]
    #First fill in the base cases 
    if obstacleGrid[0][0] == 1:
        table[0][0] = 0 
    else:
        table[0][0] = 1
    #Fill in row 0 
    for col in range(1, len(obstacleGrid[0])): 
        if obstacleGrid[0][col] == 1:
            table[0][col] = 0 
        else:
            table[0][col] = table[0][col-1]
    #Fill in col 0 
    for row in range(1, len(obstacleGrid)): 
        if obstacleGrid[row][0] == 1:
            table[row][0] = 0 
        else:
            table[row][0] = table[row-1][0]
    #Now do the main traversal 
    for row in range(1, len(obstacleGrid)): 
        for col in range(1, len(obstacleGrid[0])): 
            if obstacleGrid[row][col] == 1:
                table[row][col] = 0 
            else:
                table[row][col] = table[row-1][col] + table[row][col-1]

###Optimization
######Min path sum
grid = [[1,3,1],[1,5,1],[4,2,1]]

"""
1	3	1
1	5	1
4	2	1
"""

#grid[0] gives us [1,3,1] and the length of this = number of columns


def minpathsum(grid):
    """
    :type grid: List[List[int]]
    :rtype: int

    """
    """
    1	3	1
    1	5	1
    4	2	1
    """

    table = [ [0 for j in range(len(grid[0]))] for i in range(len(grid))]
    """
    0	0	0
    0	0	0
    0	0	0
    """
    
    #Base cases
    table[0][0] = grid[0][0]
    """
    1	0	0
    0	0	0
    0	0	0
    """
    #Row 0
    for col in range(1,len(grid[0])): #Iterate through columns
        table[0][col] = table[0][col-1] + grid[0][col]
    """
    1	4	5
    0	0	0
    0	0	0
    """
    
    #Column 0
    for row in range(1, len(grid)): #Iterate through rows
        table[row][0] = table[row-1][0] + grid[row][0]
    """
    1	4	5
    2	0	0
    6	0	0
    """
    #General traversal
    for row in range(1,len(grid)):
        for col in range(1, len(grid[0])):
            table[row][col] = grid[row][col] + min(table[row-1][col], table[row][col-1]) #current value of cell + min(row above, column before)
    """
    1	4	5
    2	7	6
    6	8	7
    """
    
    return table[len(grid)-1][len(grid[0])-1]


"""
Dynamic Programming (bottom-up tabulation) on two kinds of problems:
1.(Non-optimization) counting problems
 - Overlapping subproblems
2.(Combinatorial Optimization) problems where we found the "best" sequence
  (one that maximized or minimized some objective function)
 - Overlapping subproblems
 - Optimal substructure (required for correctness)
Both these problems would otherwise (without DP) lead to exponential time
complexity, since the number of possible sequences to consider are far too many.
Caching the results of overlapping subproblems is necessary to curb it.
"""

"""

f(i,j) = min cost from the top-left corner to cell (i,j)
f(i,j) = min[ f(i-1,j), f(i,j-1) ] + cost of cell (i,j)

f(i) = min cost of starting from below and climbing up to stair i
f(i) = min over all preceding steps j [ f(i) ] + cost of stair i

f(a) = min number of coins needed to make up amount a
f(a) = min [f(a - c(of i)] (for all coin denominations c(of i)) + 1

f(r,k) = min cost path from the top tip of the triangle to row r, entry k
f(r,k) = min [f(r-1,k) + f(r-1,k-1) ] + cost of cell (r,k)

f(i) = maximum amount of money you can rob from houses O..i
f(i) = max [f(n-2) + cash in house i, f(n-1) ]
(for both versions of the house robbery problem)

f(i) = min cost itinerary for day[0]…...dayli] (note: the travel days may not be contiguous)
f(i) = min [ f(i-1) + cost of ending 1-day pass, f(j) + cost of ending 7-day pass, f(k) +
cost of ending 30-day pass] where j,k are the rightmost days not covered by the
ending 7-day/30-day pass
"""

###Rod Breaking
n = 4
lengths = [1,2,3,4,5,6,7,8,9,10]
prices = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]

Integer array of rod length + 1

def rodcutting (n, lengths, prices):
    #n = length of the original rod #lengths and prices are the price values for rods of lengths 1, 2, 3, 4, ... which could go well beyond the length n
    if n == 0 :
        return 0 
    if n == 1:
        return prices[0]
    
    table = [0 for _ in range(n+1)] 
    table[0] = 0 
    table[1] = prices[0]
    
    #In general, if a rod has length i, then we focus on the last piece of it. 
    #What could the length of the last piece be? 
    #It no longer has a constant number of choices. It could vary from 1 to i itself 
    #Let's treat the case where we don't cut the rod at all to be the default, and see if we can do better 
    #So we will vary the length of the last cut piece from 1 to i-1
    
    for i in range(2, n+1):        
        #Need to compute and set value of table[i] 
        best = prices[i-1] #prices array is zero indexed 
        for cutlength in range(1, i): 
            if prices[cutlength-1] + table[i-cutlength] > best:
                best = prices[cutlength-1] + table[i-cutlength] 
        table[i] = best
    return table[n]
    
print(rodcutting (4, [1,2,3,4,5,6,7,8,9,10],[1, 5, 8, 9, 10, 17, 17, 20, 24, 30]))


for i in range(2,len(price)+1):
    print(f"i:{i}")
    maxi = 0
    for cutlength in range(0,i):
        print(f"cutlength:{cutlength}")

price = [1,5,8,9]

def get_maximum_profit(price):
    if len(price) <= 0:
       return 0
       
    new_price = [0]
    for p in price:
        new_price.append(p)
            
    
    for i in range(2,len(price)+1):
        maxi = 0
        for cutlength in range(0,i):
            temp = 0
            temp = new_price[cutlength] + new_price[i-cutlength]
            if temp > maxi:
                maxi = temp
        
        new_price[i] = maxi
    
    return new_price[len(price)]

get_maximum_profit(price)

 def rodcutting (lengths, prices):   
    table = [0 for _ in range(n+1)] 
    table[0] = prices[0] 
    table[1] = prices[1]
    for length in range(2, n+1):    
    
       table = []
       for p in price:
            table.append(p)
        
        
def rodcutting (n, lengths, prices):
    #n = length of the original rod #lengths and prices are the price values for rods of lengths 1, 2, 3, 4, ... which could go well beyond the length n
    if n == 0 :
        return 0 
    if n == 1:
        return prices[0]
    
    table = [0 for _ in range(n+1)] 
    table[0] = 0 
    table[1] = prices[0]
    
    #In general, if a rod has length i, then we focus on the last piece of it. 
    #What could the length of the last piece be? 
    #It no longer has a constant number of choices. It could vary from 1 to i itself 
    #Let's treat the case where we don't cut the rod at all to be the default, and see if we can do better 
    #So we will vary the length of the last cut piece from 1 to i-1
    
    for i in range(2, n+1):        
        #Need to compute and set value of table[i] 
        best = prices[i-1] #prices array is zero indexed 
        for cutlength in range(1, i): 
            if prices[cutlength-1] + table[i-cutlength] > best:
                best = prices[cutlength-1] + table[i-cutlength] 
        table[i] = best
    return table[n]     

	
#recursvie case naive
#Time complexity: O(2^N)
#Space complexity O(N)
def fib(n):
    #base case
    if n <=1 :
        return 1
    if n == 1:
        return 1
    #recursive case
    return fib(n-1) + fib(n -2)


fib(5)

n = 5

#Bottom-Up Approach using Memoization
#Time complexity: O(N)
#Space complexity O(N)
def fib(n):
    if n <= 1:
        return n
    
    cache = [0] * (n + 1)
    cache[0] = 1
    cache[1] = 1
    for i in range(2, n + 1):
        cache[i] = cache[i - 1] + cache[i - 2]

    return cache[n]

#Top-Down Approach using Memoization
#Time complexity: O(N)
#Space complexity O(N)
	
cache = {0: 1, 1: 1}
def fib(n):
    if n in cache:
        return cache[n]
    cache[n] = cache(n - 1) + cache(n - 2)
    return cache[n]

#Iterative Bottom-Up Approach (Reusing space)
#Time complexity: O(N)
#Space complexity O(1)
def fib(n):
    if (n <= 1):
        return n

    current = 0
    prev1 = 1
    prev2 = 1

    # Since range is exclusive and we want to include n, we need to put n+1.
    for i in range(2, n + 1):
        current = prev1 + prev2
        prev2 = prev1
        prev1 = current
    return current

#There are log n solutions as well refer https://leetcode.com/problems/fibonacci-number/solution/ Approach 5: Matrix Exponentiation


 
