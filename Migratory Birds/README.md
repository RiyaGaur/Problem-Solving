You have been asked to help study the population of birds migrating across the continent. Each type of bird you are interested in will be identified by an integer value. Each time a particular kind of bird is spotted, its id number will be added to your array of sightings. You would like to be able to find out which type of bird is most common given a list of sightings. Your task is to print the type number of that bird and if two or more types of birds are equally common, choose the type with the smallest ID number.

For example, assume your bird sightings are of types arr=[1,1,2,2,3]. There are two each of types 1 and 2, and one sighting of type 3. Pick the lower of the two types seen twice: type 1.

<h2>Function Description</h2>

Complete the migratoryBirds function in the editor below. It should return the lowest type number of the most frequently sighted bird.

migratoryBirds has the following parameter(s):
<ul>
    <li>arr: an array of integers representing types of birds sighted</li>
</ul>

<h2>Input Format</h2>

The first line contains an integer denoting n, the number of birds sighted and reported in the array arr.
The second line describes arr as n space-separated integers representing the type numbers of each bird sighted.

<h2>Constraints</h2>
<ul>
    <li> 5 <= n <= 2 X 10^5 </li>
    <li>It is guaranteed that each type is 1,2,3,4, or 5.</li>
</ul>

<h2>Output Format</h2>

Print the type number of the most common bird; if two or more types of birds are equally common, choose the type with the smallest ID number.

<h2>Sample Input 0</h2>

6<br>
1 4 4 4 5 3

<h2>Sample Output 0</h2>

4
