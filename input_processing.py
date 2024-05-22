# input_processing.py
# Jacqui Moreland, ENSF 692 P24

# A terminal-based program for processing computer vision changes detected by a car.

class Sensor:

    def __init__(self):
        # Initialize default values for attributes 'traffic_light', 'pedestrian', and 'vehicle_status'
        self.traffic_light = "green"
        self.pedestrian = "no"
        self.vehicle_status = "no"

    def update_status(self, light_colour, ped, vehicle):
        """ Assign passed values to their corresponding Sensor attributes, then call the print_message function. """

        self.traffic_light = light_colour
        self.pedestrian = ped
        self.vehicle_status = vehicle
        # Call the print message function
        print_message(self)


def print_message(sensor):
    """
    Uses conditional logic to check the status of the traffic light, pedestrian, and vehicle and output an
    appropriate action message. 

    Args:
        sensor: Sensor object
    """

    # "STOP" condition
    if sensor.traffic_light == "red" or sensor.pedestrian == "yes" or sensor.vehicle_status == "yes":
        response = "STOP"
    # "Caution" condition
    elif sensor.traffic_light == "yellow":
        response = "Caution"
    # "Proceed" condition
    elif sensor.traffic_light == "green":
        response = "Proceed"
    
    # Print to the console the updated status and the action message
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
                if detected_change in ['green','yellow','red']:
                    car_sensor.update_status(light_colour=detected_change, ped=car_sensor.pedestrian, vehicle=car_sensor.vehicle_status)
                else:
                    print("Invalid vision change.")
                    print_message(car_sensor)
            # User indicated change to pedestrian detection
            elif user_input == '2':
                # Prompt user to specify the identified change
                detected_change = input("What change has been identified?: ")
                # Send yes or no pedestrian detected to the update_status method, or print out the status of all attributes if the input is invalid
                if detected_change in ['yes', 'no']:
                    car_sensor.update_status(light_colour=car_sensor.traffic_light, ped=detected_change, vehicle=car_sensor.vehicle_status)
                else:
                    print("Invalid vision change.")
                    print_message(car_sensor)
            # User indicated change to vehicle detection
            elif user_input == '3':
                # Prompt user to specify the identified change
                detected_change = input("What change has been identified?: ")
                # Send yes or no vehicle detected to the update_status method, or print out the status of all attributes if the input is invalid
                if detected_change in ['yes', 'no']:
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

