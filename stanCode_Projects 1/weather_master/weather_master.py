"""
File: weather_master.py
Name: Frank Chiang
-----------------------
This program should implement a console program
that asks weather data from user to compute the
average, highest, lowest, cold days among the inputs.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""
EXIT = -1


def main():
    """
    This program will help us to find the highest, the lowest, average temperature within recorded data, also calculate
    how many cold days that under 16 degrees.
    """
    greeting()
    type_the_data()


def greeting():
    """
    This function is for greeting!"
    """
    print("stanCode \"Weather Master 4.0!\"")


def type_the_data():
    """
    This function is used to input our data.
    """
    # The first data to be put
    data = float(input('Next temperature: (or -1 to quit)? '))
    if data == EXIT:
        print('No temperatures were entered.')
        # Start over again
        return main()
    else:
        maximum = data
        minimum = data
        first_cold_day = 0
        # We need to determine whether first day was a cold day.
        if data < 16:
            first_cold_day = 1
        # To determine whether the following input data were cold days or not.
        cold_day = 0
        # The sum of the data.
        total = 0
        # For counting how many data be input.
        number_of_data = 0
        while True:
            total = total + data
            number_of_data += 1
            data = float(input('Next temperature: (or -1 to quit)? '))
            if data == EXIT:
                break
            # To determine the cold days (suggested by teacher assistant James Shih)
            if data < 16:
                cold_day += 1
            # To find the maximum
            if data > maximum:
                maximum = data
            # To find the minimum
            if data < minimum:
                minimum = data
        # To calculate the needed data.
        show_the_results(maximum, minimum, total, number_of_data, first_cold_day, cold_day)


def show_the_results(maximum, minimum, total, number_of_data, first_cold_day, cold_day):
    """
    This function will calculate the data we input, and tell us the highest, lowest, average temperature, also show
    how many cold days (temperature that under 16 degrees).
    """
    # Calculate the average temperature.
    average_of_data = total / number_of_data
    # Calculate the total cold days
    total_cold_day = first_cold_day + cold_day
    # Print out the results.
    print('Highest temperature: ' + str(maximum))
    print('Lowest temperature: ' + str(minimum))
    print('Average temperature: ' + str(average_of_data))
    print(str(int(total_cold_day)) + ' cold day(s)')
    # Start a new round.
    return main()


###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
    main()

