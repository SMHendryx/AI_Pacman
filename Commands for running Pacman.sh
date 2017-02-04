#Note my path and python2.7 virtual env python2.7 
cd /Users/seanhendryx/githublocal/AI_Pacman/search
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


##################################################################################################
#update master branch on github repo with local changes:
git add .
git status
git commit -m "Updated search.py with BFS.  Added bash commands for running and"
git push origin master
