You are choreographing a circus show with various animals. For one act, you are given two kangaroos on a number line ready to jump in the positive direction (i.e, toward positive infinity).
<ul>
    <li>The first kangaroo starts at location x1 and moves at a rate of v1 meters per jump.</li>
    <li>The second kangaroo starts at location x2 and moves at a rate of v2 meters per jump.</li>
</ul>
You have to figure out a way to get both kangaroos at the same location at the same time as part of the show. If it is possible, return YES, otherwise return NO.

For example, kangaroo 1 starts at x1=2 with a jump distance v1=1 and kangaroo 2 starts at x2=1 with a jump distance of v2=2. After one jump, they are both at x=3,(x1 + v1 = 2 + 1,x2 + 2 = 1 + 2 ), so our answer is YES.

<h2>Function Description</h2>

Complete the function kangaroo in the editor below. It should return YES if they reach the same position at the same time, or NO if they don't.

kangaroo has the following parameter(s):
<ul>
    <li>  x1, v1: integers, starting position and jump distance for kangaroo 1 </li>
    <li>  x2, v2: integers, starting position and jump distance for kangaroo 2 </li>
</ul>
<h2>Input Format</h2>

A single line of four space-separated integers denoting the respective values of x1,v1,x2 and v2.

<h2>Constraints</h2>
<ul>
    <li> 0 <= x1 < x2 <= 10000</li>
    <li> 1 <= v1 <= 10000</li>
    <li> 1 <= v2 <= 10000</li>
</ul>
<h2>Output Format</h2>

Print YES if they can land on the same location at the same time; otherwise, print NO.

<strong>Note:</strong> The two kangaroos must land at the same location after making the same number of jumps.

<h2>Sample Input 0</h2>

0 3 4 2
<h2>Sample Output 0</h2>

YES
