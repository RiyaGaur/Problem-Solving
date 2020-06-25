HackerLand Enterprise is adopting a new viral advertising strategy. When they launch a new product, they advertise it to exactly 5 people on social media.

On the first day, half of those 5 people (i.e.,floor(5/1)=2) like the advertisement and each shares it with 3 of their friends. At the beginning of the second day, floor(5/2) X 3 = 2 X 3 =6 people receive the advertisement.

Each day,floor(recipients/2) of the recipients like the advertisement and will share it with 3 friends on the following day. Assuming nobody receives the advertisement twice, determine how many people have liked the ad by the end of a given day, beginning with launch day as day 1.

For example, assume you want to know how many have liked the ad by the end of the 5th day.

Day Shared Liked Cumulative<br>
1      5     2       2<br>
2      6     3       5<br>
3      9     4       9<br>
4     12     6      15<br>
5     18     9      24

The cumulative number of likes is 24.

<h2>Function Description</h2>

Complete the viralAdvertising function in the editor below. It should return the cumulative number of people who have liked the ad at a given time.

viralAdvertising has the following parameter(s):
<ul>
    <li> n: the integer number of days </li>
</ul>

<h2>Input Format</h2>

A single integer,n, denoting a number of days.

<h2>Constraints</h2>
<ul>
    <li> 1 <= n <= 50 </li>
</ul>

<h2>Output Format</h2>

Print the number of people who liked the advertisement during the first n days.

<h2>Sample Input</h2>

3

<h2>Sample Output</h2>

9
