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
