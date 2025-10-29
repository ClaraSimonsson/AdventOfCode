from collections import defaultdict
import math
import os


def handle_input(f):
    ls = f.read().split("\n\n")
    rules = createRuleDict(ls[0])
    page_nmbrs = [update.split(",") for update in ls[1].splitlines()]
    return [rules, page_nmbrs]


def createRuleDict(rules_list):
    rules = {}
    for rule in rules_list.splitlines():
        first, second = rule.split("|")
        if first not in rules.keys():
            rules[first] = set()
            rules[first].add(second)
        else:
            rules[first].add(second)
    return rules


def solve_input(input):
    rules = input[0]
    page_nmbrs = input[1]
    valid_updates = 0
    invalid_updates = 0
    for nmbr in page_nmbrs:
        valid = True
        index = math.floor(len(nmbr) / 2)
        for i in range(len(nmbr)):
            curr_page = nmbr[i]
            if curr_page in rules.keys() and rules.get(curr_page).intersection(nmbr[:i]):
                valid = False
                break
        if valid:
            valid_updates += int(nmbr[index])
        else:
            updated_order = nmbr.copy()
            correct_order = False
            p1, p2 = 0, 1
            while correct_order != True:
                curr_item = updated_order[p1]
                next_item = updated_order[p2]
                if next_item in rules.keys() and (curr_item in rules.get(next_item)):
                    updated_order[p1] = next_item
                    updated_order[p2] = curr_item
                p2 += 1
                if p2 == len(updated_order):
                    p1 += 1
                    p2 = p1 + 1
                if p1 == len(updated_order) - 1:
                    correct_order = True
            invalid_updates += int(updated_order[index])
    return [valid_updates, invalid_updates]

