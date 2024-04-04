from matplotlib import pyplot as plt
from gridWorld import gridWorld
import numpy as np
import random


def show_action_value_function(env, Q, filename=None):
    pos = {"U": (-0.15, -0.3), "D": (-0.15, 0.4), "L": (-0.45, 0.1), "R": (0.05, 0.1)}
    fig = env.render(show_state = False, show_reward = False)            
    for k in env.states():
        s = env.legal_states[k]
        for i, a in enumerate(env.actions(k)):
            fig.axes[0].annotate("{0:.2f}".format(Q[k, i]), (s[1] + pos[a][0], s[0] + pos[a][1]), size = 40/env.board_mask.shape[0], color = "r" if Q[k, i] == max(Q[k, :]) else "k")
    if filename != None:
        plt.savefig(filename)
    plt.show()
    
def show_policy(env, Q, filename=None):
    fig = env.render(show_state = False, show_reward = False)
    action_map = {"U": "↑", "D": "↓", "L": "←", "R": "→"}
    for k in env.states():
        s = k if isinstance(k, tuple) else env.legal_states[k]
        if not env.terminal(s):
            fig.axes[0].annotate(action_map[env.actions(s)[np.argmax(Q[k, :])]], (s[1] - 0.1, s[0] + 0.1), size = 100/env.board_mask.shape[0])
    if filename != None:
        plt.savefig(filename)
    plt.show()


####################  Q-Learning ####################
def Q_Learning(env : gridWorld, gamma : float, Q : np.ndarray , alpha : float, epsilon : float):
    # Reset environment
    s, r, done = env.reset()
    """
    YOUR CODE HERE:
    Implement Q-Learning
    
    Input arguments:
        - env     Is the environment
        - gamma   Is the discount rate
        - Q       Is the Q table
        - alpha   Is the learning rate
        - epsilon Is the probability of choosing greedy action
    
    Some useful functions of the grid world environment
        - s_next, r, done = env.step(a)  Take action a and observe the next state, reward and environment termination
        - actions = env.actions()        List available actions in current state (is empty if state is terminal)
    """
    # The bellman equation:
    # bellman = lambda q, qe, r : q + alpha*(r + gamma * qe - q) 
    bellman = lambda q, qe, r : (1-alpha)*q + alpha*(r+gamma*qe)
    count = 0 
    while True:
        actions = env.actions(s)

        # Only accept valid actions
        actions = [x for x in actions if env.validateAction(x)]
        if len(actions)== 0:
            return Q
        
        idxs = [env.actionToIndex(a) for a in actions]
        
        # Epsilon greedy policy:
        # Choose the best action with a probability of epsilon, and random with a probability of 1-epsilon 
        rand = np.random.rand()
        if rand > epsilon:
            a_idx = np.random.randint(0, len(actions))
            a_idx = idxs[a_idx]
            global randomExploration
            randomExploration += 1
        else:
            # Find the index of the maximum value in Q[s,:]
            a_idx = np.argmax(Q[s,:])
            # a_idx = np.argmax([Q[s,x] for x in idxs]) # Very slow for some reason, and still not correct
            global bestAction
            bestAction += 1

        a = env.indexToAction(a_idx)
        
        # Take the action
        s_next, r, done = env.step(a, False)

        # Calculate the new Q value using the bellman equation
        q = Q[s, a_idx]
        q_e = np.max(Q[s_next,:])
        Q[s, a_idx] = bellman(q, q_e, r)

        # We have reached a terminal state, so we return 
        if done:
            return Q
        
        # Update the current state
        s, r, done = env.reset(s_next)
        # count += 1
        # print(f"Count: {count}")

def validatePositions(env : gridWorld):
    states = env.states()
    for state in states:
        actions = env.actions(state)
        legal = [x for x in actions if env.validateAction(x, state)]
        print(f"Legal actions for state: {state}")
        print(f"{legal}")

if __name__ == "__main__":
    """
    Note that this code requires the numpy and matplotlib packages.
    """
    randomExploration = 0
    bestAction = 0
    # Import the environment from file
    filename = "gridworlds/tiny.json"
    # filename = "gridworlds/large.json"
    env = gridWorld(filename)
    validatePositions(env=env)

    # Render image
    fig = env.render(show_state = True)
    plt.show()


    """
    (Run Q-Learning)
    
    Below is the code for running Q-Learning, feel free to change the code, and tweek the parameters.
    """
    gamma = 1.0     # Discount rate
    alpha = 0.1     # Learning rate
    epsilon = [0.9, 1.0, 0.5, 0.0]   # Probability of taking greedy action
    episodes = 5000 # Number of episodes
    # episodes = 1000

    for e in epsilon:
        Q = np.zeros([len(env.states()), 4])
        for i in range(episodes):
            print(i)
            Q_Learning(env, gamma, Q, alpha, e)

        action_name = "Action_Value_Function" + f"{e}.pdf"
        policy_name = "Policy" + f"{e}.pdf"

        # Render Q-values and policy 
        show_action_value_function(env, Q, action_name)
        show_policy(env, Q, policy_name)