GRAVITY = 9.8 # Acceleration in m/s^2

class Quadcopter:
    def __init__(self, name, weight, propeller_area, max_battery_life=30):
        self.name = name
        self.max_battery_life = max_battery_life  # Maximum battery life in minutes
        self.battery_life = max_battery_life  # Current battery life in minutes
        self.pitch = 0  # Pitch angle in degrees
        self.roll = 0  # Roll angle in degrees
        self.yaw = 0  # Yaw angle in degrees
        self.thrust = 0 # Motor Speed
        self.weight = weight # Weight in kg's
        self.propeller_area = propeller_area # Area in m^2
        self.altitude = 0 # Altitude in meters
        

    def take_off(self, elevation, time):
        '''
        If gravity accelerates at 9.8m/s^2, then the quadcopter must
        accelerate more than that to reach an elevation where it can hover.
        To take off, we must assaign an elevation to hover and how long it
        will take to reach that destination. The elevation equation would
        be the product of time and rpms, so in order to get to our desired
        elevation we must solve for rpms. Of course we can't forget about 
        the surface area of the propellers.
        '''



    def land(self):


    def set_pitch(self, angle):
        self.pitch = angle
        print(f"{self.name}'s pitch angle is set to {self.pitch} degrees.")

    def set_roll(self, angle):
        self.roll = angle
        print(f"{self.name}'s roll angle is set to {self.roll} degrees.")

    def set_yaw(self, angle):
        self.yaw = angle
        print(f"{self.name}'s yaw angle is set to {self.yaw} degrees.")

    def get_battery_life(self):
        print(f"{self.name}'s battery life is at {self.battery_life} minutes.")

    def recharge_battery(self):
        self.battery_life = self.max_battery_life
        print(f"{self.name}'s battery is fully recharged.")
