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

DIRS = [(1, 0), (0, 1), (-1, 0), (0, -1)]
DIRS_WITH_CORNERS = [(1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)]
CORNERS = [(1, 1), (-1, -1), (-1, 1), (1, -1)]


def get_input(year, day):
    if year == 0 and day == 0:
        print("SET YEAR AND DAY VALUES!")
        exit(1)
    try:
        return open("input").read()
    except FileNotFoundError:
        target_url = 'https://www.adventofcode.com/' + str(year) + '/day/' + str(day) + '/input'
        session_key = open("../../MiscFiles/session-key").read().strip()
        response = requests.get(target_url, cookies={'session':session_key}).text.rstrip()
        if response.startswith("Please don't repeatedly"):
            return ''
        open("input", "w").write(response)
        return response


def get_grid(inp):
    grid = dict()
    inp = inp.split('\n')
    for r, row in enumerate(inp):
        for c, cell in enumerate(row):
            grid[r, c] = cell
    nr = len(inp)
    nc = len(inp[0])
    return grid, nr, nc