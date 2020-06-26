An English text needs to be encrypted using the following encryption scheme.
First, the spaces are removed from the text. Let L be the length of this text.
For example, the sentence s= if man was meant to stay on the ground god would have given us roots, after removing spaces is  characters long.  is between  and , so it is written in the form of a grid with 7 rows and 8 columns.

ifmanwas <br> 
meanttos <br>         
tayonthe <br> 
groundgo <br> 
dwouldha <br> 
vegivenu <br> 
sroots
<ul>
    <li> Ensure that rows X columns >= L </li>
    <li> If multiple grids satisfy the above conditions, choose the one with the minimum area, i.e. rows X columns.</li>
</ul>
The encoded message is obtained by displaying the characters in a column, inserting a space, and then displaying the next column and inserting a space, and so on. For example, the encoded message for the above rectangle is:

imtgdvs fearwer mayoogo anouuio ntnnlvt wttddes aohghn sseoau

You will be given a message to encode and print.

<h2> Function Description </h2>

Complete the encryption function in the editor below. It should return a single string composed as described.

encryption has the following parameter(s):
<ul>
    <li> s: a string to encrypt </li>
</ul>
<h2> Input Format </h2>

One line of text, the string s

<h2> Constraints </h2>
<ul>
    <li> 1 <= |s| <=81 </li>
    <li> s is comprised only of characters in the range ascii[a-z]. </li>
</ul>

<h2> Output Format </h2>

Print the encoded message on one line as described.

<h2> Sample Input </h2>

haveaniceday

<h2> Sample Output 0 </h2>

hae and via ecy
