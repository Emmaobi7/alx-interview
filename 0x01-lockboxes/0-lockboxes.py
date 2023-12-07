#!/usr/bin/python3
"""
solving the the python lockboxes
chalenge
"""


def canUnlockAll(boxes):
    """
    canUnlockAll: check if box
        can be unlocked
    return: true/false
    """
    unlocked = {}
    for box_index, box in enumerate(boxes):
        if len(box) == 0 or box_index == 0:
            unlocked[box_index] = box_index
        for key in box:
            if key < len(boxes) and key != box_index:
                unlocked[key] = key
    return len(unlocked) == len(boxes)
