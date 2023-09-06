# Snake Reinforcement Learning 

This project contains two agent programs which are trained to play their respective games using the pytorch framework. The agent uses Q-Learning to create a neural network model.

The effectiveness of the neural network model is visualized on a graph using matplotlib which gives a nice illustration of how the agent learns over time.

While the agent was effective at learning to play both games, it did seem to hit a plateau. For the snake game it plateaued a score of around 30. The pixel drop agent was less effective in learning to play the game. It seemed to have some very high score and very low scores. I may play around with the number of inputs for the input layer of the model and rewards in the future to see if it enhances the model.

# Dependencies
  pytorch
  numpy
  matplotlib

# How to Run
python3 pixel_agent.py
or
python3 snake_agent.py

# Credit
snake: https://www.youtube.com/watch?v=L8ypSXwyBds&t=738s
