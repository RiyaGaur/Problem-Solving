An integer d is a divisor of an integer n if the remainder of n/d=0.

Given an integer, for each digit that makes up the integer determine whether it is a divisor. Count the number of divisors occurring within the integer.

<strong>Note:</strong> Each digit is considered to be unique, so each occurrence of the same digit should be counted (e.g. for n=111,1 is a divisor of 111 each time it occurs so the answer is 3).

<h2>Function Description</h2>

Complete the findDigits function in the editor below. It should return an integer representing the number of digits of d that are divisors of d.

findDigits has the following parameter(s):
<ul>
    <li>n: an integer to analyze</li>
</ul>
<h2>Input Format</h2>

The first line is an integer,t, indicating the number of test cases.
The t subsequent lines each contain an integer,n.

<h2>Constraints</h2>
<ul>
    <li> 1 <= t <= 15 </li>
    <li> 0 < n < 10^9 </li>
</ul>

<h2>Output Format</h2>

For every test case, count the number of digits in n that are divisors of n. Print each answer on a new line.

<h2>Sample Input</h2>

2<br>
12<br>
1012

<h2>Sample Output</h2>

2<br>
3
