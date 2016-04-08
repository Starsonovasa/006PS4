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
from boto.dynamodb.condition import NULL

# start is a state, a 3-tuple (x, y, z) where 0 <= x, y, z <= k
# transitions is a list of 2-tuples of 3-tuples (x, y, z)
#   where 0 <= x, y, z <= k.
# Note that the start state is reachable through a path of length 0.
def reachable_states(start, transitions):
#     #Each key is the first state of a transition. The values of the keys are lists of all the
#     #neighbors of that key
#     adjacency = {}
#     
#     #Want an easilty iterable list of all the source states of the adjacency dictionary
#     #Since searching for all of the keys of the dictionary depends on the size of the
#     #Hash table backing the dictionary
#     source_states = []
#     for transition in transitions:
#         if transition(0) not in source_states:
#             source_states.append(transition(0))
#         adjacency[transition(0)].append(transition(1))
#         
#     #Adjacency list taken care of
#     
#     def reachable_BFS(vertices, adjacency_dict, source_vertex):
#         level = {}
#         parent = {}
#         level[source_vertex] = 0
#         
#         for vertex in vertices:
#             if not(vertex.equal(source_vertex)):
#                 level[vertex] = float("inf")
#             parent[vertex] = NULL
#         
#         frontier = []
#         frontier[0] = source_vertex
#         
#         while len(frontier) > 0:
#             current_vertex = frontier.pop(0)
#             for vertex in adjacency_dict[current_vertex]:
#                 if level[vertex].equal(float("inf")):
#                     level[vertex] = level[current_vertex] + 1
#                     parent[vertex] = current_vertex
#                     frontier.append(vertex)
#         reachable = []   
#         #Add the start state and it's zero length path
#         reachable.append((source_vertex, level[source_vertex], source_vertex))  
#         
#         #Add states that have non-infinite levels to the list of reachable states,
#         #in tuple form listing (state, level, parent)       
#         for vertex in vertices:
#             if not(level[vertex].equal(float("inf"))):
#                 reachable.append((vertex, level[vertex], parent[vertex]))
#                 
#                 
#         return reachable
#     return reachable_BFS(source_states, adjacency, start)
    pass


# Returns either a path as a list of reachable states if the target is
# reachable or False if the target isn't reachable.
def simple_machine(k, start, target):
    # TODO: Implement part b.
    pass

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
