You are in charge of the cake for your niece's birthday and have decided the cake will have one candle for each year of her total age. When she blows out the candles, she’ll only be able to blow out the tallest ones. Your task is to find out how many candles she can successfully blow out.

For example, if your niece is turning 4 years old, and the cake will have 4 candles of height 4,4,1,3, she will be able to blow out 2 candles successfully, since the tallest candles are of height 4 and there are 2 such candles.

<h2>Function Description</h2>

Complete the function birthdayCakeCandles in the editor below. It must return an integer representing the number of candles she can blow out.

birthdayCakeCandles has the following parameter(s):
<ul>
    <li>ar: an array of integers representing candle heights</li>
</ul>
<h2>Input Format</h2>

The first line contains a single integer,n, denoting the number of candles on the cake.
The second line contains n space-separated integers, where each integer i describes the height of candle i.

<h2>Constraints</h2>
<ul>
  <li> 1 <= n <= 10^5</li>
  <li> 1 <= ar[i] <= 10^7</li>
</ul>
<h2>Output Format</h2>

Return the number of candles that can be blown out on a new line.

<h2>Sample Input 0</h2>

4<br>
3 2 1 3

<h2>Sample Output 0</h2>

2
