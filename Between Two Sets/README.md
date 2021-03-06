You will be given two arrays of integers and asked to determine all integers that satisfy the following two conditions:
<ol>
    <li> The elements of the first array are all factors of the integer being considered  </li>
    <li> The integer being considered is a factor of all elements of the second array </li>
</ol>
These numbers are referred to as being between the two arrays. You must determine how many such numbers exist.

For example, given the arrays a=[2,6] and b=[24,36], there are two numbers between them: 6 and 12. 6 % 2 = 0, 6 % 6 = 0 , 24 % 6 = 0 and 36 % 6 = 0 for the first value. Similarly, 12 % 2 = 0, 12 % 6 = 0 and 24 % 12 = 0, 36 % 12 = 0.

<h2> Function Description </h2>

Complete the getTotalX function in the editor below. It should return the number of integers that are betwen the sets.

getTotalX has the following parameter(s):
<ul>
    <li> a: an array of integers </li>
    <li> b: an array of integers </li>
</ul>
<h2> Input Format </h2>

The first line contains two space-separated integers, n and m, the number of elements in array a and the number of elements in array b.
The second line contains n distinct space-separated integers describing a[i] where 0 <= i < n.
The third line contains m distinct space-separated integers describing b[j] where 0 <= j < m.

<h2> Constraints </h2>
<ul>
    <li> 1 <= n,m <= 10 </li>
    <li> 1 <= a[i] <= 100 </li>
    <li> 1 <= b[j] <= 100 </li>
</ul>
<h2> Output Format </h2>

Print the number of integers that are considered to be between a and b.

<h2> Sample Input </h2>

2 3 <br>
2 4 <br>
16 32 96

<h2> Sample Output </h2>

3
