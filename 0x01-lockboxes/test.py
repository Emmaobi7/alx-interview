#!/usr/bin/python3
"""
Solving the Python lockboxes challenge
"""

def canUnlockAll(boxes):
    """
    canUnlockAll: check if box can be unlocked
    return: True/False
    """
    unlocked = {0}  # Start with the first box unlocked

    for box_index, box in enumerate(boxes):
        if box_index in unlocked:
            unlocked.update(box)

    return len(unlocked) == len(boxes)

