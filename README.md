# Deep Reinforcment Learning @ UDACITY --> Project 1 "Navigation"

### 1. Getting Started
To run the code in this repository please follow the listed instructions:

- __Step 1__ - Set up python requirements:  https://github.com/udacity/deep-reinforcement-learning#dependencies
    - `Problem`: During installation the following ERROR occured: 'Could not find a version that satisfies the requirement torch==0.4.0 (from unityagents)'
    - `Solution`: 
            - in Windows Explorer open \deep-reinforcement-learning\python\requirements.txt
            - remove the line 'torch==0.4.0', save and close
            - on Anaconda
                - conda install pytorch=0.4.0 -c pytorch
                - cd deep-reinforcement-learning/python
                - pip install .
    
- __Step 2__ - Set up UNITY ML environment: https://github.com/udacity/deep-reinforcement-learning/blob/master/p1_navigation/README.md

### 2. Project Details
For this project we use a framework from [UNITY](https://unity.com/de). The __UNITY Machine Learning Agents (ML-Agents)__ is an open-source Unity plugin that enables games and simulations to serve as environments for training intelligent agents. In the "Navigation" - Project, we will train an agent to navigate (and collect bananas!) in a large, square world. A reward of +1 is provided for collecting a yellow banana, and a reward of -1 is provided for collecting a blue banana. Thus, the goal of your agent is to collect as many yellow bananas as possible while avoiding blue bananas.

The state space has 37 dimensions and contains the agent's velocity, along with ray-based perception of objects around the agent's forward direction. Given this information, the agent has to learn how to best select actions. Four discrete actions are available, corresponding to:

- `0` - move forward.
- `1` - move backward.
- `2` - turn left.
- `3` - turn right.

The task is episodic, and in order to solve the environment, our agent must get an average score of +13 over 100 consecutive episodes.

### 3. Instructions
The repo contain´s 3 mandatory files for our agent
- "Main.ipynb": This is the main jupyter notebook to run
- "dqn_agent": Definition of our deep Q-Learning agent
- "dqn_model": Definition of our deep Q-Learning model
    
