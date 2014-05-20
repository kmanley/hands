#Hands#

A simple 5-card poker hand evaluator and classifier implemented in Python/Cython. There are 2 functions:

* score_5: Given a string hand representation, compute
and return a score as a tuple.
* classify_5: Given a string hand representation or score,
return a string classification of the hand.

Note that hand strings are specified as, for example, "6S7D8H9STH". That is, the string must be sorted by rank and suits must be uppercase.

##Usage##

You can either import the Python module hands.py directly, or run the setup.py to generate a c-module via Cython. The Cython-generated module is about 33% faster.

    python
    >>> import hands
    >>> hands.score_5("3C4C5C6C7C")
    (9, 7)
    >>> hands.classify_5(_)
    'Straight Flush - 7 high'
    

##Tests##
This module uses doctest. To run the tests type:

    python hands.py    

##Benchmark##
In the benchmark directory there's a script that times several thousand calls of the score_5 function and emits some statistics. 

On my machine (WinXP 64-bit, Xeon W3530@2.80GHz, 12GB RAM, Python 2.7), I get:

* Pure python module: ~145,000 calls/sec
* Cython C module: ~200,000 calls/sec	

##Usefulness##
It works but is pretty slow. This was mostly an experiment to help me learn Poker. If you're looking for a high performance hand evaluator there are others out there that can do millions of hand evaluations per second. See [here] for more info.

[here]:http://www.codingthewheel.com/archives/poker-hand-evaluator-roundup

#License#
Public domain
