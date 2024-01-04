# Gravitational Slingshot Simulation

This is a simple gravity simulation that demonstrates the gravitational slingshot effect. A spaceship can be launched around a massive planet, gaining speed from the planet's gravitational pull.  

## Overview

This simulation is built with Python and Pygame. The main features include:

- Click and drag to set spaceship trajectory  
- Spaceship orbits planet and gets accelerated by gravitational slingshot
- Spaceship removed if goes off screen or crashes into planet 
- Visual effects like background, planet image, ship/planet rendering

## Usage  

To run the simulation:

```
python slingshot.py
```

Click and hold mouse to set start point, drag to set spaceship velocity direction. Release to launch spaceship. Multiple ships can be launched.  

## Physics  

The simulation applies Newtonian gravitational physics between the planet and spaceship. Acceleration is calculated from the gravitational force. Velocity is updated each frame based on acceleration.   

Some parameters can be tweaked at the top of the code:  

- \`PLANET_MASS\` - Mass of planet  
- \`SHIP_MASS\` - Mass of spaceship  
- \`G\` - Gravitational constant  
- \`VEL_SCALE\` - Controls speed of spaceships

## Demo
![](https://github.com/rohan300/slingshot-simulation/blob/main/assets/slingshot.gif)

## Future Improvements

Some ideas for extending the simulation:  

- Add UI for setting parameters   
- Visual effects for engine burn, explosions  
- Multiple planets   
- Save/load simulation states  
