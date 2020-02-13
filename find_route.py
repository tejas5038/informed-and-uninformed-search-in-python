import sys
from queue import PriorityQueue
Graph = {}
Graph1 = {}
parent = {}
distance={}
argument_list_length = len(sys.argv)
f = sys.argv[1]    
a= sys.argv[2]
b = sys.argv[3]

				   

filename = open(f,'r')


for line in filename:
	if(line!="END OF INPUT"):
		node1, node2, weight = line.split()
		Graph.setdefault(node1, []).append((node2, weight))
		Graph.setdefault(node2, []).append((node1, weight))
   
dclist = []

	   
def backtrace(parent, start, end):
	path = [end]
	#print("end"+str(path))
	while path[-1] != start:
		path.append(parent[path[-1]]) 
	path.reverse()
	a = len(path) 
	s=""
	 
	for i in range(0,(a-1)):
		l=Graph[path[i]] 
		for j in range(0,len(l)):
			if(l[j][0]==path[i+1]):
				dis=l[j][1]
		s=s+path[i]+"\t"+"to"+ "\t"+path[i+1]+","+dis+" km"+"\n"

		#print(str(path[i])+"\t to \t"+str(path[i+1]))
	return s
def astar_search(Graph, start, goal):
	p=uninf_ucs(Graph,start,goal,1)
	expanded =0
	visited = []
	#parent = []
	queue = PriorityQueue()
	queue.put((0,0,start))
	x=0
	mq=0
	while queue:
		if(queue.qsize()>=mq):
			mq=queue.qsize()
		if(queue.qsize()==0):
			print("node expanded :"+str(x))
			print("node generated :"+str(expanded))
			print("node in memory :"+str(mq))
			print("distance: NIL")
			print("route : NIL")

			return
		h_cost,cost, node = queue.get()
		x=x+1
		if node not in visited:
		   
			visited.append(node)

			if node == goal:
				print("node expanded :"+str(x))
				print("node generated :"+str(expanded))
				print("max node in memory :"+str(mq))
				print("distance:"+str(cost)) 
				print("route:")
				print(p)
				#print(parent)
				#print(p)
				return
   
			for neighbour in Graph[node]:
				expanded+=1 
				h_cost = float(cost) + float(neighbour[1])+ float(Graph1[neighbour[0]][0])
				#print("dc list:",dclist)
				if(neighbour[0] not in dclist):
					parent[neighbour[0]] = node
					distance[neighbour[0]]=h_cost
					dclist.append(neighbour[0])
				else:
					if(h_cost<=distance[neighbour[0]]):
						parent[neighbour[0]] = node
						distance[neighbour[0]]=h_cost
			   
				cost1 = float(cost) + float(neighbour[1])
				#print(neighbour[0])
				parent[neighbour[0]] = node                    
				queue.put((h_cost,cost1,neighbour[0]))
def uninf_ucs(Graph, start, goal,x1=0):
	expanded =0
	visited = []
	queue1 = PriorityQueue()
	queue1.put((0,start))
	x=0
	mq=0
	while queue1:
		if(queue1.qsize()>=mq):
			mq=queue1.qsize()
		if(queue1.qsize()==0):
			if(x1==0):
				print("node expanded :"+str(x))
				print("node generated :"+str(expanded))
				print("max node in memory :"+str(mq))
				print("distance: NIL")
				print("route : NIL")
			else:
					p = backtrace(parent,a,b)
					return p
			return
		cost,node=queue1.get()
		x=x+1
		if node not in visited:
			visited.append(node)

			if node == goal:
				if(x1==0):
					print("node expanded :"+str(x))
					print("node generated :"+str(expanded))
					print("max node in memory :"+str(mq))
					print("distance:"+str(cost))
					#print(parent)
					print("route:")
					p = backtrace(parent,a,b)
					print(p)
				else:
					p = backtrace(parent,a,b)
					return p
				#print(p)
				return
		   
			#print("parent",node)
			#print("children")
			for neighbour in Graph[node]:
			   
				expanded+=1
				#print(visited) 
					#print(neighbour)
				total_cost = float(cost) + float(neighbour[1])
				#print("dc list:",dclist)
				if(neighbour[0] not in dclist):
					parent[neighbour[0]] = node
					distance[neighbour[0]]=total_cost
					dclist.append(neighbour[0])
				else:
					if(total_cost<=distance[neighbour[0]]):
						parent[neighbour[0]] = node
						distance[neighbour[0]]=total_cost
				#print(neighbour[0])
				#print(parent[neighbour[0]])
				queue1.put((total_cost,neighbour[0]))

if(argument_list_length==4):
	uninf_ucs(Graph,a,b)
elif(argument_list_length==5):
	heuristic = sys.argv[4]
	f1 = open(heuristic, 'r')
	for l1 in f1:
		if(l1!="END OF INPUT"):
			x,z=l1.split()
			Graph1.setdefault(x,[]).append((z))
	astar_search(Graph,a,b)
else:
		print("next time please enter correct input")