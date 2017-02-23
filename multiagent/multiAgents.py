# multiAgents.py
# --------------
# Licensing Information: Please do not distribute or publish solutions to this
# project. You are free to use and extend these projects for educational
# purposes. The Pacman AI projects were developed at UC Berkeley, primarily by
# John DeNero (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# For more info, see http://inst.eecs.berkeley.edu/~cs188/sp09/pacman.html

from util import manhattanDistance
from game import Directions
import random, util

from game import Agent

class ReflexAgent(Agent):
  """
    A reflex agent chooses an action at each choice point by examining
    its alternatives via a state evaluation function.

    The code below is provided as a guide.  You are welcome to change
    it in any way you see fit, so long as you don't touch our method
    headers.
  """


  def getAction(self, gameState):
    """
    You do not need to change this method, but you're welcome to.

    getAction chooses among the best options according to the evaluation function.

    Just like in the previous project, getAction takes a GameState and returns
    some Directions.X for some X in the set {North, South, West, East, Stop}
    """
    # Collect legal moves and successor states
    legalMoves = gameState.getLegalActions()

    # Choose one of the best actions
    scores = [self.evaluationFunction(gameState, action) for action in legalMoves]
    bestScore = max(scores)
    bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore]
    chosenIndex = random.choice(bestIndices) # Pick randomly among the best

    "Add more of your code here if you want to"

    return legalMoves[chosenIndex]

  def evaluationFunction(self, currentGameState, action):
    """
    Design a better evaluation function here.

    The evaluation function takes in the current and proposed successor
    GameStates (pacman.py) and returns a number, where higher numbers are better.

    The code below extracts some useful information from the state, like the
    remaining food (oldFood) and Pacman position after moving (newPos).
    newScaredTimes holds the number of moves that each ghost will remain
    scared because of Pacman having eaten a power pellet.

    Print out these variables to see what you're getting, then combine them
    to create a masterful evaluation function.
    """
    # Useful information you can extract from a GameState (pacman.py)
    successorGameState = currentGameState.generatePacmanSuccessor(action)
    #print "successorGameState \n", successorGameState
    newPos = successorGameState.getPacmanPosition()
    #print "newPos \n", newPos
    oldFood = currentGameState.getFood()
    #print "oldFood \n", oldFood
    newGhostStates = successorGameState.getGhostStates()
    #print "newGhostStates \n", newGhostStates
    newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]
    #print "newScaredTimes \n", newScaredTimes

    "*** YOUR CODE HERE ***"
    #print "successorGameState.getScore() \n", successorGameState.getScore()

    #make list of food that is left:
    foodList = oldFood.asList()

    #instantiate closestFoodDist to floating value of infinity
    closestFoodDist = float('inf')
    
    #First check if ghost is scared and close:

    ghostScore = 0.
    for state in newGhostStates:
      #print "state.scaredTimer \n", state.scaredTimer
      #compute distance to ghost_i
      dist_g = manhattanDistance(newPos, state.getPosition())
      #if, on proposed move, ghost is still scared and distance to ghost is 0:
      if state.scaredTimer > 0 and dist_g == 0:
        ghostScore = 100000.
        #find manhattan distance to closest food
        for food in foodList:
          dist_f = manhattanDistance(food, newPos)
          if(dist_f < closestFoodDist):
            closestFoodDist = dist_f
        return ghostScore + (1./closestFoodDist)
      #else if the ghost is catchable and dist to ghost is greater than zero on next move:  
      elif dist_g < state.scaredTimer:
        ghostScore = 10000. + (1./dist_g)
        return ghostScore
      #else if ghosts are not catchable and are too close, ascribe negative value:  
      elif dist_g < 3:
        ghostScore = -1. * dist_g

    #find manhattan distance to closest food
    for food in foodList:
      dist_f = manhattanDistance(food, newPos)
      if(dist_f < closestFoodDist):
        closestFoodDist = dist_f

    # compute reflex heuristic:
    score = 3./(-1. + ghostScore) + 1./(10. + closestFoodDist)
    return score

def scoreEvaluationFunction(currentGameState):
  """
    This default evaluation function just returns the score of the state.
    The score is the same one displayed in the Pacman GUI.

    This evaluation function is meant for use with adversarial search agents
    (not reflex agents).
  """
  return currentGameState.getScore()

class MultiAgentSearchAgent(Agent):
  """
    This class provides some common elements to all of your
    multi-agent searchers.  Any methods defined here will be available
    to the MinimaxPacmanAgent, AlphaBetaPacmanAgent & ExpectimaxPacmanAgent.

    You *do not* need to make any changes here, but you can if you want to
    add functionality to all your adversarial search agents.  Please do not
    remove anything, however.

    Note: this is an abstract class: one that should not be instantiated.  It's
    only partially specified, and designed to be extended.  Agent (game.py)
    is another abstract class.
  """

  def __init__(self, evalFn = 'scoreEvaluationFunction', depth = '2'):
    self.index = 0 # Pacman is always agent index 0
    self.evaluationFunction = util.lookup(evalFn, globals())
    self.depth = int(depth)

class MinimaxAgent(MultiAgentSearchAgent):
  """
    Your minimax agent (question 2)
  """

  def getAction(self, gameState):
    """
      Returns the minimax action from the current gameState using self.depth
      and self.evaluationFunction.

      Here are some method calls that might be useful when implementing minimax.

      gameState.getLegalActions(agentIndex):
        Returns a list of legal actions for an agent
        agentIndex=0 means Pacman, ghosts are >= 1

      Directions.STOP:
        The stop direction, which is always legal

      gameState.generateSuccessor(agentIndex, action):
        Returns the successor game state after an agent takes an action

      gameState.getNumAgents():
        Returns the total number of agents in the game
    """
    "*** YOUR CODE HERE ***"
    #here

    def getVal(self, gameState, searchDepth, agentIndex):
      #Function calls either maxVal or minVal depending on agentIndex
      #dive to next depth if traversed through all agents:
      if agentIndex == gameState.getNumAgents():
        searchDepth += 1
        agentIndex = 0

      actions = list(gameState.getLegalActions())

      # if no more actions to search through or searchDepth == self.depth:
      # return the value from the evaluation function
      if len(actions) == 0 or searchDepth == self.depth():
        return self.evaluationFunction(gameState)

      #If pacman agent (i.e. at max search node)
      if agentIndex == 0:
        return self.maxVal(gameState, searchDepth, agentIndex)

      return self.minVal(gameState, searchDepth, agentIndex)

    def maxVal(self, gameState, searchDepth, agentIndex):
      """
      Returns a list including the utility of the state from a proposed action and 
      and the action to get to that state
      """  


    #make decision by calling self.getVal which recursively calls maxVal or minVal 
    #depending on whether agent is pacman (agent index == 0) or ghost, respectively
    backedUpVal = self.getVal(gameState, 0, self.index)
    #return action:
    return backedUpVal[1]



class AlphaBetaAgent(MultiAgentSearchAgent):
  """
    Your minimax agent with alpha-beta pruning (question 3)
  """

  def getAction(self, gameState):
    """
      Returns the minimax action using self.depth and self.evaluationFunction
    """
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

class ExpectimaxAgent(MultiAgentSearchAgent):
  """
    Your expectimax agent (question 4)
  """

  def getAction(self, gameState):
    """
      Returns the expectimax action using self.depth and self.evaluationFunction

      All ghosts should be modeled as choosing uniformly at random from their
      legal moves.
    """
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def betterEvaluationFunction(currentGameState):
  """
    Your extreme ghost-hunting, pellet-nabbing, food-gobbling, unstoppable
    evaluation function (question 5).

    DESCRIPTION: <write something here so we know what you did>
  """
  "*** YOUR CODE HERE ***"
  util.raiseNotDefined()

# Abbreviation
better = betterEvaluationFunction

class ContestAgent(MultiAgentSearchAgent):
  """
    Your agent for the mini-contest
  """

  def getAction(self, gameState):
    """
      Returns an action.  You can use any method you want and search to any depth you want.
      Just remember that the mini-contest is timed, so you have to trade off speed and computation.

      Ghosts don't behave randomly anymore, but they aren't perfect either -- they'll usually
      just make a beeline straight towards Pacman (or away from him if they're scared!)
    """
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

