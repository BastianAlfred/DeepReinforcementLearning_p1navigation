# Deep Reinforcment Learning @ UDACITY --> Project 1 "Navigation"

### 1. Learning Algorithm
To solve our "Navigation" task a Deep Q-Learning agent with experience reply is used.\
The algorithm is explained in the following picture out of the DQN Nature Paper "Human-level control through deep reinforcement learning".

![algorithm](algorithm.jpg)

Our agent improves his choosen actions by exploring (with e-greedy policy) the presented state and choose appropriate action to maximize cumulative reward (due to a high GAMMA value the agent cares mainly for future rewards). 


Following Hyperparameters were used to train the agent (carry over from previous project "dqn")
- BUFFER_SIZE = int(1e5)  # replay buffer size
- BATCH_SIZE = 64         # minibatch size
- GAMMA = 0.99            # discount factor
- TAU = 0.001             # for soft update of target parameters
- LR = 0.0005             # learning rate 
- UPDATE_EVERY = 4        # how often to update the network
- LAYERS = 64             # depth of fully connected layers


To keep the model architecture lean and to bring not too much complexity in the non linear function approximator for the Q-table a simple neural network with the following architecture is used (carry over from previous project "dqn")
- __1__ fully connected __input layer__ with ReLu activation function 
- __1__ fully connected  __hidden layer__ with ReLu activation function 
- __1__ fully connected __output layer__


### 2. Plot rewards
Here you can see the progress of rewards the agent collects over several episodes.

![reward](reward.jpg)

Episode 100	Average Score: 0.92\
Episode 200	Average Score: 3.99\
Episode 300	Average Score: 6.98\
Episode 400	Average Score: 10.17\
Episode 500	Average Score: 12.55\
Episode 524	Average Score: 13.06\
Environment solved in 424 episodes!	Average Score: 13.06

### 3. Ideas for future Work
To imporve the agents learning performance the following can be done:
- a further detailled scan of the choosen hyperparameters
- implement 'Double DQN'
- implement 'Prioritized Experience Reply'
- implement 'Dueling DQN'
- implement 'Rainbow DQN'