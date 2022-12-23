# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [w,s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
		
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
    
    #########################################################################################

    #Pseudo code for DFS
    #1. Create a node to store the starting state and PUSH it in a STACK.
    #2. POP the node from the STACK and replace it with its children. 
    #3. Check if we have a goal in the stack, if yes then return the path and if no then continue expanding.
    #4. Repeat while saving the information of the parent nodes.
    #5. The STACK works in LIFO strategy so the algorithm will go deep until the end of the branch.
    #6. Once we reach a goal node the program will return the path and exit.
    #7. If there was no goal encountered then the program will return failure.

    ########################################################################################

    util.raiseNotDefined()

def breadthFirstSearch(problem):

    #########################################################################################

    #Pseudo code for BFS
	#1. Create a node to store the starting state and save it in a QUEUE.
	#2. Remove the node from the QUEUE and replace it with its children. 
	#3. Check if we have a goal in the queue, if yes then return the path and if no then continue expanding.
	#4. Repeat while saving the information of the parent nodes.
	#5. The QUEUE works in FIFO strategy so the algorithm will scan nodes level by level.
	#6. Once we reach a goal node the program will return the path and exit.
	#7. If there was no goal encountered then the program will return failure.
	
    ##########################################################################################

    util.raiseNotDefined()

    
def uniformCostSearch(problem):

    """Search the node of least total cost first."""

    ##########################################################################################

    #Pseudo code for UCS
	#1. Create a node to store the the starting state and the cost to each child and save in a priority queue.
	#2. Compare the costs and choose the child with the least cost.
	#3. Expand the least cost node and ADD the value of the path to the child to the current cost.
	#4. Compare the costs again and choose the least one and expand it.
	#5. Every time we expand, we check if there is a GOAL and we store the path.
	#6. Repeat until the goal is found and then return the path
    #7. If there are no more nodes to expand then return failure.

    ##########################################################################################

    util.raiseNotDefined()
    
def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):

    """Search the node that has the lowest combined cost and heuristic first."""

    #########################################################################################

    #Pseudo code for A* search
    #1. Create a node to store the starting state and the cost to each child and their heuristic and save in a priority queue.
    #2. Compare the value of f(n) = g(n) + h(n) and choose the child with the least sum. 
    #3. Expand the least sum node and check f(n) of the children.
    #4. Compare the sums again and choose the least one and expand it.
    #5. Every time we expand we check if there is a GOAL and we store the path.
    #6. Repeat until the goal is found and then return the path.
    #7. If there are no more nodes to expand, then return failure.

    ##########################################################################################

    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
