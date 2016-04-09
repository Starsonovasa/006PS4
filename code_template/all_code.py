################################################################################
#
# States are represented by 3-tuples of integers in the range 0, ..., k.
#
# Transitions are 2-tuples of states (start_state, end_state), where start_state
# is the start of the transition and end_state is the end of the transition.
#
# Reachable states should be represented by a 3-tuple (state, length, previous)
# where state is the reachable state, length is the length of the path to get
# there, and previous is the previous state. For the 0 length path to the start,
# that would be (start, 0, start).
#
################################################################################


# start is a state, a 3-tuple (x, y, z) where 0 <= x, y, z <= k
# transitions is a list of 2-tuples of 3-tuples (x, y, z)
#   where 0 <= x, y, z <= k.
# Note that the start state is reachable through a path of length 0.
def reachable_states(start, transitions):
    #Each key is the first state of a transition. The values of the keys are lists of all the
    #neighbors of that key
    adjacency = {}
     
    #Want an easilty iterable list of all the source states of the adjacency dictionary
    #Since searching for all of the keys of the dictionary depends on the size of the
    #Hash table backing the dictionary
    states = {}
    states_list = []
    for transition in transitions:
        #Originally, I was checking to see if a state that I wanted to add was already in a list
        #of states. I realized that the search time of a list is too long. Therefore, I made a dummy
        #dictionary where the states are the keys and the values are empty lists. In doing so,
        #I could use the function get(key, default) to check if I already have a state. If the state is
        #not a key in my dummy dictionary, the get method returns the default value (which here I chose to
        #be infinity). Then, I can add that state to both my dummy dictionary and to a list of states so that
        #I never have duplicate elements in my list of states.
        
        if adjacency.get(transition[0], float("inf")) == float("inf"):
            adjacency[transition[0]] = []
            
        adjacency[transition[0]].append(transition[1])
        
        #Add source states to the total list of states
        if states.get(transition[0], float("inf")) == float("inf"):
            states[transition[0]] = []
            states_list.append(transition[0])
            
        #Add destination states to the total list of states    
        if states.get(transition[1], float("inf")) == float("inf"):
            states[transition[1]] = []
            states_list.append(transition[1])
         
    #Adjacency list taken care of
     
    def reachable_BFS(vertices, adjacency_dict, source_vertex):
        level = {}
        parent = {}
        level[source_vertex] = 0
         
        for vertex in vertices:
            if not(vertex == source_vertex):
                level[vertex] = float("inf")
            parent[vertex] = None
         
        frontier = []
        frontier.append(source_vertex)
        
        reachable = []   
        #Add the start state and it's zero length path
        reachable.append((source_vertex, level[source_vertex], source_vertex))
        while len(frontier) > 0:
            current_vertex = frontier.pop(0)
            neighbors = adjacency_dict.get(current_vertex, [])
            if len(neighbors) > 0:
                for vertex in adjacency_dict[current_vertex]:
                    if level.get(vertex) == (float("inf")):
                        level[vertex] = level[current_vertex] + 1
                        parent[vertex] = current_vertex
                        frontier.append(vertex)
                        reachable.append((vertex, level[vertex], current_vertex))
          
         
#         #Add states that have non-infinite levels to the list of reachable states,
#         #in tuple form listing (state, level, parent)       
#         for vertex in vertices:
#             if not(level[vertex] == float("inf")):
#                 reachable.append((vertex, level[vertex], parent[vertex]))
#                  
                 
        return reachable
    value = reachable_BFS(states_list, adjacency, start)
    return value



# Returns either a path as a list of reachable states if the target is
# reachable or False if the target isn't reachable.
def simple_machine(k, start, target):
    rules = [(1,1,1),(-1,-1,-1), (1,0,0), (-1,0,0)]
    def transitions(start, rules, limit = -1):
        transitions_list = []
        
        #Default value is -1, no upper bound on the value for each component of the 
        #intial or final state
        if limit <= -1:
            for rule in rules:
                final = (start[0]+rule[0], start[1]+rule[1], start[2]+rule[2])
                transitions_list.append((start,final))
            return transitions_list
        
        #Otherwise, every component of the inital and final state must be below the limit
        else:
            #If any component of the start state is above the limit, then it already violated
            #our precondition
            for component in start:
                if component > limit:
                    return transitions_list
                    
            
            for rule in rules:
                final = (start[0]+rule[0], start[1]+rule[1], start[2]+rule[2])
                above_limit = False
                
                #If any component of the final state after the transition is above the limit,
                #then it is not reachable
                for component in final:
                    if component > limit:
                        above_limit = True
                
                if not(above_limit):
                    transitions_list.append((start, final))
        return transitions_list
    
    #BFS
    frontier = []
    frontier.append(start)
    parent = {}
    visited = set()
    
    parent[start] = None
    
    while(len(frontier) > 0):
        current_state = frontier.pop(0)
        transitions = transitions(current_state, rules, k)
        reachable = reachable_states(current_state, transitions)
        
        for single_length_path in reachable:
            destination = single_length_path[0]
            parent[destination] = single_length_path[2]
            if destination ==  target:
                return shortest_path(destination, parent)
            
            if destination not in visited:
                visited.add(destination)
                frontier.append(destination)
    
    return False
    
    def shortest_path(destination, parent_dict):
        frontier = []
        frontier.append(destination)
        list_in_reverse = []
        while (frontier[0] != None) and (len(frontier) > 0):
            current_node = frontier.pop(0)
            list_in_reverse.append(current_node)
            frontier.append(parent[current_node])
        return list_in_reverse.reverse()
    

# Returns either False if the mutual exclusion property is satisfied or
# a minimum-length counterexample as a list of reachable states.
def mutual_exclusion_1():
    # TODO: Implement part c.
    pass

# Returns either False if the mutual exclusion property is satisfied or
# a minimum-length counterexample as a list of reachable states.
def mutual_exclusion_2():
    # TODO: Implement part d.
    pass
