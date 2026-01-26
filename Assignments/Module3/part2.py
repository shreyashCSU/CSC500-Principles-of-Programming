# Many people keep time using a 24-hour clock (11 is 11am and 23 is 11pm, 0 is midnight). 
# If it is currently 13 and you set your alarm to go off in 50 hours, it will be 15 (3pm). 
# Write a Python program to solve the general version of the above problem. Ask the user 
# for the time now (in hours) and then ask for the number of hours to wait for the alarm. 
# Your program should output what the time will be on a 24-hour clock when the alarm goes off.


current_time = int(input("Enter current time in hours (0-23): "))
# Hours to wait before arriving
wait_time = int(input("Enter wait time in hours: "))

# Wrap around the 24-hour clock using modulo to keep the hour in 0-23
arrival_time = (current_time + wait_time) % 24

# Convert to 12-hour format with an A.M./P.M. label
if arrival_time < 12:
    print("The arrival time is:", 12 if arrival_time == 0 else arrival_time, "A.M.")
else:
    arrival_time -= 12
    print("The arrival time is:", 12 if arrival_time == 0 else arrival_time, "P.M.")
