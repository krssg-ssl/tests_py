from krssg_ssl_msgs.msg import BeliefState
from random import randint, random
import geometry_msgs

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

PI = 3.14159265358979323

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

	return (randint(x_min, x_max), randint(y_min, y_max), random()*2*PI)

def parse_state(state):
	new_state = BeliefState()
	new_state.isteamyellow = (state[0] == 'Y')
	new_state.ballPos.x, new_state.ballPos.y, new_state.ballPos.theta = parse_pos_rand(int(state[1]))
	for ind in range(2,8):
		new_state.homePos.append(geometry_msgs.msg._Pose2D.Pose2D(*parse_pos_rand(int(state[ind]))))
	for ind in range(8,14):
		new_state.awayPos.append(geometry_msgs.msg._Pose2D.Pose2D(*parse_pos_rand(int(state[ind]))))
	return new_state


def get_instance(state):
	if state not in sample_states:
		print "Creating new instance: "+state
		sample_states[state] = parse_state(state)
	return sample_states[state]