<h2> Sequence Equation </h2>
Given a sequence of n integers, p(1),p(2),....,p(n) where each element is distinct and satisfies 1 <= p(x) <= n. For each x where 1 <= x <= n, find any integer y such that p(p(y))=x and print the value ofy on a new line.
For example, assume the sequence p = [5,2,1,3,4]. Each value of x between 1 and 5, the length of the sequence, is analyzed as follows:
<ol>
   <li> x = 1 = p[3],p[4]=3, so p[p[4]] = 1 </li>
   <li> x = 2 = p[2],p[2]=2, so p[p[2]] = 2 </li>
   <li> x = 3 = p[4],p[5]=4, so p[p[5]] = 3 </li>
   <li> x = 4 = p[5],p[1]=5, so p[p[1]] = 4 </li>
   <li> x = 5 = p[1],p[3]=1, so p[p[3]] = 5 </li>
</ol>
The values for y are [4,2,5,1,3].
<h2> Function Description </h2>
Complete the permutationEquation function in the editor below. It should return an array of integers that represent the values of y.
permutationEquation has the following parameter(s):
p: an array of integers

<h2> Input Format </h2>
The first line contains an integer n, the number of elements in the sequence.
The second line contains n space-separated integers p[i] where 1 <= i <= n.

<h2> Constraints </h2>
1 <= n <= 50 <br>
1 <= p[i] <= 50, where 1 <= i <= n. <br>
Each element in the sequence is distinct.

<h2> Output Format </h2>
For each x from 1 to n, print an integer denoting any valid y satisfying the equation p(p(y))=x on a new line.

<h2> Sample Input 0 </h2>
3<br>
2 3 1

<h2> Sample Output 0 </h2>
2<br>
3<br>
1
