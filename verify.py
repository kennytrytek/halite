#!/usr/bin/env python

import copy
import os
import sys
import uuid
from multiprocessing import Pool
from subprocess import PIPE, Popen


seeds = ('2944993328', '2949872884', '3218539606', '3552599139', '3693640182', '1410710215')
map_sizes = tuple(str(x) for x in range(20, 55, 5))


def main(argv):
    print('HAL vs v{}'.format(argv[0]))
    with Pool(6) as p:
        for seed in seeds:
            print('Seed {}'.format(seed))
            cmds = []
            for size in map_sizes:
                cmds.append((
                    ['./halite',
                     '-s', seed,
                     '-d', '{} {}'.format(size, size),
                     'python HAL.py',
                     'python v{}.py'.format(argv[0])],
                    size))

            print('\n'.join([_ for _ in p.starmap(run_game, cmds)]))

    return 0


def run_game(cmd, size):
    p = Popen(cmd, stdout=PIPE, stderr=PIPE, cwd=os.curdir)
    stdout, stderr = p.communicate()
    if stderr:
        return stderr

    return parse_output(stdout, size)


def parse_output(output, map_size):
    if b'Player #1, HAL, came in rank #1' in output:
        return '{}x{}: \u2713'.format(map_size, map_size)
    elif b'Player #2, HAL, came in rank #1' in output:
        return '{}x{}: \u2718'.format(map_size, map_size)
    else:
        file_hex = uuid.uuid4().hex
        with open('{}.out'.format(file_hex), 'w') as f:
            f.write(str(output))

        'Invalid output. Written to {}.out'.format(file_hex)


if __name__ == '__main__':
    sys.exit(main(copy.deepcopy(sys.argv[1:])))
