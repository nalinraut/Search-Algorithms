######################################################################################################
# Notations used in code:
# M_L  : Missionaries on Left bank
# C_L  : Cannibals on Left bank
# boat : Location of boat (left/right bank)
# M_R  : Missionaries on Left bank
# C_R  : Cannibals on Left bank
# 
# 
######################################################################################################

import sys
import os
import math

class State:

	def __init__(self, parent, M_L, C_L, boat, M_R, C_R):				#Contains object of parent state which will be used 
																		#to trace back the path to initial state.

		self.parent = parent

		self.M_L = M_L
		self.C_L = C_L
		self.boat = boat
		self.M_R = M_R
		self.C_R = C_R

	def isValid(self):

		if self.M_L>=0 and self.C_L>=0 and self.M_R>=0 and self.C_R>=0 and\
		 (self.M_L>=self.C_L or self.M_L==0) and (self.M_R>=self.C_R or self.M_R==0):
			return True
		else:
			return False


	def __eq__(self, other):

		if self.M_L==other.M_L and self.C_L==other.C_L and self.M_R==other.M_R and self.C_R==other.C_R and self.boat==other.boat:
			return True
		else:
			return False

	def generateSuccessors(self):

		children = []

		if self.boat == 'Left':

			#######################################################################################################
			# Two Missionaries cross river
			child = State(self, self.M_L-2, self.C_L, 'Right', self.M_R+2, self.C_R)
			if child.isValid():
				children.append(child)
			#######################################################################################################
			# Two Cannibals cross river
			child = State(self, self.M_L, self.C_L-2, 'Right', self.M_R, self.C_R+2)
			if child.isValid():
				children.append(child)
			#######################################################################################################
			# One Missionaries crosses river
			child = State(self, self.M_L-1, self.C_L, 'Right', self.M_R+1, self.C_R)
			if child.isValid():
				children.append(child)
			#######################################################################################################
			# One Cannibals cross river
			child = State(self, self.M_L, self.C_L-1, 'Right', self.M_R, self.C_R+1)
			if child.isValid():
				children.append(child)
			#######################################################################################################
			# One Missionary and One Cannibal cross river
			child = State(self, self.M_L-1, self.C_L-1, 'Right', self.M_R+1, self.C_R+1)
			if child.isValid():
				children.append(child)
			#######################################################################################################

		else:

			#######################################################################################################
			# Two Missionaries cross river
			child = State(self, self.M_L+2, self.C_L, 'Left', self.M_R-2, self.C_R)
			if child.isValid():
				children.append(child)
			#######################################################################################################
			# Two Cannibals cross river
			child = State(self, self.M_L, self.C_L+2, 'Left', self.M_R, self.C_R-2)
			if child.isValid():
				children.append(child)
			#######################################################################################################
			# One Missionaries crosses river
			child = State(self, self.M_L+1, self.C_L, 'Left', self.M_R-1, self.C_R)
			if child.isValid():
				children.append(child)
			#######################################################################################################
			# One Cannibals cross river
			child = State(self, self.M_L, self.C_L+1, 'Left', self.M_R, self.C_R-1)
			if child.isValid():
				children.append(child)
			#######################################################################################################
			# One Missionary and One Cannibal cross river
			child = State(self, self.M_L+1, self.C_L+1, 'Left', self.M_R-1, self.C_R-1)
			if child.isValid():
				children.append(child)
			#######################################################################################################

		return children


	def isGoal(self):

		if self.M_R == 3 and self.C_R == 3:
			return True
		else:
			return False


def BFS(state):

	queue = []
	exploredStates = []

	if state.isGoal():
		return state

	queue.append(state)

	while len(queue)!=0:

		currState = queue.pop(0)
#		printState(currState)

		if currState.isGoal():
			return currState

		exploredStates.append(currState)
		children = currState.generateSuccessors()

		for child in children:
			if (child not in queue) or (child not in exploredStates):
				queue.append(child)
#				printState(child)

#		print "#####################################################"


def printState(state):

	print "------------------------------"
	for i in range(state.M_L):
		sys.stdout.write('M')
	for i in range(state.C_L):
		sys.stdout.write('C')
	

	if state.boat == 'Left':
		print "\t",
		print "Boat","\t\t",
	else:
		print "\t\t"," Boat",
		print "  ",

	for i in range(state.M_R):
		sys.stdout.write('M')
	for i in range(state.C_R):
		sys.stdout.write('C')

	print "\n======\t\t\t======"
	print "------------------------------\n"

def printSequence(goal):

	sequence = []
	sequence.append(goal)

	parent = goal.parent
	while parent != None:
		sequence.insert(0,parent)
		parent = parent.parent

	for state in sequence:
		printState(state)

def main():

	os.system("clear")

	print "Missionaries-Cannibals Problem using BFS"
	print "----------------------------------------\n"

	initialState = State(None, 3, 3, 'Left', 0, 0)		#Initial state with No parent node and all missionaries, cannibals and boat on left

	goalState = BFS(initialState)

	print "SOLUTION SEQUENCE\n"

	printSequence(goalState)



main()