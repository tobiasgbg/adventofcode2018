import os
import sys
import re
 
def main():
    cwd = os.getcwd()
 
    with open (cwd + "/day4input.txt", "r") as myfile:
        file_list=myfile.readlines()

    file_list_sorted = sorted(file_list)

    #print(file_list_sorted)

    #record = (date, id, observation)

    current_guard = None
    current_date = ''
    action_list = [0] * 60
    last_time = 0
    is_awake = True
    guard_list = []
 
    for line in file_list_sorted:
        regexp = re.search('-(\d{2}-\d{2})\s(\d{2}):(\d{2})]\s(Guard\s(#\d+)|falls asleep|wakes up)', line)
        date = regexp.group(1)
        time_hour = regexp.group(2)
        time_minute = regexp.group(3)
        action = regexp.group(4)
        guard_id = regexp.group(5)

        if action == "falls asleep" or action == "wakes up":
            is_awake = action != "falls asleep"
            for i in range(0 if last_time == 0 else last_time - 1, int(time_minute) - 1):
                action_list[i] = '#' if is_awake else '.'
            last_time = int(time_minute)
        elif guard_id != '':
            if (current_guard != None):
                for i in range(0 if last_time == 0 else last_time - 1, 59):
                    action_list[i] = '.' if is_awake else '#'
                guard_list.append((current_date, current_guard, list(action_list)))
            is_awake = True
            last_time = 0
            current_guard = guard_id
            current_date = date

    for i in range(0 if last_time == 0 else last_time - 1, 59):
        action_list[i] = '.' if is_awake else '#'
    guard_list.append((current_date, current_guard, list(action_list)))

    #print(guard_list)

    guard_dict = {}

    for guard in guard_list:
        minutes_asleep = guard_dict.get(guard[1])
        if minutes_asleep == None:
            minutes_asleep = 0

        for minute in guard[2]:
            if minute == '#':
                minutes_asleep += 1

        guard_dict[guard[1]] = minutes_asleep

    #print(guard_dict)

    sleepiest_guard = ''
    most_minutes_slept = 0

    for guard in guard_dict:
        if int(guard_dict[guard]) > most_minutes_slept:
            sleepiest_guard = guard
            most_minutes_slept = int(guard_dict[guard])

    print("Most minutes slept: " + str(most_minutes_slept))
    print("Sleepiest guard: " + str(sleepiest_guard))
    guard_minute_dict = {}

    for guard in guard_list:
        if guard[1] == sleepiest_guard:
            i = 0
            for minute in guard[2]:
                if minute == '#':
                    if guard_minute_dict.get(i) == None:
                        guard_minute_dict[i] = 1
                    else:
                        guard_minute_dict[i] = guard_minute_dict.get(i) + 1 
                i += 1
    
    sleepiest_minute = ''
    days_most_slept = 0

    print(guard_minute_dict)

    for guard_minute in guard_minute_dict:
        if int(guard_minute_dict[guard_minute]) > days_most_slept:
            sleepiest_minute = guard_minute
            days_most_slept = int(guard_minute_dict[guard_minute])

    print("Sleepiest guard: " + str(sleepiest_guard) + " minute most slept: " + str(sleepiest_minute))

if __name__ == "__main__":
	main()