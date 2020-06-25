We say that a string contains the word hackerrank if a subsequence of its characters spell the word hackerrank. For example, if string s= haacckkerrannkk it does contain hackerrank, but s= haacckkerannkk does not. In the second case, the second r is missing. If we reorder the first string as hccaakkerrannkk, it no longer contains the subsequence due to ordering.

More formally, let p[0],p[1],...,p[9] be the respective indices of h, a, c, k, e, r, r, a, n, k in string . If p[0] < p[1] < p[2] < ... < p[9] is true, then s contains hackerrank.

For each query, print YES on a new line if the string contains hackerrank, otherwise, print NO.

<h2>Function Description</h2>

Complete the hackerrankInString function in the editor below. It must return YES or NO.

hackerrankInString has the following parameter(s):
<ul>
    <li>s: a string</li>
</ul>
<h2>Input Format</h2>

The first line contains an integer q, the number of queries.
Each of the next q lines contains a single query string s.

<h2>Constraints</h2>
<ul>
    <li> 2 <= q <= 10^2 </li>
    <li> 10 <= |s| <= 10^4 </li>
</ul>

<h2>Output Format</h2>

For each query, print YES on a new line if s contains hackerrank, otherwise, print NO.

<h2>Sample Input 0</h2>

2<br>
hereiamstackerrank<br>
hackerworld

<h2>Sample Output 0</h2>

YES<br>
NO
