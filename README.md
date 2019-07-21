XIII-2 Clock Puzzle Solver
==========================

This is a quick script to solve the "Clock"-type puzzles in Final Fantasy XIII-2.

## How to use
Open up the `xiii-2.py` file in the text editor of your choice. Change the 1st line so the numbers in between the square brackets are those from the clock puzzle you want to solve. The order is important, the point where you start is not - I still recommend starting with what should be 12 o'clock and going clockwise for ease of use, though.

Save the changed file, then from a command line, run `$ python xiii-2.py`. It should print out (several) possible solutions; just pick one and have Serah do the right combination. Or Noel, I suppose, though who likes playing Noel, really?

The names printed correspond to the number of the hour you should go to next, and a letter to identify which if several of the same number is present on your clock. A is the first one, B is the second, etc., as per the starting point and ordering you used when filling up the List Of Hours (LOH). 

## Improvements to come never
I originally threw this together quick-and-dirty for my personal use; I used to input the full clock by hand. When I reached Oerba 400AF and realized there were a lot more of these to come, I coded up the automated clock generator from a manually inputed LOH, once again for personal use, but then I figured as it was my little script could maybe save someone the trouble someday, so here goes. I can't really foresee a timeline where I can be bothered to improve this thing, really, but if I did, I guess I'd start with the following:

- make it so you just launch the script, then it asks you to input the clock and you just type it in;
- make it so it only prints one possible solution;
- take a screen and write up a slightly more detailed tutorial here with the example.

## Still here?
If you're curious about that `verbose` keyword in `TryPath`, it was just for my personal curiosity - this puzzle thing messed with my head a lot more than it should have. For instance I wanted to see the proportion of successful paths, and whether you could pick any hour as your first choice, and how the number of possible solutions evolved with the number of hours, oh and also if I randomly generate clocks, are they always solvable?! That kind of thing.

## Okay, I'm flattered, you win a super cool fun fact.
There's an actual paper written by Nathaniel Johnston of the University of Guelph on puzzles in XIII-2! Here's the [arXiv link](https://arxiv.org/abs/1203.1633). Among other cool things, Nate showed (theorem 4) that a partially completed clock puzzle is NP hard. 

So yeah, if you ended up here - you can rest easy, it's not just you. This thing is _hard_.
