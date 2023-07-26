import numpy as np         
import random              
import time                
from collections import deque   

class Quadcopter:
    """Class representing a quadcopter with attributes and methods to generate and follow targets."""

    def __init__(self):
        """
        Initializes the Quadcopter with basic parameters and sets up recent locations deque.
        """
        self.altitude = 0
        self.distance = 0
        self.pitch = 0
        self.roll = 0
        self.yaw = 0
        self.cam_x = 0
        self.cam_y = 0
        self.prev_target_x = None  # Keeps track of previous target x position
        self.prev_target_y = None  # Keeps track of previous target y position
        # Queue to store recent locations, initialized to hold a maximum of 10 elements
        self.recent_locations = deque(maxlen=10)
        # L1 = front left motor, R1 = front right motor
        # L2 = back left motor, R2 = back right motor
        self.L1 = 0
        self.R1 = 0
        self.L2 = 0
        self.R2 = 0

    def generate_target(self):
        """
        Generates a target in a 5x5 grid. If a previous target exists, the new target will be in one of the
        neighbouring positions, otherwise it's randomly placed within the grid.
        """
        self.target = np.zeros((5, 5))  # Initialize target grid to zeros

        # If there's no previous target, generate a random target
        if self.prev_target_x is None or self.prev_target_y is None:
            x = random.randint(0, 4)
            y = random.randint(0, 4)
        else:  # If there's a previous target, the new target is in one of the neighboring locations
            possible_directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, 1), (1, -1), (-1, -1)]
            dx, dy = random.choice(possible_directions)
            x = max(0, min(self.prev_target_x + dx, 4))
            y = max(0, min(self.prev_target_y + dy, 4))

        self.target[y, x] = 1  # Set the target location in the grid to 1
        self.prev_target_x, self.prev_target_y = x, y  # Remember this target for next time

        # Add the current target location to the deque
        self.recent_locations.append((y, x))

    def find_target_location(self):
        """
        Finds the location of the target in the grid and returns its coordinates.
        If no target is found, returns None.
        """
        indices = np.argwhere(self.target == 1)  # Get the indices of the target in the grid
        if len(indices) > 0:
            x, y = indices[0]
            return x, y
        else:
            return None

    def follow(self):
        """
        Generates a target, displays it, waits for a second, then attempts to find and display the target location.
        """
        self.generate_target()
        print(self.target)
        location = self.find_target_location()
        if location:  # If a target location is found, display it
            print("Found target at:", location)
        else:
            print("No target found.")  # If no target is found, display a message

    def get_recent_locations(self):
        """
        Returns the recent locations of the targets as a list.
        """
        return list(self.recent_locations)

    def simulate(self):
      """
      Simulates the motors of the quadcopter. The motors are not connected to any actual
      logic in this current implementation.
      """

      current_target = self.find_target_location()

      if current_target != (2, 2):
          # Calculate pitch difference
          
              pitch_diff = current_target[0] - 2
        
              #pitch_diff = 2 - current_target[0]
          
          # Calculate roll difference
          
              roll_diff = current_target[1] - 2
         
              #roll_diff = 2 - current_target[1]
      else:
          return f"Pitch: {0}, Roll: {0}"
          
      return f"Pitch: {pitch_diff}, Roll: {roll_diff}"      
          

# Create an instance of the Quadcopter class
quadcopter = Quadcopter()

# Continuously follow and display targets
for _ in range(25):
    quadcopter.follow()
    recent_locations = quadcopter.get_recent_locations()
    print("Recent locations:", recent_locations)
    simulation = quadcopter.simulate()
    print(simulation)
    print("\n")
