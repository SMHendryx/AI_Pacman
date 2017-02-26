#Note my path and python2.7 virtual env python2.7 


cd /Users/seanhendryx/githublocal/AI_Pacman/multiagent
#minimax
python2.7 pacman.py -p MinimaxAgent -l minimaxClassic -a depth=4
python2.7 pacman.py -p MinimaxAgent -l mediumClassic -a depth=4
python2.7 pacman.py -p MinimaxAgent -l trappedClassic -a depth=3
python2.7 pacman.py -p MinimaxAgent -l mediumClassic -a depth=4



python2.7 pacman.py ­-p ReflexAgent
python2.7 pacman.py -p ReflexAgent -l testClassic

python2.7 pacman.py -p ReflexAgent -l testClassic

python2.7 pacman.py --frameTime 0 -p ReflexAgent -k 1

python2.7 pacman.py -p ReflexAgent -l openClassic -n 10 -q





cd /Users/seanhendryx/githublocal/AI_Pacman/search
#test
python2.7 pacman.py
#DFS implementation should quickly find a solution for
#python2.7 pacman.py -l tinyMaze -p SearchAgent
#python2.7 pacman.py -l mediumMaze -p SearchAgent
python2.7 pacman.py -l bigMaze -z .5 -p SearchAgent


#BFS
python2.7 pacman.py -l mediumMaze -p SearchAgent -a fn=bfs

#UCS:
python2.7 pacman.py -l mediumMaze -p SearchAgent -a fn=ucs
python2.7 pacman.py -l mediumDottedMaze -p StayEastSearchAgent
python2.7 pacman.py -l mediumScaryMaze -p StayWestSearchAgent

#A*
cd /Users/seanhendryx/githublocal/AI_Pacman/search
python2.7 pacman.py -l bigMaze -z .5 -p SearchAgent -a fn=astar,heuristic=manhattanHeuristic 

#Finding all the corners:
cd /Users/seanhendryx/githublocal/AI_Pacman/search
python2.7 pacman.py -l tinyCorners -p SearchAgent -a fn=bfs,prob=CornersProblem

python2.7 pacman.py -l mediumCorners -p SearchAgent -a fn=bfs,prob=CornersProblem

#Test " Implement a heuristic for the CornersProblem in cornersHeuristic":
python2.7 pacman.py -l mediumCorners -p AStarCornersAgent -z 0.5

#eating all the dots
python2.7 pacman.py -l testSearch -p AStarFoodSearchAgent

python2.7 pacman.py -l trickySearch -p AStarFoodSearchAgent

#suboptimal search:
python2.7 pacman.py -l bigSearch -p ClosestDotSearchAgent -z .5 


##################################################################################################
#update master branch on github repo with local changes:
git add .
git status
git commit -m "implemented suboptimal search"
git push origin master
