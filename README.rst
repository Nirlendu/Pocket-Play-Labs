Pocket Play Labs Assignment
===========================

This is in fulfilment of Pocket Play Labs Assignment 

.. code-block:: pycon

    >>> python Source/ServerDataParser.py Test_Cases/sample.log


This will run a proper analysis for the server data

Alternatively, we can also run the makefile

.. code-block:: pycon

    >>> make all


Features
--------

- Proper format of design.
- Codes are well organised using OOPS.
- Efficient, used the minimum memory possible. Used a single array to calculate mean, median and mode.

Details
-------
- Though I could have done a lot more, like making it like a library, and/or breaking the codes further into separate files and classes, I opted out of it because of the simplicity of the assignment, assuming that the above steps would be unnecessary.  In more complex scenarios, the above stated points should be taken care of.

- Calculation wise, I used a single array to calculate mean, median and mode. The complexity for respective operations would be O(n), O(1), O(nlogn), with a space complexity of O(n), for storing the array.

- The calculation of dyno is O(n) operation, with O(n) space requirements, as I am using a dictionary for storing the data.