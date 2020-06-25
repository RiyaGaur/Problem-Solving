John Watson knows of an operation called a right circular rotation on an array of integers. One rotation operation moves the last array element to the first position and shifts all remaining elements right one. To test Sherlock's abilities, Watson provides Sherlock with an array of integers. Sherlock is to perform the rotation operation a number of times then determine the value of the element at a given position.

For each array, perform a number of right circular rotations and return the value of the element at a given index.

For example, array a=[3,4,5], number of rotations,k=2  and indices to check,m=[1,2] .

First we perform the two rotations:

[3,4,5] --> [5,3,4] --> [4,5,3]

Now return the values from the zero-based indices 1 and 2 as indicated in the m array.

a[1]=5<br>
a[2]=3

<h2>Function Description</h2>

Complete the circularArrayRotation function in the editor below. It should return an array of integers representing the values at the specified indices.

circularArrayRotation has the following parameter(s):
<ul>
    <li> a: an array of integers to rotate</li>
    <li> k: an integer, the rotation count</li>
    <li> queries: an array of integers, the indices to report</li>
</ul>

<h2>Input Format</h2>

The first line contains 3 space-separated integers, n, k, and q, the number of elements in the integer array, the rotation count and the number of queries.
The second line contains n space-separated integers, where each integer i describes array element a[i] (where 0 <= i < n).
Each of the q subsequent lines contains a single integer denoting m, the index of the element to return from a.

<h2>Constraints</h2>
<ul>
    <li> 1 <= n <= 10^5 </li>
    <li> 1 <= a[i] <= 10^5 </li>
    <li> 1 <= k <= 10^5 </li>
    <li> 1 <= q <= 500 </li>
    <li> 0 <= m <= n </li>
</ul>
<h2>Output Format</h2>

For each query, print the value of the element at index m of the rotated array on a new line.

<h2>Sample Input 0</h2>

3 2 3<br>
1 2 3<br>
0<br>
1<br>
2

<h2>Sample Output 0</h2>

2<br>
3<br>
1
