# SOURCE: Leetcode
# https://leetcode.com/problems/car-fleet/
# Solution: https://neetcode.io/solutions/car-fleet


# Time Complexity (TC): O(nlogn): Because we are using a nested loop
# Space Complexity (SC): O(n): additional memory for stack and cars

# Approach: Sort the cars by their positions in descending order so that we process the
# car closest to the target first. For each car, compute the time it would take to reach the target.
# The first car always forms a fleet. As we process the remaining cars, compare each car’s arrival time
# with the arrival time of the fleet immediately ahead. If the current car reaches the target
# in less than or equal time, it must catch up to that fleet before (or exactly at) the target,
# so it becomes part of the same fleet. Otherwise, it cannot catch up and forms a new fleet.
def car_fleet_1(target, position, speed):
    cars = sorted(zip(position, speed), reverse=True)

    stack = []

    for pos, speed in cars:
        time = (target - pos) / speed

        if not stack or time > stack[-1]:
            stack.append(time)

    return len(stack)



# Much better because of smaller constant factor
# Time Complexity (TC): O(nlogn): Because we are using a nested loop
# Space Complexity (SC): O(n): additional memory for cars list

# Approach: Sort the cars by their positions in descending order so that we process the
# car closest to the target first. For each car, compute the time it would take to reach the target.
# The first car always forms a fleet. As we process the remaining cars, compare each car’s arrival time
# with the arrival time of the fleet immediately ahead. If the current car reaches the target
# in less than or equal time, it must catch up to that fleet before (or exactly at) the target,
# so it becomes part of the same fleet. Otherwise, it cannot catch up and forms a new fleet.
def car_fleet_2(target, position, speed):
    cars = sorted(zip(position, speed), reverse=True)

    fleets = 0
    last_fleet_time = 0

    for pos, speed in cars:
        time = (target - pos) / speed

        if time > last_fleet_time:
            last_fleet_time = time
            fleets += 1

    return fleets