# input_processing.py
# Jacqui Moreland, ENSF 692 P24
# A terminal-based program for processing computer vision changes detected by a car.

class Sensor:

    # Initialize default values for attributes 'traffic_light', 'pedestrian', and 'vehicle_status'
    def __init__(self):
        self.traffic_light = "green"
        self.pedestrian = "no"
        self.vehicle_status = "no"

    # Assign passed values (designated by user input) to their corresponding attributes, then call the print_message method
    def update_status(self, light_colour, ped, vehicle):
        self.traffic_light = light_colour
        self.pedestrian = ped
        self.vehicle_status = vehicle
        print_message(self)

# Print out the value of all three attributes as well as the appropriate action message
def print_message(sensor):
    # If there is a vehicle or pedestrian detected, or the light is red, print a "STOP" message 
    if sensor.traffic_light == "red" or sensor.pedestrian == "yes" or sensor.vehicle_status == "yes":
        response = "STOP"
    # If the traffic light is yellow, print a "Caution" message
    elif sensor.traffic_light == "yellow":
        response = "Caution"
    # If the traffic light is yellow, print a "Proceed" message
    elif sensor.traffic_light == "green":
        response = "Proceed"
    print(f"\n{response}\n\nLight = {sensor.traffic_light}, Pedestrian = {sensor.pedestrian}, Vehicle = {sensor.vehicle_status}\n")


def main():
    print("\n***ENSF 692 Car Vision Detector Processing Program***\n")
    # Create new object of the Sensor class
    car_sensor = Sensor()

    while True:
        try:
            # Prompt user for input regarding changes to sensor detection
            user_input = input("Are there any changes detected in the vision input?\n" + 
                            "Select 1 for light, 2 for pedestrian, 3 for vehicle, or 0 to end the program: ")
            # Stop the loop if the user enters 0
            if user_input == '0':
                break
            # User indicated change to traffic light
            elif user_input == '1':
                # Prompt user to specify the identified change
                detected_change = input("What change has been identified?: ")
                # Send specific color change to the update_status method, or print out the status of all attributes if the input is invalid
                if detected_change == 'green' or detected_change == 'yellow' or detected_change == 'red':
                    car_sensor.update_status(light_colour=detected_change, ped=car_sensor.pedestrian, vehicle=car_sensor.vehicle_status)
                else:
                    print("Invalid vision change.")
                    print_message(car_sensor)
            # User indicated change to pedestrian detection
            elif user_input == '2':
                # Prompt user to specify the identified change
                detected_change = input("What change has been identified?: ")
                # Send yes or no pedestrian detected to the update_status method, or print out the status of all attributes if the input is invalid
                if detected_change == 'yes' or detected_change == 'no':
                    car_sensor.update_status(light_colour=car_sensor.traffic_light, ped=detected_change, vehicle=car_sensor.vehicle_status)
                else:
                    print("Invalid vision change.")
                    print_message(car_sensor)
            # User indicated change to vehicle detection
            elif user_input == '3':
                # Prompt user to specify the identified change
                detected_change = input("What change has been identified?: ")
                # Send yes or no vehicle detected to the update_status method, or print out the status of all attributes if the input is invalid
                if detected_change == 'yes' or detected_change == 'no':
                    car_sensor.update_status(light_colour=car_sensor.traffic_light, ped=car_sensor.pedestrian, vehicle=detected_change)
                else:
                    print("Invalid vision change.")
                    print_message(car_sensor)
            # Raise ValueError if the initial input is not accepted
            else:
                raise ValueError("You must select either 1, 2, 3, or 0.")
        
        except ValueError as err:
            print(err, end="\n\n")


# Conventional Python code for running main within a larger program
if __name__ == '__main__':
    main()

