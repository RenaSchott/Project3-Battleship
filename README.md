# Battleship

Being interested in different games, this Python challenge was an interesting experience. The game should be fun for all user liking those kind of games.

View the live project here: <https://project3-battleship-2a9ceefa4769.herokuapp.com/>

## Table of content

- [Battleship](#battleship)
  - [Table of content](#table-of-content)
  - [UX](#ux)
    - [Site goals](#site-goals)
    - [User stories](#user-stories)
      - [As a visitor](#as-a-visitor)
      - [As the administrator](#as-the-administrator)
    - [Wireframes](#wireframes)
    - [Flow Chart](#flow-chart)
  - [Method](#method)
    - [POC (prove of concept)](#poc-(prove-of-concept))
    - [MVP (minimum viable product)](#mvp-(minimum-viable-product))
  - [Features](#features)
    - [Index page](#index-page)
    - [Game page](#game-page)
    - [Features left to implement](#features-left-to-implement)
  - [Used Technologies](#used-technologies)
    - [Languages Used](#languages-used)
    - [Framework, Libraries and Programs](#framework-libraries-and-programs)
  - [Testing](#testing)
    - [Manual testing](#manual-testing)
    - [Testing user stories](#testing-user-stories)
    - [Validator testing](#validator-testing)
    - [Unfixed bugs](#unfixed-bugs)
  - [Deployment](#deployment)
  - [Credits](#credits)
    - [Content](#content)
    - [Media](#media)
  - [Acknowledgements](#acknowledgements)

## UX

### Site goals

The site wants to challenge the user to a fun battleship game.

### User stories

#### As a visitor

- I want to play a game of battleship
- I want to have fun
- I want to be entertained
- I want to be able to have a good overview

#### As the administrator

- I want to be able to adjust the game if needed
- I want to be able to expand the game
- I want to be able to easily add new option to the game
- I want to be able to easily add new features to the existing game

### Wireframes

Here are the drawings of the wireframes:

![Drawing of welcome page](assets/readmeimages/wireframe1.png)
![Drawing of exemplary game set up](assets/readmeimages/wireframe2.png)


### Flow Chart

Here is the previously outlined flow chart which contains parts of the actual project and of version 2:

![Drawn flow chart of the project](assets/readmeimages/flow-chart.png)

### Method

#### POC (prove of concept)

- User input → start game
- Display boards
- User guess input
- Evaluation → showing result
- Move repetition

#### MVP (minimum viable product)

- Welcome screen
- Want to play message and link to rules
- Random placement of battleships
- End of game conditions
- End screen -> announcing winner

## Features

### 

### Welcome screen

- The welcome screen is the first thing the user sees from the battleship app. Here the large letters "Welcome to Battleship!" can be seen as well as the question "Do you want to start the game (y/n)?. The (y/n) indicates the possible input. By typing in y the user can progress with the game. While n  will stop the game from running. If the user gives any other input the user will be asked again to answer the question correct. The y and n answer will be autocommented.

![Screen shot of the welcome screen of the project](assets/readmeimages/welcome-screen.png)

### Username

- Next the game asks the user for a name. There the user can type whatever the user wants as long as something can be seen. An empty space will not be accepted and the game has to be restarted if this was a mistake.

![Screen shot of the question for the username](assets/readmeimages/name.png)

### Game rules

- Since this is a short version of the battleship game the user can read the game rules if wanted. Here only n or y are accepted. Otherwise the user will be asked again. The y and n answer will be autocommented.

![Screen shot of the question for the game rules](assets/readmeimages/rules.png)

### Game board

- With the username above the game board it will be personalized. On the game board the user can see the numbers 1-6 for columns and a-f for rows.

![Screen shot of the personalized game board](assets/readmeimages/board.png)

### User moves

- To make a guess where a battleship could be the user has to make a valid guess for row and column. Invalid input will be stated and the question will be asked again. The move is evaluated and the program will tell the user whether it was a hit, a miss or whether the user already asked the question previously. A hit and a miss will be marked on the board with * and O and the remaining move will be stated. As long as there are still remaining moves and battleships the user will be asked again for their guess. If the moves count reaches zero the game is lost. If the user hits all battleships before that the user will win the game. Both events will be commented.

![Screen shot of examplary move](assets/readmeimages/moves.png)

### Features left to implement

There is the possibility to integrate

- **V2 (version 2)**
  - Styling (colorama?)
  - Board size options
  - Placing Battleships
  - Number and ship sizes
  - Opponent turn
    - Random opponent guess
  - Evaluation → showing result
  - Display board with battleships



## Used Technologies

### Languages Used

- Python

### Framework, Libraries and Programs

- Frameworks 
    -
- Libraries 
    -
- Moduls
    - Random
    - Pyfiglet
- Programs
    - Balsamiq
        - was used to create the wireframes
    - Lucidchart
        - was used to create the flow chart
    - GitHub
        - was used to store the project site
    - Gitpod
        - was used to write the code and commit it to GitHub
    - Heroku 
        - was used to deploy the project 


- Am I responsive
  - was used to check the responsiveness of the website
- DevTools
  - were used to inspect the code during the development process and to check the accessibility
    - Languagetool
        - was used to check the spelling and grammar in the README file.
  
## Testing

### Manual testing

| **Feature** | **Expect** | **Action** | **Result** |
|---------------------|--------------------|--------------------------|------------------------------|


### Testing user stories

| **Expectation - User** | **Result**|
|--------------|------------|


**As the administrator**

| **Expectation - Administrator** | **Result**|
|--------------|------------|


### Validator testing

- **Python**


### Unfixed bugs

- 

## Deployment

The deployment was done using <https://www.heroku.com/>

- 
The link to the live page can be found here: [Battleship] (<https://project3-battleship-2a9ceefa4769.herokuapp.com/>)

## Credits

### Content

The content of this project was inspired by the Love Sandwiches project and the content of the course. In general, the following websites were used for inspiration:
  - <https://www.w3schools.com/>
  - <https://www.youtube.com/watch?v=RqCZBbfd9Fw>
  - <https://www.youtube.com/watch?v=tF1WRCrd_HQ>

Inspirations for specific problems were taken from the following websites:
  - <https://www.geeksforgeeks.org/python-ascii-art-using-pyfiglet-module/>
  - <https://www.freecodecamp.org/news/python-exit-how-to-use-an-exit-function-in-python-to-stop-a-program/>
  - <https://www.geeksforgeeks.org/python-docstrings/>
  - <https://www.freecodecamp.org/news/print-newline-in-python/>

### Media

- no media was used

## Acknowledgements

- I would love to thank the following persons:
  - My mentor for his support
  - The Code Institute tutor support for their fast answers
  - My facilitator for her support
  - The slack community for their fast answers and support