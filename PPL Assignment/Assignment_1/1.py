entity = ['goat', 'tiger', 'grass']
path = []


# Defines who can eat whom
def eats(x, y):
    if x == 'goat' and y == 'grass':
        return True
    elif x == 'tiger' and y == 'goat':
        return True
    else:
        return False


# Defines if a pair of entities is safe to be left alone on one side of the river.
def safe_pair(x, y):
    if eats(x, y) or eats(y, x):
        return False
    else:
        return True


def state_of(who, state):
    try:
        return state[who]
    except KeyError:
        state[who] = False
        return False


# Verifies if the state defined as an dictionary is safe. If the goat is on the same side as the man, then we're safe.
# Otherwise if the grass or the tiger is also on the other side, then we're not safe.
def safe_state(state):
    if state_of('man', state) == state_of('goat', state):
        return True
    elif state_of('goat', state) == state_of('tiger', state):
        return False
    elif state_of('goat', state) == state_of('grass', state):
        return False
    else:
        return True


def move(who, state):
    if state[who] == 'left':
        state[who] = 'right'
    else:
        state[who] = 'left'
    return state


# Tests if the state has reached the goal. This is the case if all four entities are on the other side.
def goal_reach(state):
    if not state:
        return False
    return (state_of('man', state) == 'right' and
            state_of('goat', state) == 'right' and
            state_of('tiger', state) == 'right' and
            state_of('grass', state) == 'right')


# Checks if child is a safe state to move into, and if it is, it adds it to the list of states.
def check_add_child(child, list_states):
    if safe_state(child):
        list_states.append(child)
    return list_states


def expand_states(state):
    children = []
    child = state.copy()
    # the man can also move alone
    move('man', child)
    check_add_child(child, children)
    for ent in entity:
        # Move one object on the same side as the man
        if state_of(ent, state) == state_of('man', state):
            child = state.copy()
            move('man', child)
            move(ent, child)
            check_add_child(child, children)
    return children


# Searches for a solution from the initial state
def search_sol(state):
    path.append(state)
    next = state.copy()
    while next and not goal_reach(next):
        nl = expand_states(next)
        next = {}
        for child in nl:
            if not (child in path):
                next = child
                path.append(next)
                break
    return next


# Initialization of the global variables
initial_state = {}
initial_state['man'] = 'left'
for e in entity:
    initial_state[e] = 'left'

print("Initial state : ")
print(initial_state)

search_sol(initial_state)

# Evaluate the variable path to see the solution backwards.
print("The full path is:")
for s in path:
    print(s)