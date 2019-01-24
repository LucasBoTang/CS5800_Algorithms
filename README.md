# CS5800 Algorithms Progamming Assignment

## Assignment1: Protecting Boston

Boston has n buildings and m one way roads between the buildings. You have been selected to build fire departments in Boston in order to keep Boston safe from fire.

Fire departments can only be built where a building already exists. In case of a fire, the firetruck must leave the fire department and go back to the same location it left. So a single fire department i can protect buildings j where the fire truck can go from i to j, and back from j to i (and the fire department can protect itself as well).

To build a fire department at a building location, we need to destroy that building first and build a fire department at its place. Each building you destroy has a cost, and your task is to minimize that cost while protecting all of Boston from fire.

### Example:

![Example](https://github.com/Apocrypse/CS5800_Algorithms/blob/master/pa1_example.png?raw=true)

Building a fire department in building 1 would protect buildings 1, 2 and 3. Building a fire department in building 2 would protect buildings 1, 2 and 3. Building a fire department in building 3 would protect buildings 1, 2 and 3. Building a fire department in building 4 would protect building 4.

So to protect all Boston with minimum cost, we should build a fire department in building 2, and one in building 4 with a total cost of 5.

Note that even if the fire truck leaving from building 2 can reach building 4, it cannot return back to its original place, so building 4 is not protected when building a fire department at building 2.

The first Sample below (Sample 0), is this example explained above.

### Input Format

The first line will be n, the number of buildings in Boston 1<= n <= 10^5. The second line has n space separated integers. The ith integer is the cost of destroying the ith building in Boston. The cost of the building Ci will be 1<= Ci <= 10^9.

The third line will be m, the number of one way roads in Boston 0<= m <= 3*10^5. Each of the next m lines will contain a pair ui and vi where 1<= ui, vi <=n and ui!=vi. A pair ui, vi means there is a one way road from building ui to building vi. There will be at most 1 road between 2 buildings in the same direction.

### Constraints

1<= n <= 10^5 1<= Ci <= 10^9 0<= m <= 3*10^5

### Output Format

Print 1 integer: the minimum cost of securing all Boston from fire.

### Sample Input 0

'''
4
5 3 4 2
4
1 2
2 3
3 1
3 4
'''

### Sample Output 0

'''
5
'''

### Sample Input 1

'''
10
8 1 3 9 5 7 3 9 9 9
10
5 8
1 10
4 1
6 10
7 3
6 4
5 10
3 6
4 9
3 5
'''

### Sample Output 1

'''
63
'''

## Assignment2: Fun with the Fellowship

Legolas, Gimli and Aragorn have just fought an army of orcs and now want to relax for the day. Their way of having fun is to play an archery contest with Legolas trying to hit any object that the other two point to. However, Aragorn soon realises that Legolas is too good for this game. He adds a twist to the game. Aragorn will now point to 4 targets and assign some number of points (a,b,c,d) to those 4 targets - the points will be unique for each target. Gimli will then give Legolas a number n and Legolas has to tell how many ways he can hit any of those 4 targets one after the other in any order so that the total points scored will be n. Now Legolas is a genius in archery but he's stumped by this question. Help Legolas!

You have to print the answer modulo 1000000007 (10^9+7).

### Input Format

There is only one line in input with 5 space-separated integers - a b c d n

The last 3 test cases are for Extra Credit.

### Constraints

1 <= a,b,c,d <= 10 and a,b,c,d are unique 1 <= n <= 10^5 For extra credit: 1 <= n <= 10^18

### Output Format

Print the number of ways Legolas can get to the target number modulo 1000000007 (10^9+7). If it is impossible, print 0.

### Sample Input 0

'''
2 3 5 7 8
'''

### Sample Output 0

'''
6
...

### Explanation 0

The 6 ways of scoring a total of 8 are (2 + 2 + 2 + 2), (2 + 3 + 3), (3 + 2 + 3), (3 + 3 + 2), (3 + 5), and (5 + 3).
