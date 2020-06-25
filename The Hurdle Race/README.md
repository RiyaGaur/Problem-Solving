Dan is playing a video game in which his character competes in a hurdle race. Hurdles are of varying heights, and Dan has a maximum height he can jump. There is a magic potion he can take that will increase his maximum height by 1 unit for each dose. How many doses of the potion must he take to be able to jump all of the hurdles.

Given an array of hurdle heights height, and an initial maximum height Dan can jump,k, determine the minimum number of doses Dan must take to be able to clear all the hurdles in the race.

For example, if height=[1,2,3,3,2] and Dan can jump 1 unit high naturally, he must take 3-2=1 doses of potion to be able to jump all of the hurdles.

<h2>Function Description</h2>

Complete the hurdleRace function in the editor below. It should return the minimum units of potion Dan needs to drink to jump all of the hurdles.

hurdleRace has the following parameter(s):
<ul>
    <li>k: an integer denoting the height Dan can jump naturally</li>
    <li>height: an array of integers denoting the heights of each hurdle</li>
</ul>

<h2>Input Format</h2>

The first line contains two space-separated integers n and k, the number of hurdles and the maximum height Dan can jump naturally.
The second line contains n space-separated integers height[i] where 0 <= i <n.

<h2>Constraints</h2>
<ul>
    <li>1 <= n,k  <= 100 </li>
    <li>1 <= height[i]  <= 100 </li>
</ul>

<h2>Output Format</h2>

Print an integer denoting the minimum doses of magic potion Dan must drink to complete the hurdle race.

<h2>Sample Input 0</h2>

5 4<br>
1 6 3 5 2

<h2>Sample Output 0</h2>

2
