steps = {chr(x): set() for x in range(65, 91)}
for line in open('input').readlines():
    line = line.split()
    steps[line[7]].add(line[1])

taken = set()
seconds = 1
steps_left = 26
workers = {x: ['-', 0] for x in range(5)}
workers[0] = ['L', ord('L')-4]
taken.add('L')
workers[1] = ['N', ord('N')-4]
taken.add('N')
workers[2] = ['R', ord('R')-4]
taken.add('R')
workers[3] = ['T', ord('T')-4]
taken.add('T')
while steps_left > 0:
    seconds += 1
    for worker in workers:
        if workers[worker][0] != '-':
            workers[worker][1] -= 1
            if workers[worker][1] == 0:
                steps_left -= 1
                for step_change in steps:
                    steps[step_change] -= {workers[worker][0]}
                workers[worker][0] = '-'
                for worker_change in workers:
                    if workers[worker_change][0] == '-':
                        for step in steps:
                            if not steps[step] and step not in taken:
                                taken.add(step)
                                workers[worker_change] = [step, ord(step)-4]
                                break
print(seconds)
