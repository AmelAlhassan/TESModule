#Choose.py
# 4.12.2015

import random
def choose(x,y):
	"this fuction chooses y random elements from a list xand return them in a list"
	choice = random.sample(x,y)
	return choice
