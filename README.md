# Strava Lite
### Strava is a popular exercise app which allows users to track workouts and incoporates social media features such as seeing friends' workouts. This final project is a basic version of Strava, with the ability to register, find, list users and see users you follow's workouts.

Link to repo: https://github.com/saracheak/strava-lite \
Author: Ravisara Cheakdkaipejchara\
Email: rcheakdk@stevens.edu

![Strava (LITE)](picture.png)

### Any bugs or issues you faced while working on this project and how you overcame the issues
#### The main challenge was due to the fact that within our "database" there were many nested dictionaries, lists, and sets. This made it more difficult to know which level you were in. I overcame this by adding print statements as I went along to understand which level I was keying into. Also I found out that although .get() and ["key"] could both return the same thing if done correctly, they behave differently when the key is not found, and this caused some confusion I learnt that .get() returns None, but ["key"] raises a KeyError if it is not found
