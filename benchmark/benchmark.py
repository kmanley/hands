import sys
sys.path.append("..")
import hands
import time
from decorators import timed

score_5 = timed(hands.score_5)

HANDS = ["THJHQHKHAH", "2H3H4H5H6H", "4C4H4D4SAH", "3H3D4C4D4S", "3C4C5C9CAC", "2C3C4D5H6S", 
         "6S7D8H9STH", "6S6D6H9STH", "4S4DTHTS3H", "3H4S4D7S7H", "3H4S7S7HJD", "3H4STSJDQH"]

ITERS = 1000
for i in range(ITERS):
    for hand in HANDS:
        score_5(hand)
    
