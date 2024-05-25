The Python platform module: a quick dive
#########################################

:date: 2023-12-13
:author: Jeremiah Igrami
:category: python
:tag: python, windows, linux, machine
:slug: the-python-platform-module
:status: hidden


The platform module in Python is designed to give you specific information about the underlying platform. In computing, a platform is the environment a piece of software is running on, typically the hardware and operating system of the computer you're working with.

If you have a program that relies on certain hardware specs that differ across machines (e.g., the type of processor), the platform module can help you identify these details so that you can adjust your code accordingly.

Let’s run through some functions and find out what useful information they can tell us about our computer.

To use platform, all you have to do is import it (assuming you have Python installed). Just do import platform . Once imported, the module becomes available on your platform (pun intended) for you to explore.
