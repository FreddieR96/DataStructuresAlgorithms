# Data Structures and Algorithms

This project contains algorithms for sorting a random array of sortable data and structures for querying and displaying data.

## Binary Search Tree

Displaying data as a binary tree with elements getting smaller the further to the 'left' they are enables binary search. The algorithm can ignore half of the remaining subtree every time it descends the tree, because that subtree contrains items that are too big or too small to be the answer. This yields an efficiency tending towards O(log n) the 'fuller' the tree gets.

## Binary Heap

This min-heap places the smallest element at the top, with each element having two children which are larger than it. You can create a sorted array by popping elements into the array at O(n log n) efficiency as the last element in the array must be moved back into its proper place for each element.

## Hash

Allows lookup of item value using its key. The index of a string key in the list is determined by the sum of the unicode of its characters modulus the array length. There is a linked list at each index which is queried at O(n) efficiency, but redistributing after the list reaches a threshold of 0.75 should stop large lists developing.

## Directed Acyclic Graph

A DAG is a great way to represent data that is comprised of vertices and weight edges, such as the distance between different airports in a network. An instance of the DAG here has a method that constructs a grid of the minimum distance from a chosen root to all connected vertices.

## Priority Queue

This priority queue places the 'smaller' elements at the front of the queue. When a new item is added, items that are now lower priority are all moved down one place.

The queue uses a special array which will move the front index up when an element is popped rather than move all elements downwards. It will also move the rear index to 0 and up if it is vacant, rather than resize and redistribute the whole array.

## Algorithms

This includes three algorithms for sorting unsorted data. Selection sort goes through the array for each element and places the lowest element it finds in the lowest unsorted index for O(n^2) efficiency.

Quick sort breaks the array into subarrays with items smaller and larger than a randomly selected pivot on either side of it. The subarrays are continuously broken down until they are one element long. All elements in the array have to be visited to sort them into subarrays, but we avoid comparing it to at least half the array which we know is bigger or smaller than the element, yielding efficiency of O(n log n).

Merge sort continually breaks the array down into subarrays until the elements are ready for sorting. Once an array reaches four elements across, the first two elements and second two elements will be sorted by size. Then, while the positioned element in the second half of the array is bigger than the positioned element in the first half, the element from the first half will be added to a holding array before moving on to the next element in the first half of the array, a bigger element. When the position has gone beyond the first half of the array, all remaining elements in the second half will be added in, in their sorted size order. If the second half has been exhausted first, all remaining elements in the first half will be added in. The recursive calling of the function emans this will be done for bigger and bigger subarrays on the left of the array and then the right, leading to the whole array being sorted. We avoid comparing every index with every other, but the amount of operations needed rises with indexes in the array for efficiency of O(n log n).

The folder also includes a sortable class called Developer with a class method to return an unsorted array of up to 50 developers.
