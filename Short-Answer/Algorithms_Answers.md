#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(n) A single while loop is O(n), this equates to O(n^3) - O(n^2), breaks down to O(n) 


b) O(n log n). The first loop running is O(n). 
The second loop only runs when J is less than n. When it does. J increments.


c) O(n) This will run as many times as needed to get down to the basecase.  

## Exercise II


1. Cut the number of floors (n) in half, and then drop an egg to see if it breaks. 
2. Based on return value, you would either remove the higher or lower values of n.
3. You continue to do this until you find the right floor (f)

The runtime complexity is O(log n)
