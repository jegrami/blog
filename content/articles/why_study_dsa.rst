
Why Study Data Structures and Algorithms?
##########################################

:date: 2024-05-08
:author: Jeremiah Igrami
:category: DSA
:slug: why-study-dsa
:tags: algorithms, data
:hide_summary: True



Programmers learn a lot by looking at how other programmers do their work. 
We learn by watching others do, and by doing. We learn how to solve problems
by studying various problem-solving techniques and solutions developed by others.
After a while of exposing ourselves to so many techniques, we start to 
recognize patterns in problems and develop solutions of our own. 

For example, having gone through a handful of problems and solutions on Leetcode,
I observed that, with challenges that involved tasks like comparing or 
evaluating subelements while moving through the sequence of elements, two
techniques often came up in most solutions Leetcoders submitted: 
**sliding window** and **two pointers**. 

The sliding window technique lets you analyze an array of elements in small 
chunks (called *windows*). You focus on one window at a time as you slide through 
the array, performing some operation on each window. We use two pointers to 
keep track of the left and right boundaries of the window.

Knowing this, whenever I encounter problems like *finding the longest character 
substring*, *checking if a word is a palindrome*, or *grouping anagrams*, the first
question that comes to mind is, *Can I solve this problem with a sliding window 
and two pointers?* Without much thinking, I already have a starting point 
for a solution, solely based on my experience seeing how other programmers 
have solved similar problems in the past.


The ability to recognize patterns in problems, consider various solutions, 
and then choose the best one for that specific problem is at the core of what 
software engineers do. And that’s a skill you acquire through a dedicated 
study of data structures and algorithms. 


.. note-info::

    I use the terms 'programmer', 'software engineer', and 
    'software developer' interchangeably in this article. They all mean the
    same thing to me. A programmer is someone who specializes in writing 
    computer source code, a.k.a programs. To be a software developer or software 
    engineer, you need to be skilled in computer programming as well as other
    things like software design and testing. 
    


Every software application on the planet is powered by two elements: 
**data** and **algorithm**. While *algorithms* are step-by-step instructions 
that a computer can follow to solve a problem, *data* provides the input
and context the computer needs to execute the instruction and produce the desired 
result. And *data structures* are ways in which programmers 
organize and store data for computers to process and manipulate.

In other words, algorithms show us how to solve a problem by describing the data needed to 
represent it and the steps required to produce the desired 
output. Data structures, on the other hand, help us organize and store the 
data we need in  a way that makes it easy for our algorithms to access, modify, 
and manipulate it. 

Data Structures and Algorithms (DSA) are the cornerstone of computer science 
and software engineering. The two go hand-in-hand. Together, they provide 
a powerful toolkit for programmers to tackle complex problems. 

Why do tech companies use DSA problems to assess software engineering skills?
==============================================================================

The internet is growing fast. So is the data we generate every day, and so is 
our ability to perform complex computations on large input data. The problems 
companies deal with nowadays are large-scale, often requiring data-intensive 
applications to solve them. Software developers with a solid understanding of DSA 
are preferred for *their ability to provide efficient procedures for 
solving large-scale problems.* 

The following are some more reasons why companies prefer devs with 
DSA skills:

To make efficient use of computing resources
---------------------------------------------

Companies measure the cost of a software solution by how much computing resource 
it would consume. How much memory and execution time would the system need to run? 
Developers skilled in DSA know how to design algorithms that run faster. 
They know how to choose the most suitable data structure and algorithm 
to minimize storage consumption and reduce costs for their company. 


To create software systems that scale
-------------------------------------


As more people get online, the number of users that software systems need to handle 
grows rapidly. Scalability becomes a critical concern. With a well-designed app, 
businesses can accommodate growing user traffic without compromising performance.
Software engineers with DSA expertise build scalable apps by carefully selecting
their data structures and obsessing over the execution time of their algorithms. 



To serve performance-critical applications
-------------------------------------------

Interactive video applications like Zoom are a type of web apps that require 
real-time, uninterrupted audio and video transmission in both directions. 
Minor delays to this transmission, leading to skipped sounds or frozen video, 
will certainly annoy users. No one would want to use a video conferencing app 
afflicted with poor network latency. 

Ensuring smooth video and audio delivery, especially under low network bandwidth 
conditions, is often a significant challenge for the maintainers of these software 
systems. As a developer working on these applications, you are *required* 
to know how to structure data and algorithms to support fast information 
flow and retrieval. Building and maintaining performance-sensitive 
applications would be difficult without a solid grasp of DSA principles 
and techniques.


Comparing Algorithms
=====================

Algorithms are solutions. There are often more than one solution to a problem. 
Programmers need a way to compare different solutions to determine which one is 
best for the given situation. The best solutions are the ones that need less time
and space to run — or the ones that make the most efficient use of available time
and space. The space an algorithm consumes is typically determined 
by the specific problem case. We more often compare algorithms based on their
running time. To do this, programmers consider how the speed of the algorithm 
changes as the size of the data grows.

For example, suppose you want to search for a name in a list of 40 names. 
You could choose to use a **simple search algorithm** (also called *linear search*), 
which will look at every name on the list one by one, from first to last, 
until the target name is found. But it would take 40 steps to complete the 
search in the worst case (i.e., if the target name is the last entry on the list). 
Now, assuming it takes a millisecond (ms) to lookup one name, 
that’s 40 ms for 40 names. Programmers say this type of algorithm runs in 
*linear time*.

Alternatively, you could choose the **binary search approach**. 
Rather than look at every single name, one by one, binary search looks at the 
*middle* name first, and then, if it's not the target name, it divides the list in 
half and checks the middle name again. The algorithm will repeat 
this process until the target name is found or the list is exhausted. 
For a list of 40 names, a binary search will take roughly five steps 
(or 5 ms) to achieve the same result because a binary search algorithm runs in 
*logarithmic time*

.. block-success:: A word on logarithms (from an innumerate)

    Think of logarithms as the inverse operation of exponentials. 
    For example, the expression :math:`8^2` in logarithmic notation 
    would be expressed as ``log base two of eight``, denoted as 
    log\ :sub:`2`\  8. This is simply asking, `How many times do I need 
    to multiply 2 by itself to get 8?` The answer is 3 times 
    (:math:`2 * 2 * 2 = 8`). So :math:`2^8` (``two exponent eight``) is the same 
    as log\ :sub:`2`\  8. Logarithms and exponentials are inverse operations
    of each other. 


Now, back to comparing algorithms. Let’s assume that our list 
suddenly grows into a database of three billion names. How will this growth 
affect the search speed of our algorithms? 

For the linear search algorithm, it will now take exactly three billion steps
to complete the search. That's ``three billion ms``, equivalent to 34 days! 

What about the binary search algorithm? How long will it take to 
complete the search? Remember that binary search runs in logarithmic time. So that   
would be log\ :sub:`2`\  3,000,000,000, which amounts 
to roughly 31 steps (31 ms). 

As you can see, binary search is better than linear search for finding a name 
quickly in a list of names, especially if that list is large. Also notice that,
as the list grew larger, the performance gap between the two algorithms widened
exponentially. Binary search becomes increasingly more efficient than 
linear search as the size of the input data grows.

Choosing the right tool and technique to tackle a problem could mean the 
difference between solving that problem in **three seconds** and **three days**, 
or between solving it in **five steps** and **five thousand steps**. As a developer,
it's not enough to just throw in any solution to solve a problem. 
You must be able to compare several techniques to come up with the most efficient solution, especially when
the data you’re working with is large. 

DSA teaches you how to evaluate solutions for their efficiency so you can decide
which one is best for the task at hand. Understanding the low-level 
implementation details of common data structures and algorithms help 
programmers achieve this.













      

