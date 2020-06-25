HackerLand University has the following grading policy:
<ul>
    <li>Every student receives a grade in the inclusive range from 0 to 100.</li>
    <li>Any grade less than 40 is a failing grade.</li>
</ul>
Sam is a professor at the university and likes to round each student's grade according to these rules:
<ul>
    <li>If the difference between the grade and the next multiple of 5 is less than 3, round grade up to the next multiple of 5.</li>
    <li>If the value of grade is less than 38, no rounding occurs as the result will still be a failing grade.</li>
</ul>

For example,grade=84  will be rounded to 85 but rade=29 will not be rounded because the rounding would result in a number that is less than 40.

Given the initial value of grade for each of Sam's n students, write code to automate the rounding process.

<h2>Function Description</h2>

Complete the function gradingStudents in the editor below. It should return an integer array consisting of rounded grades.

gradingStudents has the following parameter(s):
<ul>
    <li>grades: an array of integers representing grades before rounding</li>
 </ul>
 
<h2>Input Format</h2>

The first line contains a single integer,n, the number of students.
Each line i of the n subsequent lines contains a single integer,grades[i], denoting student i's grade.

<h2>Constraints</h2>
<ul>
    <li> 1 <= n <= 60 </li>
    <li> 0 <= grades[i] <= 100 </li>
</ul>

<h2>Output Format</h2>

For each grades[i], print the rounded grade on a new line.

<h2>Sample Input 0</h2>

4<br>
73<br>
67<br>
38<br>
33

<h2>Sample Output 0</h2>

75<br>
67<br>
40<br>
33
