# ShouldWeSurrender15

The goal of this project is to create a model to predict probability of winning in the game of League of legends given the state after 10 minutes. It was inspired by [OpenAi 5](https://openai.com/projects/five/) bots which calculate the probability of winning against the professional DoTa2 players during the match. 

## Overview 

The main feature is gradient boosting classifier implemented using **XGBoost** library and fitted to [League of Legends Diamond Ranked Games (10 min)](https://www.kaggle.com/bobbyscience/league-of-legends-diamond-ranked-games-10-min) dataset from Kaggle. It is wrapped in a simple web app written in **Django**. Application is basically a calculator which could be written without the use of django but one of the goals of this project was learning basic django project structure. 

## Usage


First user is provided forms to input data :

![userinput](https://github.com/lukasztroc/ShouldWeSurrender15/blob/master/user_input.png)


And then the probability is calculated based on the input and displayed as a gauge chart:

![chart](https://github.com/lukasztroc/ShouldWeSurrender15/blob/master/gauge.png)
