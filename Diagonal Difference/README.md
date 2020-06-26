Given a square matrix, calculate the absolute difference between the sums of its diagonals.

For example, the square matrix arr is shown below:

1  2  3<br>
4  5  6<br>
9  8  9  

The left-to-right diagonal = 1+ 5 + 9 = 15. The right to left diagonal = 3 + 5 + 9 = 17. Their absolute difference is |15-17|=2.

<h2> Function description </h2>

Complete the diagonalDifference function in the editor below. It must return an integer representing the absolute diagonal difference.

diagonalDifference takes the following parameter:
<ul>
    <li> arr: an array of integers. </li>
</ul>

<h2> Input Format </h2>

The first line contains a single integer, n, the number of rows and columns in the matrix arr.
Each of the next n lines describes a row, arr[i], and consists of n space-separated integers arr[i][j].

<h2> Constraints </h2>
<ul>
    <li> -100 <= arr[i][j] <= 100 </li>
</ul>
<h2> Output Format </h2>

Print the absolute difference between the sums of the matrix's two diagonals as a single integer.

<h2> Sample Input </h2>

3<br>
11 2 4<br>
4 5 6<br>
10 8 -12

<h2> Sample Output </h2>

15
