import heapq
 
def heuristic(node, goal):
	return 0
 
def greedy_best_first_search(graph, start, goal):
	open_list = [(heuristic(start, goal), start)]
	closed_set = set()
 
	while open_list:
    	_, current_node = heapq.heappop(open_list)
 
    	if current_node == goal:
        	return True  # Goal reached
 
    	closed_set.add(current_node)
 
    	for neighbor, _ in graph[current_node].items():
        	if neighbor not in closed_set:
            	heapq.heappush(open_list, (heuristic(neighbor, goal), neighbor))
 
	return False
graph = {
	'A': {'B': 5, 'C': 2},
	'B': {'A': 5, 'D': 4},
	'C': {'A': 2, 'D': 7},
	'D': {'B': 4, 'C': 7, 'E': 3},
	'E': {'D': 3, 'F': 1},
	'F': {'E': 1}
}
 
start_node = 'A'
goal_node = 'F'
result = greedy_best_first_search(graph, start_node, goal_node)

if result:
	print("Goal reached! Path found.")
else:
	print("Goal not reachable.")
