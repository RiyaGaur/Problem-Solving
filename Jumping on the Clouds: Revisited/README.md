Aerith is playing a cloud hopping game. In this game, there are sequentially numbered clouds that can be thunderheads or cumulus clouds. Her character must jump from cloud to cloud until it reaches the start again.

To play, Aerith is given an array of clouds,c and an energy level e=100. She starts from c[0] and uses 1 unit of energy to make a jump of size k to cloud c[( i + k )% n]. If Aerith lands on a thundercloud,c[i]=1, her energy (e) decreases by 2 additional units. The game ends when Aerith lands back on cloud 0.

Given the values of n, k, and the configuration of the clouds as an array c, can you determine the final value of e after the game ends?

For example, give c=[0,0,1,0] and k=2, the indices of her path are 0-->2-->0. Her energy level reduces by 1 for each jump to 98. She landed on one thunderhead at an additional cost of 2 energy units. Her final energy level is 96.

Note: Recall that % refers to the modulo operation. In this case, it serves to make the route circular. If Aerith is at c[n-1] and jumps 1, she will arrive at c[0].

<h2> Function Description </h2>

Complete the jumpingOnClouds function in the editor below. It should return an integer representing the energy level remaining after the game.

jumpingOnClouds has the following parameter(s):
<ul>
    <li> c: an array of integers representing cloud types </li>
    <li> k: an integer representing the length of one jump </li>
</ul>

<h2> Input Format </h2>

The first line contains two space-separated integers,n and k, the number of clouds and the jump distance.
The second line contains n space-separated integers c[i] where 0 <= i < n. Each cloud is described as follows:
<ul>
    <li> If c[i] = 0, then cloud  is a i cumulus cloud.</li>
    <li> If c[i] = 1, then cloud  is a i thunderhead.</li>
</ul>

<h2> Constraints </h2>
<ul>
    <li> 2 <= n <= 25 </li>
    <li> 1 <= k <= n </li>
    <li> n % k = 0 </li>
    <li> c[i] belongs to {0,1} </li>
</ul>

<h2> Output Format </h2>

Print the final value of e on a new line.

<h2> Sample Input </h2>

8 2<br>
0 0 1 0 0 1 1 0

<h2> Sample Output </h2>

92
