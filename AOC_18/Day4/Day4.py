import datetime


class Action:
    def __init__(self, action_string):
        temp = action_string.split(']')
        time = temp[0].split(' ')
        date = time[0].split('-')
        time = time[1].split(':')
        self.date = datetime.datetime(int(date[0][1:]), int(date[1]), int(date[2]), int(time[0]), int(time[1]))
        if temp[1][1] == 'G':
            self.action = int(temp[1].split(' ')[2][1:])
        elif temp[1][1] == 'f':
            self.action = -1
        else:
            self.action = -2


actions = []
guard_data = {}
for line in open('input').readlines():
    action = Action(line)
    if action.action >= 0 and action.action not in guard_data.keys():
        guard_data[action.action] = [0]*60
    actions.append(action)


curr_guard = -1
asleep = False
minute = 0
for action in sorted(actions, key=lambda x: x.date):
    if asleep:
        for i in range(minute, action.date.minute):
            guard_data[curr_guard][i] += 1
    if action.action == -2:
        asleep = False
    elif action.action == -1:
        asleep = True
    else:
        curr_guard = action.action
    minute = action.date.minute

curr_guard = max(guard_data, key=lambda x: sum(guard_data[x]))
print("Part 1:", guard_data[curr_guard].index(max(guard_data[curr_guard])) * curr_guard)

curr_guard = max(guard_data, key=lambda x: max(guard_data[x]))
print("Part 2:", guard_data[curr_guard].index(max(guard_data[curr_guard]))*curr_guard)
