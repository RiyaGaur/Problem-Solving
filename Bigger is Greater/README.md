Lexicographical order is often known as alphabetical order when dealing with strings. A string is greater than another string if it comes later in a lexicographically sorted list.

Given a word, create a new word by swapping some or all of its characters. This new word must meet two criteria:
<ul>
    <li>It must be greater than the original word</li>
    <li>It must be the smallest word that meets the first condition</li>
</ul>
For example, given the word w= abcd, the next largest word is abdc.

Complete the function biggerIsGreater below to create and return the new string meeting the criteria. If it is not possible, return no answer.

<h2>Function Description</h2>

Complete the biggerIsGreater function in the editor below. It should return the smallest lexicographically higher string possible from the given string or no answer.

biggerIsGreater has the following parameter(s):
<ul>
    <li>w: a string</li>
</ul>

<h2>Input Format</h2>

The first line of input contains T, the number of test cases.
Each of the next T lines contains w.

<h2>Constraints</h2>
<ul>
    <li> 1 <= T <= 10^5 </li>
    <li> 1 <= |w| <= 100 </li>
    <li> w will contain only letters in the range ascii[a..z].</li>
</ul>

<h2>Output Format</h2>

For each test case, output the string meeting the criteria. If no answer exists, print no answer.

<h2>Sample Input 0</h2>

5<br>
ab<br>
bb<br>
hefg<br>
dhck<br>
dkhc

<h2>Sample Output 0</h2>

ba<br>
no answer<br>
hegf<br>
dhkc<br>
hcdk
