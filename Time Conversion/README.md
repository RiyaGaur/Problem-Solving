Given a time in 12-hour AM/PM format, convert it to military (24-hour) time.

<strong>Note:</strong> Midnight is 12:00:00AM on a 12-hour clock, and 00:00:00 on a 24-hour clock. Noon is 12:00:00PM on a 12-hour clock, and 12:00:00 on a 24-hour clock.

<h2>Function Description</h2>

Complete the timeConversion function in the editor below. It should return a new string representing the input time in 24 hour format.

timeConversion has the following parameter(s):
<ul>
    <li>s: a string representing time in 12 hour format</li>
</ul>

<h2>Input Format</h2>

A single string s containing a time in 12-hour clock format (i.e.:hh:mm:ssAM or hh:mm:ssPM), where 01 <= hh <= 12 and 00 <= mm , ss<=59.

<h2>Constraints</h2>

All input times are valid

<h2>Output Format</h2>

Convert and print the given time in 24-hour format, where 00 <= hh <= 23.

<h2>Sample Input 0</h2>

07:05:45PM

<h2>Sample Output 0</h2>

19:05:45
