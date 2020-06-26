Maria plays college basketball and wants to go pro. Each season she maintains a record of her play. She tabulates the number of times she breaks her season record for most points and least points in a game. Points scored in the first game establish her record for the season, and she begins counting from there.

For example, assume her scores for the season are represented in the array scores=[12,24,10,24]. Scores are in the same order as the games played. She would tabulate her results as follows:

                                 Count
Game  Score  Minimum  Maximum   Min Max<br>
 0      12     12       12       0   0<br>
 1      24     12       24       0   1<br>
 2      10     10       24       1   1<br>
 3      24     10       24       1   1
 
Given Maria's scores for a season, find and print the number of times she breaks her records for most and least points scored during the season.

<h2> Function Description </h2>

Complete the breakingRecords function in the editor below. It must return an integer array containing the numbers of times she broke her records. Index 0 is for breaking most points records, and index 1 is for breaking least points records.

breakingRecords has the following parameter(s):
<ul>
    <li> scores: an array of integers </li>
</ul>

<h2> Input Format </h2>

The first line contains an integer n, the number of games.
The second line contains n space-separated integers describing the respective values of score0,ccore1,...,scoren-1.

<h2> Constraints </h2>
<ul>
    <li> 1 <= n <= 1000 </li>
    <li> 0 <= scores[i] <= 10^8 </li>
</ul>
<h2> Output Format </h2>

Print two space-seperated integers describing the respective numbers of times her best (highest) score increased and her worst (lowest) score decreased.

<h2> Sample Input 0 </h2>

9<br>
10 5 20 20 4 5 2 25 1

<h2> Sample Output 0 </h2>

2 4
