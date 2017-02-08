# search.py
# ---------
# Licensing Information: Please do not distribute or publish solutions to this
# project. You are free to use and extend these projects for educational
# purposes. The Pacman AI projects were developed at UC Berkeley, primarily by
# John DeNero (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# For more info, see http://inst.eecs.berkeley.edu/~cs188/sp09/pacman.html

"""
In search.py, you will implement generic search algorithms which are called 
by Pacman agents (in searchAgents.py).
"""

# Authors: Implementation finished by Sean Hendryx and Kathy Dudding
# References: Stuart Russell and Peter Norvig (2010). Artificial Intelligence: A Modern Approach
#(3rd Edition); http://eddmann.com/posts/depth-first-search-and-breadth-first-search-in-python/; 

import util

class SearchProblem:
  """
  This class outlines the structure of a search problem, but doesn't implement
  any of the methods (in object-oriented terminology: an abstract class).
  
  You do not need to change anything in this class, ever.
  """
  
  def getStartState(self):
     """
     Returns the start state for the search problem 
     """
     util.raiseNotDefined()
    
  def isGoalState(self, state):
     """
       state: Search state
    
     Returns True if and only if the state is a valid goal state
     """
     util.raiseNotDefined()

  def getSuccessors(self, state):
     """
       state: Search state
     
     For a given state, this should return a list of triples, 
     (successor, action, stepCost), where 'successor' is a 
     successor to the current state, 'action' is the action
     required to get there, and 'stepCost' is the incremental 
     cost of expanding to that successor
     """
     util.raiseNotDefined()

  def getCostOfActions(self, actions):
     """
      actions: A list of actions to take
 
     This method returns the total cost of a particular sequence of actions.  The sequence must
     be composed of legal moves
     """
     util.raiseNotDefined()
           

def tinyMazeSearch(problem):
  """
  Returns a sequence of moves that solves tinyMaze.  For any other
  maze, the sequence of moves will be incorrect, so only use this for tinyMaze
  """
  from game import Directions
  s = Directions.SOUTH
  w = Directions.WEST
  return  [s,s,w,s,w,w,s,w]


class Node:
  """
  Search-tree node, data structure class for storing essential components of search tree nodes
  thus allowing for backtracking and reconstructing a path
  """
  def __init__(self, state, parent=None, action=None, pathCost=0):
    self._state = state
    self._parent = parent
    self._action = action
    self._pathCost = pathCost
  
  def State(self):
    return self._state
  
  def Parent(self):
    return self._parent
  
  def Action(self):
    return self._action
  
  def pathCost(self):
    return self._pathCost
  
  def getGoalPath(self):
    """
    Returns goal path ACTIONS by reconstructing path from goal state node in search tree to start node
    """
    # soln (solution) node is current node
    soln = self
    #instantiate empty path list
    path = [] 
    while soln.Parent():
      path.append(soln.Action())         
      #update soln to be soln's parent:
      soln = soln.Parent()
    #return path in reverse with [::-1]
    return path[::-1]  


def graphSearch(problem, frontier):
  """
  General graph-search algorithm that will be called by some variants of uninformed search such as DFS and BFS
  """
  print "Start:", problem.getStartState()
  print "Is the start a goal?", problem.isGoalState(problem.getStartState())
  print "Start's successors:", problem.getSuccessors(problem.getStartState())
  
  # push start state onto frontier (aka fringe):
  frontier.push(Node(problem.getStartState()))
  # Initialize explored set as empty list:
  explored = []
  #here
  while not frontier.isEmpty():
    # pop search node from frontier and put it into parent variable (note that this removes the search node "parent" from frontier):
    parent = frontier.pop()
    # check if current node in search tree is goal state:
    if problem.isGoalState(parent.State()):
      #and if so, return the path from the goal to the start:
      print "\n", "Found solution state!", "\n"
      print "Solution state: ", "\n", parent.State()
      return parent.getGoalPath()
    #if current node in search tree (parent) is not in explored set:  
    if parent.State() not in explored:
      #then add state to explored set
      explored.append(parent.State()) 
      # get all successors/children and push them onto frontier as Node instance:
      for child in problem.getSuccessors(parent.State()):
        # recall that Node data structure is:
        # (state, parent, action, pathCost)
        # and the successor's data structure is:
        # Start's successors: [((5, 4), 'South', 1), ((4, 5), 'West', 1)]
        frontier.push(Node(child[0],parent,child[1],parent.pathCost() + child[2]))
  #
  #Or return empty list:
  return []

  """
  # Initialize explored set as empty list:
  explored = []
  print "[(problem.getStartState(), \"Stop\", 0)] \n", [(problem.getStartState(), "Stop", 0)], "\n"
  print "frontier.push([(problem.getStartState(), \"stop\", 0)]) \n", frontier.push([(problem.getStartState(), "Stop", 0)]), "\n"
  print "frontier \n", frontier
  print "frontier.isEmpty() \n", frontier.isEmpty(), "\n"
  """


def depthFirstSearch(problem):
  """
  Search the deepest nodes in the search tree first [p 85].
  
  Your search algorithm needs to return a list of actions that reaches
  the goal.  Make sure to implement a graph search algorithm [Fig. 3.7].
  
  To get started, you might want to try some of these simple commands to
  understand the search problem that is being passed in:
  
  print "Start:", problem.getStartState()
  print "Is the start a goal?", problem.isGoalState(problem.getStartState())
  print "Start's successors:", problem.getSuccessors(problem.getStartState())
  """
  "*** YOUR CODE HERE ***"

  # instantiate frontier (aka fringe) as Stack object which will thus implement DFS given that Stack is LIFO
  frontier = util.Stack()
  return graphSearch(problem, frontier)
  
  #util.raiseNotDefined()

def breadthFirstSearch(problem):
  "Search the shallowest nodes in the search tree first. [p 81]"
  "*** YOUR CODE HERE ***"
  #instantiate frontier as util.Queue() object thus implementing BFS due to FIFO queuing policy
  frontier = util.Queue()
  return graphSearch(problem, frontier)
  util.raiseNotDefined()
      
def uniformCostSearch(problem):
  "Search the node of least total cost first. "
  "*** YOUR CODE HERE ***"
  #Define cost function as the cost of actions from problem.getCostOfActions()
  #def costFunction(problem):
  #  return problem.getCostOfActions([])
  #cost = lambda path: problem.getCostOfActions([x[1] for x in path])
  #def getPathCost(problem):
  #  here
  #frontier = util.PriorityQueueWithFunction(getPathCost)
  #return graphSearch(problem, frontier)
  #util.raiseNotDefined()
  print "Start:", problem.getStartState()
  print "Is the start a goal?", problem.isGoalState(problem.getStartState())
  print "Start's successors:", problem.getSuccessors(problem.getStartState())
  
  #instantiate frontier as PriorityQueue
  frontier = util.PriorityQueue()
  
  # push start state onto frontier (aka fringe):
  frontier.push(Node(problem.getStartState()),0)
  # Initialize explored set as empty list:
  explored = []
  #here
  while not frontier.isEmpty():
    # pop search node from frontier and put it into parent variable (note that this removes the search node "parent" from frontier):
    parent = frontier.pop()
    # check if current node in search tree is goal state:
    if problem.isGoalState(parent.State()):
      #and if so, return the path from the goal to the start:
      print "\n", "Found solution state!", "\n"
      print "Solution state: ", "\n", parent.State()
      return parent.getGoalPath()
    #if current node in search tree (parent) is not in explored set:  
    if parent.State() not in explored:
      #then add state to explored set
      explored.append(parent.State()) 
      # get all successors/children and push them onto frontier as Node instance:
      for child in problem.getSuccessors(parent.State()):
        # recall that Node data structure is:
        # (state, parent, action, pathCost)
        # and the successor's data structure is:
        # Start's successors: [((5, 4), 'South', 1), ((4, 5), 'West', 1)]
        #Make totalPathCost variable for adding to Node objects in frontier and for setting queueing priority order:
        totalPathCost = parent.pathCost() + child[2]
        frontier.push(Node(child[0],parent,child[1],totalPathCost), totalPathCost)
  #
  #Or return empty list:
  return []

def nullHeuristic(state, problem=None):
  """
  A heuristic function estimates the cost from the current state to the nearest
  goal in the provided SearchProblem.  This heuristic is trivial.
  """
  return 0

def aStarSearch(problem, heuristic=nullHeuristic):
  "Search the node that has the lowest combined cost and heuristic first."
  "*** YOUR CODE HERE ***"
  print "Start:", problem.getStartState()
  print "Is the start a goal?", problem.isGoalState(problem.getStartState())
  print "Start's successors:", problem.getSuccessors(problem.getStartState())
  #Code is mostly the same as UCS save that heuristic function has been added with totalPathCost to make priority variable
  #instantiate frontier as PriorityQueue
  frontier = util.PriorityQueue()
  
  # push start state onto frontier (aka fringe):
  frontier.push(Node(problem.getStartState()),0)
  # Initialize explored set as empty list:
  explored = []
  #here
  while not frontier.isEmpty():
    # pop search node from frontier and put it into parent variable (note that this removes the search node "parent" from frontier):
    parent = frontier.pop()
    # check if current node in search tree is goal state:
    if problem.isGoalState(parent.State()):
      #and if so, return the path from the goal to the start:
      print "\n", "Found solution state!", "\n"
      print "Solution state: ", "\n", parent.State()
      return parent.getGoalPath()
    #if current node in search tree (parent) is not in explored set:  
    if parent.State() not in explored:
      #then add state to explored set
      explored.append(parent.State()) 
      # get all successors/children and push them onto frontier as Node instance:
      for child in problem.getSuccessors(parent.State()):
        # recall that Node data structure is:
        # (state, parent, action, pathCost)
        # and the successor's data structure is:
        # Start's successors: [((5, 4), 'South', 1), ((4, 5), 'West', 1)]
        #Make totalPathCost variable for adding to Node objects in frontier and for setting queueing priority order:
        totalPathCost = parent.pathCost() + child[2]
        #Set priority of priority queue with f(n), which is g(n) + h(n), which is totalPathCost plus hueristic function
        priority = totalPathCost + heuristic(child[0], problem)
        frontier.push(Node(child[0],parent,child[1],totalPathCost), priority)
  #
  #Or return empty list:
  return []
  util.raiseNotDefined()
    
  
# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch