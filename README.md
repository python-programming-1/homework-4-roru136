# homework-4

Part 1:

Imagine you have the following list:

vegetables = ['carrot', 'lettuce', 'onion', 'radish']

Write a function that takes a list as an argument and returns a sentence of the items in a list like so 'carrot, lettuce, onion, and radish.' Notice that there is a comma and space between each item, and at the very last item, there is a comma, space, an 'and' and a period. 

Your function should be able to handle any list of items and output a string with the above mentioned format.

```python
def my_function(some_list):
     # do formatting here
     return my_formatted_string
```
     
Part 2:

Imagine you have the following grid:
```python
grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]
```      
You can think of grid[x][y] as being the character at the x- and y-coordinates of a “picture” drawn with text characters. The (0, 0) origin will be in the upper-left corner, the x-coordinates increase going right, and the y-coordinates increase going down.

Copy the previous grid value into your python script, and write code that uses it to print the image.
```
..OO.OO..
.OOOOOOO.
.OOOOOOO.
..OOOOO..
...OOO...
....O....
```
Hint: You will need to use a loop in a loop in order to print grid[0][0], then grid[1][0], then grid[2][0], and so on, up to grid[8][0]. This will finish the first row, so then print a newline. Then your program should print grid[0][1], then grid[1][1], then grid[2][1], and so on. The last thing your program will print is grid[8][5].

Also, remember to pass the end keyword argument to print() if you don’t want a newline printed automatically after each print() call.

homework source: https://automatetheboringstuff.com/chapter4/
