Given an array of integers, find and print the maximum number of integers you can select from the array such that the absolute difference between any two of the chosen integers is less than or equal to 1. For example, if your array is a=[1,1,2,2,4,4,5,5,5], you can create two subarrays meeting the criterion:[1,1,2,2] and [4,4,5,5,5]. The maximum length subarray has 5 elements.

<h2>Function Description</h2>

Complete the pickingNumbers function in the editor below. It should return an integer that represents the length of the longest array that can be created.

pickingNumbers has the following parameter(s):
<ul>
    <li> a: an array of integers </li>
</ul>

<h2>Input Format</h2>

The first line contains a single integer n, the size of the array a.
The second line contains n space-separated integers a[i].

<h2>Constraints</h2>
<ul>
    <li> 2 <= n <= 100 </li>
    <li> 0 <= a[i] < 100 </li>
    <li>The answer will be <= 2. </li>
</ul>

<h2>Output Format</h2>

A single integer denoting the maximum number of integers you can choose from the array such that the absolute difference between any two of the chosen integers is <= 1.

<h2>Sample Input 0</h2>

6<br>
4 6 5 3 3 1

<h2>Sample Output 0</h2>

3
