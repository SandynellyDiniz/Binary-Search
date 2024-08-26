

<h2 align="center">Binary Search 🕵🏻‍♀️🔍</h2>
<h3>Binary search, is a fundamental algorithm in computer science. 
    It allows you to perform efficient searches in ordered lists. Let's explore how it works:
</h3>

<h3>1 - Basic Principle:</h3>
<ul>
  <li>Binary search is applied to an ordered list (e.g. a list of numbers in ascending order).</li>
  <li>The algorithm repeatedly splits the list in half, reducing the possible locations of the searched element.</li>
</ul>

<h3>2 - Algorithm Steps:</h3>
<ul>
  <li>Initially, we have the complete list.</li>
  <li>We calculate the index of the intermediate element of the list.</li>
  <li>We compare the middle element with the sought value.</li>
  <li>If the fetched value is equal to the middle element, we find the element and return its index.</li>
  <li>Otherwise, we check whether the fetched value is greater or less than the middle element.</li>
  <li>If it is larger, we repeat the process on the top half of the list; if it is smaller, in the lower half.</li>
  <li>We continue dividing the list until we find the element or determine that it is not present.</li>
</ul>

<h3>3 - Efficiency:</h3>
<ul>
  <li>Binary search is very efficient, as each iteration reduces the search space by half.</li>
  <li>Its complexity is O(log n), where n is the size of the list.</li>
  <li>Compared to linear search, which has O(n) complexity, binary search is significantly faster for large lists.</li>
</ul>


