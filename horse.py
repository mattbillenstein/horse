#!/usr/bin/env pypy3

import json
import glob
import sys

class Puzzle:
    def __init__(self, puzzle):
        if isinstance(puzzle, str):
            with open(puzzle) as f:
                puzzle = json.load(f)

        self.puzzle = puzzle
        self.parse()

    def parse(self):
        self.board = {}
        self.horse = None
        self.portals = {}
        self.cherries = set()

        rows = self.puzzle['map'].replace('~', '#').split('\n')
        self.ys = ys = range(len(rows))
        self.xs = xs = range(len(rows[0]))
        for x in xs:
            for y in ys:
                pt = (x, y)
                self.board[pt] = c = rows[y][x]
                if c.isdigit():
                    if c not in self.portals:
                        self.portals[c] = []
                    self.portals[c].append(pt)
                elif c == 'C':
                    self.cherries.add(pt)
                elif c == 'H':
                    self.horse = pt

        # convert portals to bidirectional pointers pt1 -> pt2 and pt2 -> pt1
        for p in list(self.portals):
            pt1, pt2 = self.portals.pop(p)
            self.portals[pt1] = pt2
            self.portals[pt2] = pt1

    def print(self):
        print('Horse @ ', self.horse)
        print('Portals @ ', self.portals)
        print('Cherreis @ ', self.cherries)
        print()

        for y in self.ys:
            s = ''.join(self.board[(x, y)] for x in self.xs)
            print(s)

def main(files):
    if not files:
        files = glob.glob('puzzles/*.json')

    for fname in files:
        p = Puzzle(fname)
        p.print()
    
if __name__ == '__main__':
    main(sys.argv[1:])
