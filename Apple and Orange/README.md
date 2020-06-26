Sam's house has an apple tree and an orange tree that yield an abundance of fruit. In the diagram below, the red region denotes his house, where s is the start point, and t is the endpoint. The apple tree is to the left of his house, and the orange tree is to its right. You can assume the trees are located on a single point, where the apple tree is at point a, and the orange tree is at point b.

Apple and orange(2).png

When a fruit falls from its tree, it lands d units of distance from its tree of origin along the x-axis. A negative value of d means the fruit fell d units to the tree's left, and a positive value of d means it falls d units to the tree's right.

Given the value of d for m apples and n oranges, determine how many apples and oranges will fall on Sam's house (i.e., in the inclusive range [s,t])?

For example, Sam's house is between s=7 and t=10. The apple tree is located at a=4 and the orange at b=12. There are m=3 apples and n=3 oranges. Apples are thrown apples=[2,3,-4] units distance from a, and oranges=[3,-2,-2] units distance. Adding each apple distance to the position of the tree, they land at [4 + 2,4 + 3,4 + =4]. Oranges land at [12 + 3, 12 + -2,12 + -4]=[15,10,8]. One apple and two oranges land in the inclusive range 7 - 10 so we print

1<br>
2

<h2>Function Description</h2>

Complete the countApplesAndOranges function in the editor below. It should print the number of apples and oranges that land on Sam's house, each on a separate line.

countApplesAndOranges has the following parameter(s):
<ul>
    <li>s: integer, starting point of Sam's house location.</li>
    <li>t: integer, ending location of Sam's house location.</li>
    <li>a: integer, location of the Apple tree.</li>
    <li>b: integer, location of the Orange tree.</li>
    <li>apples: integer array, distances at which each apple falls from the tree.</li>
    <li>oranges: integer array, distances at which each orange falls from the tree.</li>
</ul>

<h2>Input Format</h2>

The first line contains two space-separated integers denoting the respective values of s and t.
The second line contains two space-separated integers denoting the respective values of a and b.
The third line contains two space-separated integers denoting the respective values of m and n.
The fourth line contains m space-separated integers denoting the respective distances that each apple falls from point a.
The fifth line contains n space-separated integers denoting the respective distances that each orange falls from point b.

<h2>Constraints</h2>
<ul>
    <li> 1 <= s,t,a,b,m,n <= 10^5 </li>
    <li> -10^5 <= d <= 10^5 </li>
    <li> a < s < t < b </li>
</ul>

<h2>Output Format</h2>

Print two integers on two different lines:
<ol>
    <li> The first integer: the number of apples that fall on Sam's house. </li>
    <li> The second integer: the number of oranges that fall on Sam's house. </li>
</ol>
<h2>Sample Input 0</h2>

7 11 <br>
5 15 <br>
3 2 <br>
-2 2 1 <br>
5 -6

<h2>Sample Output 0</h2>

1 <br>
1