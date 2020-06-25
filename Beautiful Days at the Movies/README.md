Lily likes to play games with integers. She has created a new game where she determines the difference between a number and its reverse. For instance, given the number 12, its reverse is 21. Their difference is 9. The number 120 reversed is 21, and their difference is 99.

She decides to apply her game to decision making. She will look at a numbered range of days and will only go to a movie on a beautiful day.

Given a range of numbered days,[i...j] and a number k, determine the number of days in the range that are beautiful. Beautiful numbers are defined as numbers where |i-reverse(i)| is evenly divisible by k. If a day's value is a beautiful number, it is a beautiful day. Print the number of beautiful days in the range.

<h2>Function Description</h2>

Complete the beautifulDays function in the editor below. It must return the number of beautiful days in the range.

beautifulDays has the following parameter(s):
<ul>
    <li>i: the starting day number</li>
    <li>j: the ending day number</li>
    <li>k: the divisor</li>
</ul>

<h2>Input Format</h2>

A single line of three space-separated integers describing the respective values of i,j, and k.

<h2>Constraints</h2>
<ul>
    <li> 1 <= i <= j <= 2 X 10^6  </li>
    <li> 1 <= k <= 2 X 10^9  </li>
</ul>

<h2>Output Format</h2>

Print the number of beautiful days in the inclusive range between i and j.

<h2>Sample Input</h2>

20 23 6

<h2>Sample Output</h2>

2
