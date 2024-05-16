# input_processing.py
# Jacqui Moreland, ENSF 692 P24
# A terminal-based program for processing computer vision changes detected by a car.
# Detailed specifications are provided via the Assignment 2 README file.
# You must include the code provided below but you may delete the instructional comments.
# You may add your own additional classes, functions, variables, etc. as long as they do not contradict the requirements (i.e. no global variables, etc.). 
# You may import any modules from the standard Python library.
# Remember to include your name and comments.



# No global variables are permitted


# You do not need to provide additional commenting above this class, just the user-defined functions within the class
class Sensor:

    # Must include a constructor that uses default values
    # You do not need to provide commenting above the constructor
    def __init__(self):
        self.traffic_light = "green"
        self.pedestrian = "no"
        self.vehicle_status = "no"

    # Replace these comments with your function commenting
    def update_status(self, light_colour="green", ped="no", vehicle="no"): # You may decide how to implement the arguments for this function
        self.traffic_light = light_colour
        self.pedestrian = ped
        self.vehicle_status = vehicle

        if self.traffic_light == "red" or self.pedestrian == "yes" or self.vehicle_status == "yes":
            print_message(self, "STOP")
        elif self.traffic_light == "yellow":
            print_message(self, "Caution")
        elif self.traffic_light == "green":
            print_message(self, "Proceed")


# The sensor object should be passed to this function to print the action message and current status
# Replace these comments with your function commenting
def print_message(sensor, response):
    print(f"\n{response}\n\nLight = {sensor.traffic_light}, Pedestrian = {sensor.pedestrian}, Vehicle = {sensor.vehicle_status}\n")


# Complete the main function below
def main():
    print("\n***ENSF 692 Car Vision Detector Processing Program***\n")
    car_sensor = Sensor()

    while True:
        try:
            user_input = input("Are there any changes detected in the sensor?\n" + 
                            "Select 1 for light, 2 for pedestrian, 3 for vehicle, or 0 to end the program: ")
            if user_input == '0':
                break
            elif user_input == '1':
                detected_change = input("What change has been identified?: ")
                detected_change = detected_change.lower()
                if detected_change == 'green' or detected_change == 'yellow' or detected_change == 'red':
                    car_sensor.update_status(light_colour=detected_change)
                else:
                    raise ValueError("Please enter either 'green', 'yellow', or 'red'")
            elif user_input == '2':
                detected_change = input("What change has been identified?: ")
                detected_change = detected_change.lower()
                if detected_change == 'yes' or detected_change == 'no':
                    car_sensor.update_status(ped=detected_change)
                elif detected_change == 'no':
                    car_sensor.update_status()
                else:
                    raise ValueError("Please enter either 'yes' or 'no'")
            elif user_input == '3':
                detected_change = input("What change has been identified?: ")
                detected_change = detected_change.lower()
                if detected_change == 'yes':
                    car_sensor.update_status(vehicle=detected_change)
                elif detected_change == 'no':
                    car_sensor.update_status(vehicle=detected_change)
                else:
                    raise ValueError("Please enter either 'yes' or 'no'")
            else:
                raise ValueError("Your input must be either a 1, 2, 3, or 0")
        
        except ValueError as err:
            print(f"\nValueError:", err, end="\n\n")





# Conventional Python code for running main within a larger program
# No additional code should be included below this
if __name__ == '__main__':
    main()

