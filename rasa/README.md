# Description

## About this bot

This is funny bot, that can send you pictures about cats, dogs, foxes. Can tell you facts about cats and dogs. Also it can find some football matchs and check country of the city.

## Run the Bot

Make sure you have installed all of the requirements from the `requirements.txt` file:

```bash
pip3 install -r requirements.txt
```

To run the bot locally you must first train the bot by opening a terminal window in the rasa directory.

```bash
rasa train
```

Thirst of all run Action server. Starting the action server requires opening a new terminal window in rasa directory.

```bash
rasa run actions
```

Open a new terminal in the same directory as the previous terminal. Run the following command to start the server

```bash
rasa run --enable-api --cors "*"

```

Open one more terminal, go to the root directory and install all packagas

```bash
npm install  or yarn install
```

run web application

```bash
yarn start Or npm start
```

## What the Bot Does

The bot can does those functions:

1. Can make you smile
2. Find information about football
3. Find pictures with fox, dog or cat
4. Find facts about dog or cat
5. Check country by city
