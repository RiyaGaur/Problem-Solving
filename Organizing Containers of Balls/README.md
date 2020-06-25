David has several containers, each with a number of balls in it. He has just enough containers to sort each type of ball he has into its own container. David wants to sort the balls using his sort method.

As an example, David has n=2 containers and 2 different types of balls, both of which are numbered from 0 to n-1=1. The distribution of ball types per container are described by an n X n matrix of integers,M[container][type] . 

David wants to perform some number of swap operations such that:
<ul>
    <li> Each container contains only balls of the same type.</li>
    <li> No two balls of the same type are located in different containers.</li>
</ul>
You must perform q queries where each query is in the form of a matrix,M. For each query, print Possible on a new line if David can satisfy the conditions above for the given matrix. Otherwise, print Impossible.

<h2>Function Description</h2>

Complete the organizingContainers function in the editor below. It should return a string, either Possible or Impossible.

organizingContainers has the following parameter(s):
<ul>
    <li> containter: a two dimensional array of integers that represent the number of balls of each color in each container</li>
</ul>

<h2>Input Format</h2>

The first line contains an integer q, the number of queries.

Each of the next q sets of lines is as follows:
<ol>
    <li>The first line contains an integer n, the number of containers (rows) and ball types (columns).</li>
    <li>Each of the next n lines contains n space-separated integers describing row M[i].</li>
</ol>
<ul>
    <li> 1 <= q <= 10 </li>
    <li> 1 <= n <= 100 </li>
    <li> 0 <= M[container][type] <= 10^9 </li>
</ul>
<h2>Constraints</h2>

<h2>Scoring</h2>
<ul>
    <li> For 33% of score, 1 <= n <= 10. </li>
    <li> For 100% of score, 1 <= n <= 100. </li>
</ul>

<h2>Output Format</h2>

For each query, print Possible on a new line if David can satisfy the conditions above for the given matrix. Otherwise, print Impossible.

<h2>Sample Input 0</h2>

2<br>
2<br>
1 1<br>
1 1<br>
2<br>
0 2<br>
1 1

<h2>Sample Output 0</h2>

Possible<br>
Impossible
