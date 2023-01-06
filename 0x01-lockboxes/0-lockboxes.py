#!/usr/bin/python3
'''lockboxes'''


def canUnlockAll(boxes):
    '''determines if all boxes can be unlocked.'''
    visited = [False] * len(boxes)
    stack = [0]
    while stack:
        key = stack.pop()
        if not visited[key]:
            visited[key] = True
            stack.extend(boxes[key])
    return all(visited)
