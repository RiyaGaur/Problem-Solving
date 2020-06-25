Two cats and a mouse are at various positions on a line. You will be given their starting positions. Your task is to determine which cat will reach the mouse first, assuming the mouse doesn't move and the cats travel at equal speed. If the cats arrive at the same time, the mouse will be allowed to move and it will escape while they fight.

You are given q queries in the form of x,y, and z representing the respective positions for cats A and B, and for mouse C. Complete the function catAndMouse to return the appropriate answer to each query, which will be printed on a new line.
<ul>
    <li> If cat A catches the mouse first, print Cat A.</li>
    <li> If cat B catches the mouse first, print Cat B.</li>
    <li> If both cats reach the mouse at the same time, print Mouse C as the two cats fight and mouse escapes.</li>
</ul>

For example, cat A is at position x=2 and cat B is at y=5. If mouse C is at position z=4, it is 2 units from cat A and 1 unit from cat B. Cat B will catch the mouse.

<h2>Function Description</h2>

Complete the catAndMouse function in the editor below. It should return one of the three strings as described.

catAndMouse has the following parameter(s):
<ul>
    <li>x: an integer, Cat A's position</li>
    <li>y: an integer, Cat B's position</li>
    <li>z: an integer, Mouse C's position</li>
</ul>
<h2>Input Format</h2>

The first line contains a single integer,q, denoting the number of queries.
Each of the q subsequent lines contains three space-separated integers describing the respective values of x(cat A's location), y(cat B's location), and z(mouse C's location).

<h2>Constraints</h2>
<ul>
    <li> 1 <= q <= 100 </li>
    <li> 1 <= x,y,z <= 100 </li>
</ul>

<h2>Output Format</h2>

For each query, return Cat A if cat A catches the mouse first, Cat B if cat B catches the mouse first, or Mouse C if the mouse escapes.

<h2>Sample Input 0</h2>

2<br>
1 2 3<br>
1 3 2

<h2>Sample Output 0</h2>

Cat B<br>
Mouse C
