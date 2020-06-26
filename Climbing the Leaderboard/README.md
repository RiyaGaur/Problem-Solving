Alice is playing an arcade game and wants to climb to the top of the leaderboard and wants to track her ranking. The game uses Dense Ranking, so its leaderboard works like this:
<ul>
    <li> The player with the highest score is ranked number 1 on the leaderboard. </li>
    <li> Players who have equal scores receive the same ranking number, and the next player(s) receive the immediately following ranking number. </li>
</ul>
For example, the four players on the leaderboard have high scores of 100, 90, 90, and 80. Those players will have ranks 1, 2, 2, and 3, respectively. If Alice's scores are 70,80 and 105, her rankings after each game are 4th,3rd and 1st.

<h2> Function Description</h2>

Complete the climbingLeaderboard function in the editor below. It should return an integer array where each element res[j] represents Alice's rank after the jth game.

climbingLeaderboard has the following parameter(s):
<ul>
    <li> scores: an array of integers that represent leaderboard scores</li>
    <li> alice: an array of integers that represent Alice's scores</li>
</ul>
<h2> Input Format</h2>

The first line contains an integer n, the number of players on the leaderboard.
The next line contains n space-separated integers scores[i], the leaderboard scores in decreasing order.
The next line contains an integer, m, denoting the number games Alice plays.
The last line contains m space-separated integers alice[j], the game scores.

<h2> Constraints</h2>
<ul>
    <li> 1 <= n <= 2 X 10^5 </li>
    <li> 1 <= m <= 2 X 10^5 </li>
    <li> 0 <= scores[i] <= 10^9 for 0 <= i < n </li>
    <li> 0 <= alice[j] <= 10^9 for 0 <= j < m  </li>
    <li>The existing leaderboard, scores, is in descending order. </li>
    <li>Alice's scores, alice, are in ascending order. </li>
</ul>

<h2> Subtask</h2>

For  of the maximum score:
<ul>
    <li> 1 <= n <= 200 </li>
    <li> 1 <= m <= 200 </li>
</ul>

<h2> Output Format</h2>

Print m integers. The jth integer should indicate Alice's rank after playing the jth game.
