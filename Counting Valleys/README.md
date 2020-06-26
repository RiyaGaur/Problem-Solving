Gary is an avid hiker. He tracks his hikes meticulously, paying close attention to small details like topography. During his last hike he took exactly n steps. For every step he took, he noted if it was an uphill, U, or a downhill,D step. Gary's hikes start and end at sea level and each step up or down represents a 1 unit change in altitude. We define the following terms:
<ul>
    <li> A mountain is a sequence of consecutive steps above sea level, starting with a step up from sea level and ending with a step down to sea level. </li>
    <li> A valley is a sequence of consecutive steps below sea level, starting with a step down from sea level and ending with a step up to sea level. </li>
</ul>
Given Gary's sequence of up and down steps during his last hike, find and print the number of valleys he walked through.

For example, if Gary's path is s=[DDUUUUDD], he first enters a valley 2 units deep. Then he climbs out an up onto a mountain 2 units high. Finally, he returns to sea level and ends his hike.

<h2> Function Description</h2>

Complete the countingValleys function in the editor below. It must return an integer that denotes the number of valleys Gary traversed.

countingValleys has the following parameter(s):
<ul>
    <li> n: the number of steps Gary takes <li>
    <li> s: a string describing his path <li>
</ul>

<h2> Input Format</h2>

The first line contains an integer n, the number of steps in Gary's hike.
The second line contains a single string s, of n characters that describe his path.

<h2> Constraints</h2>
<ul>
    <li> 2 <= n <= 10^6 </li>
    <li> s[i] belongs to {UD} </li>
</ul>

<h2> Output Format</h2>

Print a single integer that denotes the number of valleys Gary walked through during his hike.

<h2> Sample Input</h2>

8<br>
UDDDUDUU

<h2> Sample Output</h2>

1
