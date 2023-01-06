#!/usr/bin/python3
'''lockboxes'''


def canUnlockAll(boxes):
    unlocked_boxes = [0]
    for box_id, box in enumerate(boxes):
        if not box:
            continue
        for key in box:
            if key < len(boxes) and key not in unlocked_boxes and key != box_id:
                unlocked_boxes.append(key)
    return len(unlocked_boxes) == len(boxes)
