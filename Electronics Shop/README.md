Monica wants to buy a keyboard and a USB drive from her favorite electronics store. The store has several models of each. Monica wants to spend as much as possible for the 2 items, given her budget.

Given the price lists for the store's keyboards and USB drives, and Monica's budget, find and print the amount of money Monica will spend. If she doesn't have enough money to both a keyboard and a USB drive, print -1 instead. She will buy only the two required items.

For example, suppose she has b=60 to spend. Three types of keyboards cost keyboards=[40,50,60]. Two USB drives cost drives=[5,8,12]. She could purchase a 40 keyboards + 12 USB drive =52, or a 50 keyboard + 8 USB drive =58. She chooses the latter. She can't buy more than 2 items so she can't spend exactly 60.

<h2>Function Description</h2>

Complete the getMoneySpent function in the editor below. It should return the maximum total price for the two items within Monica's budget, or -1 if she cannot afford both items.

getMoneySpent has the following parameter(s):
<ul>
    <li> keyboards: an array of integers representing keyboard prices</li>
    <li> drives: an array of integers representing drive prices</li>
    <li> b: the units of currency in Monica's budget</li>
</ul>

<h2>Input Format</h2>

The first line contains three space-separated integers b,n, and m, her budget, the number of keyboard models and the number of USB drive models.
The second line contains n space-separated integers keyboard[i], the prices of each keyboard model.
The third line contains m space-separated integers drives, the prices of the USB drives.

<h2>Constraints</h2>
<ul>
    <li> 1 <= n,m <=1000 </li>
    <li> 1 <= b <= 10^6 </li>
    <li> The price of each item is in the inclusive range [1,10^6].</li>
</ul>

<h2>Output Format</h2>

Print a single integer denoting the amount of money Monica will spend. If she doesn't have enough money to buy one keyboard and one USB drive, print -1 instead.

<h2>Sample Input 0</h2>

10 2 3<br>
3 1<br>
5 2 8

<h2>Sample Output 0</h2>

9
