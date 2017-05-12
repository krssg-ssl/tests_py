from krssg_ssl_msgs.msg import BeliefState
from plays_py.utils import config
from random import randint

sample_states = {}

"""
	States are stored in the following format:
	<team_color><ball_pos><home_bot(i)_pos><away_bot(i)_pos>
	Eg : B1234567891234

	Positions are defined as:
	+-----------------------------------+
	|           |           |           |
	|     1     |     2     |     3     |
	|-----------|-----------|-----------|
	|--+        |           |        +--|
	|--+  4     |     5     |     6  +--|
	|-----------|-----------|-----------|
	|           |           |           |
	|     7     |     8     |     9     |
	+-----------------------------------+
	
"""

MINX = 1
MAXX = 100

MINY = 1
MAXY = 50

RESY = (MAXY - MINY) / 3
RESX = (MAXX - MINX) / 3

def parse_pos_rand(pos):
	r = (pos-1)/3
	c = (pos-1)%3

	y_min = RESY*r
	y_max = y_min + RESY

	x_min = RESX*c
	x_max = x_min + RESX

	return (randint(x_min, x_max), randint(y_min, y_max))

def parse_state(state):
	new_state = BeliefState()
	new_state.isteamyellow = (state[0] == 'Y')
	new_state.ballPos = parse_pos_rand(state[1])
	for ind in range(2,8):
		new_state.homePos[ind - 2] = parse_pos_rand(state[ind])
	for ind in range(9,15):
		new_state.awayPos[ind - 9] = parse_pos_rand(state[ind])
	return new_state


def get_instance(state):
	try:
		return sample_states[state]
	except KeyError:
		sample_states[state] = parse_state(state)
		return sample_states[state]