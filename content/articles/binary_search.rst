
Binary search: a better way to look for things
################################################

:date: 2024-05-20
:author: Jeremiah Igrami
:category: DSA
:slug: binary-search
:tag: binary-search, dsa, linear-search, big-o


.. role:: red(strong)
    :class: m-text m-danger

.. role:: green(strong)
    :class: m-text m-success


The basic logic of binary search is eliminating irrelevant options to get to 
your target item faster.

.. contents::
    :class: m-block m-default

`Intro`_
==========


You are at a supermarket to get some chocolate bars. The market is doubly super, 
with many aisles displaying products of different types, shapes, and sizes. 
You can find what you are looking for by checking every single item in every 
category of every section. This technique is called **simple search**
(or *linear search*).

For a small list of items, simple search is a decent choice because it’s easy to do
and less prone to errors. But for a large group of things, such as goods in a 
supermarket, running a simple search would consume a lot of energy and waste a lot 
of time. 

This article is an introduction to the concept of **binary search algorithms**. 
You’ll learn what binary search is and how it compares to linear search. 
You’ll also learn how to implement binary search by writing a simple binary search 
algorithm in Python! 

------

Back to our supermarket example.

We know that products in a supermarket are often organized into categories, 
like “Canned Goods”, “Confectioneries”, “Fresh Produce”, etc. So the smarter way to 
find chocolate bars would be to narrow down your search by going to the specific 
category you would expect to find chocolates in, such as the section labeled 
“Confectioneries”, and begin your search from there. This is similar to how binary 
search works.

Binary search is an algorithm. An algorithm is just a series of steps a computer 
can follow to perform a task. The task could be a simple one like adding two numbers
or a complex one like finding the shortest possible path to a group of five cities 
in different geolocations. A binary search algorithm enables you to quickly find 
the position of something in a sorted list of things by repeatedly splitting the 
list in the middle, narrowing down the possible location of the target item with 
each split, until the item is found or the list is exhausted

While our supermarket technique isn’t exactly an implementation of a binary search 
algorithm, the underlying principle is the same: **eliminate irrelevant options to 
get to your desired outcome faster**.



`The guessing game`_
====================

One practical application of the binary search technique is in the popular guessing 
game. Here is an example.

I’m thinking of a number between 1 and 10. Your goal is to guess the number in the 
fewest tries possible, much like the `Wordle game <https://www.nytimes.com/games/index.html/>`_. 
With each guess, you’ll receive one of three feedbacks from me: :green:`correct`, 
:red:`too low`, or :red:`too high`. 

Let’s say my secret number is 9. You could try to guess it by following the simple 
search approach, considering every single number from 1 through 10, like this: 

.. code-block:: console

    Me: I'm thinking of a number between 1 and 10. Can you guess the number?

    You: 1

    Me: too low

    You: 2

    Me: too low

    You: 3

    Me: too low

    You: 4

    Me: too low

    ...

    You: 9

    Me: Correct!

But wait, that took you nine tries! If it were a Wordle game, you’d have run out 
of guesses before you got the number correctly. 

Now what if you applied a binary search approach in this game? You know the size 
of the list is 10, so you’d start from the middle:

.. code-block:: console

    Me:  I'm thinking of a number between 1 and 10. Can you guess the number?
    
    You: 5

    Me: too low

    
    # If 5 is too low, then 4, 3, 2, and 1 are also too low.
    # They can be safely discarded. You now have to consider
    # only numbers between 6 and 10. So you pick a middle number again.
    

    You: 7

    Me: too low

    
    # Again, 6 and 7 are out of consideration, remaining numbers
    # from 8 to 10. You pick the middle value.


    You: 9

    Me: Correct!


You got the answer in 3 tries, enough to win a Wordle game! That’s four steps fewer
than the linear search approach. This may not seem much at first. But the 
difference in steps between linear and binary search increases significantly 
as the input size grows. That is, as the list gets larger, binary search becomes 
much faster compared with linear search, and the gap in efficiency between the two 
methods widens considerably.

Consider this next example:

At the time of this writing, Spotify has about 11 million artists on its 
platform. Imagine you need to search for a particular artist by name. 
In a linear search algorithm, which examines every single item from first to last, 
it would take the computer 11 million steps to find the artist, in the worst case. 
With a binary search algorithm, however, it would take the computer only about 23 
steps! Notice how the difference widens dramatically as the list grows? 


`Big O notation`_
=================

But how did I know a binary search algorithm can search an entire list of 11 
million items in just 23 steps? I explain in this section.

To measure the speed (a.k.a. *runtime*) of an algorithm, computer scientists use a 
technique called Big O notation. Don’t worry; this is one of those fancy terms that
sound a lot more complicated than they really are. 
Big O notation is just a way to tell how much slower an algorithm would run if the 
size of the data it handles increases.

There are several Big O runtimes (you can check out this comprehensive `Big O 
cheatsheet <https://bigocheatsheet.com/>`_), but for the sake of simplicity, 
we'll focus only on the two runtimes most relevant to this article.


`O(n), where n is the size of the list`_ 
--------------------------------------------

This type of algorithm runs in
linear time, or *n length of time*. This means that, as the input size (n) grows, 
the amount of time the algorithm takes to run also increases linearly. 
So if the list is 10 items long, an algorithm with this run time might take 10 
steps to complete a search on the list. If the list grows to 11 million, it might then take 11 million 
steps. The simple search technique, introduced at the beginning of this article, 
is an example of an algorithm with this runtime.


`O(log n), where n is the size of the list`_
-----------------------------------------------

Unlike linear search, algorithms with O(log n) runtime, such as the binary 
search algorithm, run in *logarithmic time*. 

.. note-info:: Important note

    In Big O, ``log`` is always understood to be in ``base 2``, and the :sub:`2`
    is sometimes left out in the expression. So :math:`log n`  is actually
    log\ :sub:`2`\  n. 

..

.. block-success:: A word on logarithms (from an innumerate)

    Think of logarithms as the inverse operation of exponentials.
    For example, the expression ``two exponent three`` (:math:`2^3`)
    in logarithmic notation would be ``log base two of eight`` (:math:`log 8`). 
    This is simply asking, `How many times do I need to multiply 2 by itself to 
    get 8?` The answer is 3 times (:math:`2 * 2 * 2 = 8`). Hence :math:`log  8 = 3`
    Interestingly, :math:`2^3 = 8`. This shows that **logarithms** 'undo' the 
    operation of **exponentials**, and vice versa. See? Logarithms and exponentials 
    are opposite operations of each other. 
    
    Now, going back to our Spotify list example. How did I know a binary search 
    algorithm would take approximately 23 steps to search an entire list of 
    11 million names? I know because binary search runs in **logarithmic time**, 
    and :math:`log  11,000,000 = 23.4`. 
    
    
Big O helps us compare algorithms to understand how they perform as the data they 
work with gets larger. It helps us make better decisions on which algorithm to use 
for specific use cases, because we can always tell, through Big O notation, 
how their performance will be impacted as the data they handle grows. 

-------


`Writing your first binary search algorithm with Python`_
==========================================================

Now that you understand what binary search is, how it compares to linear search, 
and how software engineers measure the performance of algorithms, you’re ready
to write your first algorithm.


.. note-primary::

    To follow the code example in this section, you’ll need to have Python and a code 
    editor installed. Get the latest version of Python for your 
    operating system on the `official website <https://www.python.org/>`_. 
    
    For a code editor, VS Code is a popular choice. It’s free, lightweight, and 
    feature-rich. Get VS Code `here <https://code.visualstudio.com/Download/>`_.


A basic binary search function accepts two arguments: **a sorted list** and a 
**target item** to search for in that list. If the item is in the list, the 
function will return its *index*. If not, the function will return None.

Ready? Let's write some code! Open your code editor, create a new file, and 
name it ``binary_search.py``. 

.. note-dim::

    I encourage you to type the code by hand instead of just copying and pasting. 
    Doing so helps you develop muscle memory. Plus, typing it is more fun! It's
    what gives you the 'hands-on' experience. 


We’ll start by defining the function we just described above using the ``def`` keyword:



.. code-block:: python
    

    def binary_search(sorted_list, item):
        '''A function to calculate the index of an item in a sorted list'''
        pass


The code above defines a function called ``binary_search`` that expects two 
arguments: the list you want to search and the item you want to search for. 
Once these two args are supplied, the function will calculate and print out the location
(i.e., the index) of the item you’re looking for. The comment enclosed by '''
is the function documentation (a.k.a, docstring), describing the function and what
it does. The ``pass`` keyword is just a placeholder for the code we'll add later. 


In binary search, knowing the exact length of the list is important. So the next 
step is to define the first and last indexes of the list you're working with 
so you can keep track of your search range:

.. code-block:: python
    

    def binary_search(sorted_list, item):
        '''A function to calculate the index of an item in a sorted list'''

        first_item = 0
        last_item = len(sorted_list) - 1


The index of the last item in a sorted list is the length of the list - 1. 
This is because of something called **zero-based indexing**, where the first item in
a sequence is assigned the index 0, instead of 1. Hence, in a sorted list of 10 
items, the index of the last item is 9.

Here's the remaining body of the code for our binary search algorithm:

.. code-block:: python

    ...
    


        while first_item <= last_item: 
            # calculate the position of the middle item
            middle_item = (first_item + last_item) // 2
            
            # make that value you got your first guess
            guess = sorted_list[middle_item]

            # check whether your guess is correct. if yes, return the item.
            if guess == item:
                return middle_item
            elif guess > item:      
                last_item = middle_item - 1
            else:
                
                first_item = middle_item + 1
            
        # If the loop ends without finding a match, the item is not on the list
        
        return None
        

A lot of interesting things are going on in the code above. Let’s take it line by 
line:

.. code-block:: python
    

    while first_item <= last_item:
        middle_item = (first_item + last_item ) // 2
    

The first line initializes a while loop that runs as long as the starting index 
(``first_item``) is less than or equal to the ending index (``last_item``). 
This loop ensures that the search continues until the target item is found or the 
search range is exhausted. The next line calculates the middle index of the current 
search range by adding the first and last indexes and dividing by 2.

.. note-dim::

    The // operator, called **floor division** in Python, ensures that the result
    returned is a single integer value, not a decimal. For example, :math:`5 // 2` 
    returns :math:`2`, whereas :math:`5 / 2` returns :math:`2.5`.

..

.. code-block:: python

    
    guess = sorted_list[middle_item]


Here, the middle item of ``sorted_list`` is retrieved and assigned 
to the variable ``guess``. This is our current candidate for the target item.

.. code-block:: python


        if guess == item:
            return middle_item


This block checks whether ``guess`` matches the target ``item``. If yes, the 
function returns ``middle_item``, which should be the position of ``item`` in ``sorted_list``. 
If you want the code to return the ``item`` itself, not **its position** on the list, 
all you have to do is change the return value from ``middle_item`` to ``item``. 
So the code will now be 

.. code-block:: python

    if guess == item: 
        return item


..

Next line:


.. code-block:: python

    
    elif guess > item:
        last_item = middle_item - 1
    else:
        first_item = middle_item + 1


If the value we guessed is greater than the target item (``guess > item``), 
it means the item we're looking for must be in the lower half of our list. 
So we narrow our search range to the lower half by updating our current ending 
index (``last_item``) to be **one position less than the middle**, effectively 
cutting the list in half. And if the guess is lower than the target 
(``guess < item``), the code also updates the starting index (``first_item``) 
to be **one position greater than the current middle**, discarding 
the lower half.

For example, assuming our list has 10 items. The target item is 3, but our first 
guess was 5, which is higher than the target. Invariably, every item after
``5`` (6, 7, 8, 9, and 10) would also be higher than our target and therefore 
irrelevant to our search. We discard the irrelevant half of the list by updating
the position of ``last_item`` to be ``middle_item`` - 1. That would be :math:`5 - 1`, 
which is :math:`4`. So we now have a new search range (0 to 4).

..


The last line:


.. code-block:: python

    ...

    # If the loop ends without finding a match, the item is not on the list

    return None


If the while loop completes without finding the target item, the function returns 
None. This indicates that the item is not present in the list.

Here's the complete code: 

.. code-block:: python

    def binary_search(sorted_list, item):
        '''A function to calculate the index of an item in a sorted list'''

        first_item = 0
        last_item = len(sorted_list) -1

        while first_item <= last_item: 
            # calculate the position of the middle item
            middle_item = (first_item + last_item) // 2
            
            # make that value you got your first guess
            guess = sorted_list[middle_item]

            # compare 'guess' with 'item'. If they match, return the index.
            if guess == item:
                return middle_item
            elif guess > item:      
                last_item = middle_item - 1
            else:
                
                first_item = middle_item + 1
            
        # If the loop ends without finding a match, the item is not on the list  
        
        return None

        

Let's run the code to see if it works. We’ll test it on two lists:
a list of numbers and a list of desserts:


>>> nums = [20, 33, 40, 55, 58, 64, 77, 89]
>>> desserts = ['bacon', 'donut', 'eggs', 'ice cream', 'pizza', 'spam']
>>> print(binary_search(nums, 77))
6
>>> print(binary_search(desserts, 'ice cream'))
3
>>> print(binary_search(nums, 90))
None
>>> print(binary_search(desserts, 'cheesecake'))
None


If everything goes well, you should see results similar to our examples
above. The algorithm returns the position of the items you specify 
in the first and second print calls. The number ``77`` is at index 6 of the 
list ``nums``, which is why the function returns 6. The same for ``ice cream``,
which is at index 3 of ``desserts``. The third and fourth print calls both return 
None because 90 is not in ``nums`` nor is 'cheesecake' in ``desserts``. 

.. note-warning:: Important!

    
    Notice that both lists in our example are sorted (``desserts`` is sorted 
    alphabetically). Binary search works only 
    on sorted data. So if the list you're working with isn't sorted, you might 
    need to take the extra step to sort it before applying a binary search 
    function. Fortunately, many easy-to-implement sorting algorithms, like 
    **selection sort** and **quick sort**, are available. And most 
    programming languages, including Python, offer built-in sorting functions 
    that allow you to sort your data with just a single line of code!
    

That's it! You have successfully implemented a binary search algorithm in
Python. Although it’s tested here on a small list of items, this algorithm 
will work perfectly even if the input size is 1 billion!

Don’t stop here. There are many more powerful and important algorithms to learn. 
This is your first step into mastering skills that are useful for everyday 
problem-solving. I’m also learning and loving it. Join me!














    






                  











    

















