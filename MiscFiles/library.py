import requests
from collections import deque, defaultdict, Counter
import itertools
import z3
import networkx as nx
import functools
import heapq
import math
import re
import numpy as np

DIRS = [(-1, 0), (0, 1), (1, 0), (0, -1)]
DIRS_WITH_CORNERS = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
CORNERS = [(-1, 1), (1, 1), (1, -1), (-1, -1)]
SESSION_KEY = open("../../MiscFiles/session-key").read().strip()

def get_input(year, day):
    if year == 0 and day == 0:
        print("SET YEAR AND DAY VALUES!")
        exit(1)
    try:
        return open("input").read()
    except FileNotFoundError:
        target_url = 'https://www.adventofcode.com/' + str(year) + '/day/' + str(day) + '/input'
        response = requests.get(target_url, cookies={'session':SESSION_KEY}).text.rstrip()
        if response.startswith("Please don't repeatedly"):
            return ''
        open("input", "w").write(response)
        return response


def submit_ans(year, day, part, ans):
    if year == 0 and day == 0:
        print("SET YEAR AND DAY VALUES!")
        return
    if part not in (1, 2):
        print("INVALID LEVEL VALUE!")
        return

    print("Answer Found:")
    print(ans)
    _ = input("Submit?")

    target_url = f'https://adventofcode.com/{year}/day/{day}/answer'
    data = {'level': str(part), 'answer': str(ans)}
    response = requests.post(target_url, data=data, cookies={'session':SESSION_KEY})

    response_text = re.search("<article><p>(.*)</p></article>", response.text, re.DOTALL).group(1)
    response_text = re.sub('([.!])( ){1,2}', '.\n', response_text)
    s = re.compile('<.*?>', re.DOTALL)
    response_text = re.sub(s, '', response_text)

    print(response_text)

def get_grid(inp):
    grid = dict()
    inp = inp.split('\n')
    for r, row in enumerate(inp):
        for c, cell in enumerate(row):
            grid[r, c] = cell
    nr = len(inp)
    nc = len(inp[0])
    return grid, nr, nc