#Note my path and python2.7 virtual env python2.7 
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



##################################################################################################
#update master branch on github repo with local changes:
git add .
git status
git commit -m "Implemented CornersProblem search problem in searchAgents.py"
git push origin master
