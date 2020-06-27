We define a magic square to be an n X n matrix of distinct positive integers from 1 to n^2 where the sum of any row, column, or diagonal of length n is always equal to the same number: the magic constant.

You will be given a 3 X 3 matrix  of integers in the inclusive range [1,9]. We can convert any digit a to any other digit b in the range [1,9] at cost of |a-b|. Given s, convert it into a magic square at minimal cost. Print this cost on a new line.

<strong>Note:</strong> The resulting magic square must contain distinct integers in the inclusive range .

For example, we start with the following matrix s:

5 3 4 <br>
1 5 8 <br>
6 4 2

We can convert it to the following magic square:

8 3 4<br>
1 5 9<br>
6 7 2

This took three replacements at a cost of |5-8|+|8-9|+|4-7|=7.

<h2> Function Description </h2>

Complete the formingMagicSquare function in the editor below. It should return an integer that represents the minimal total cost of converting the input square to a magic square.

formingMagicSquare has the following parameter(s):
<ul>
    <li> s: a 3 X 3 array of integers </li>
</ul>
<h2> Input Format </h2>

Each of the lines contains three space-separated integers of row s[i].

<h2> Constraints </h2>
<ul>
    <li> s[i][j] belongs to [1,9] </li>
</ul>
<h2> Output Format </h2>

Print an integer denoting the minimum cost of turning matrix s into a magic square.

<h2> Sample Input 0 </h2>

4 9 2 <br>
3 5 7 <br>
8 1 5

<h2> Sample Output 0 </h2>

1
