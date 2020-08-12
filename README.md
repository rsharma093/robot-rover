# Robot rover / turtle problem

## Description

Create a command line that prompts for commands and moves a rover around a 2D plane.

The robot should point in a direction, turn to face different directions, and take a step in the direcion it is facing.


## Commands

**Run Test Cases:**
```
python -m unittest robot_rover.py
```
**Run Programe:**
```
python robot_rover.py
```

## Demo

```
Hello! Robot coming online.
Command the robot with:
  L - turn left
  R - turn right
  S - step forward
  ? - this message
  Q - quit
> S
Robot at (1, 0) facing North
> L
Robot at (1, 0) facing West
> S
Robot at (1, -1) facing West
> S
Robot at (1, -2) facing West
> R
Robot at (1, -2) facing North
> R
Robot at (1, -2) facing East
> S
Robot at (1, -1) facing East
> ?
Command the robot with:
  L - turn left
  R - turn right
  S - step forward
  ? - this message
  Q - quit
> Q
Robot shutting down.
