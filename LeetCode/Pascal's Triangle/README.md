# Pascal's Triangle I and II
https://leetcode.com/problems/pascals-triangle/

https://leetcode.com/problems/pascals-triangle-ii/

# Notes
Generating specific row uses simplified equation for `Any Entry in The Triangle` from:

https://www.mathsisfun.com/pascals-triangle.html

If you iterate through entire row from the beginning to the middle no factorials from the equation are required. Simply 
multiply by decreasing iterator and divide by increasing iterator. Then add reversed list of results.