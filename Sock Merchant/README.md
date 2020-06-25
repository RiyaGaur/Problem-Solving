John works at a clothing store. He has a large pile of socks that he must pair by color for sale. Given an array of integers representing the color of each sock, determine how many pairs of socks with matching colors there are.

For example, there are n=7 socks with colors ar=[1,2,1,2,1,3,2]. There is one pair of color 1 and one of color 2. There are three odd socks left, one of each color. The number of pairs is 2.

<h2>Function Description</h2>

Complete the sockMerchant function in the editor below. It must return an integer representing the number of matching pairs of socks that are available.

sockMerchant has the following parameter(s):
<ul>
    <li>n: the number of socks in the pile</li>
    <li>ar: the colors of each sock</li>
</ul>

<h2>Input Format</h2>

The first line contains an integer n, the number of socks represented in ar.
The second line contains n space-separated integers describing the colors ar[i] of the socks in the pile.

<h2>Constraints</h2>
<ul>
    <li> 1 <= n <= 100</li>
    <li> 1 <= ar[i] <= 100 where 0 <=i < n </li>
 </ul>
 
<h2>Output Format</h2>

Return the total number of matching pairs of socks that John can sell.

<h2>Sample Input</h2>

9<br>
10 20 20 10 10 30 50 10 20

<h2>Sample Output</h2>

3
