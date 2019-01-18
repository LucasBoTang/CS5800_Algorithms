# CS5800 Algorithms Progamming Assignment

## Assignment1: Protecting Boston

Boston has n buildings and m one way roads between the buildings. You have been selected to build fire departments in Boston in order to keep Boston safe from fire.

Fire departments can only be built where a building already exists. In case of a fire, the firetruck must leave the fire department and go back to the same location it left. So a single fire department i can protect buildings j where the fire truck can go from i to j, and back from j to i (and the fire department can protect itself as well).

To build a fire department at a building location, we need to destroy that building first and build a fire department at its place. Each building you destroy has a cost, and your task is to minimize that cost while protecting all of Boston from fire.

Example:

![Example](https://github.com/Apocrypse/CS5800_Algorithms/blob/master/pa1_example.png?raw=true)

Building a fire department in building 1 would protect buildings 1, 2 and 3. Building a fire department in building 2 would protect buildings 1, 2 and 3. Building a fire department in building 3 would protect buildings 1, 2 and 3. Building a fire department in building 4 would protect building 4.

So to protect all Boston with minimum cost, we should build a fire department in building 2, and one in building 4 with a total cost of 5.

Note that even if the fire truck leaving from building 2 can reach building 4, it cannot return back to its original place, so building 4 is not protected when building a fire department at building 2.

The first Sample below (Sample 0), is this example explained above.

Input Format

The first line will be n, the number of buildings in Boston 1<= n <= 10^5. The second line has n space separated integers. The ith integer is the cost of destroying the ith building in Boston. The cost of the building Ci will be 1<= Ci <= 10^9.

The third line will be m, the number of one way roads in Boston 0<= m <= 3*10^5. Each of the next m lines will contain a pair ui and vi where 1<= ui, vi <=n and ui!=vi. A pair ui, vi means there is a one way road from building ui to building vi. There will be at most 1 road between 2 buildings in the same direction.

Constraints

1<= n <= 10^5 1<= Ci <= 10^9 0<= m <= 3*10^5

Output Format

Print 1 integer: the minimum cost of securing all Boston from fire.
