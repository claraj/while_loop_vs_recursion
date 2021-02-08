# Recursion vs. While Loop

You want to let your user play the game again. So you call the main function, and the game plays again. Everything looks good.

However, there's an issue. If main() calls main(), then the main function never returns, it starts another function running. Your computer has a limited amount of space to store all of the function and method calls in a program, and it can run out of space. This causes your program to crash.

Calling a function from itself is known as recursion, here's a simple example,

```
def main():
    print('this is the main method!')
    main()   # main calls itself - this is known as recursion


if __name__ == '__main__':
    main()
```

If you run this code, it will crash with a error `RecursionError: maximum recursion depth exceeded while calling a Python object`.

In a game, you may see this error after several hundred turns. Maybe not going to be an issue in rock-paper-scissions, but there are many places where a program repeats a task many times, and using recursion is not desirable.  

Another issue with recursion is that it can make code harder to test. If you try and test a function that calls itself, that calls itself, that calls itself.... there's no way for a test to end successfully. 

For this example, it would be better to use a while loop to repeat the program.

There are many useful applications of recursion. For example, games like Minesweeper and Candy Crush use recursive algorithms to work with the game board, https://en.wikipedia.org/wiki/Flood_fill.  Programs that traverse file systems often use recursion too. 

https://realpython.com/python-thinking-recursively/