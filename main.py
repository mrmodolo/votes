#!/usr/bin/env python
# -*- coding: utf-8 -*-

from operator import itemgetter


states_dict = [
    {'name': 'Maine', 'votes': 5, 'days': 1},
    {'name': 'Nevada', 'votes': 6, 'days': 1},
    {'name': 'Minnesota', 'votes': 10, 'days': 2},
    {'name': 'New Hampshire', 'votes': 4, 'days': 1},
    {'name': 'Michigan', 'votes': 16, 'days': 3},
    {'name': 'Pennsylvania', 'votes': 20, 'days': 4},
    {'name': 'Wisconsin', 'votes': 10, 'days': 2},
    {'name': 'Florida', 'votes': 29, 'days': 5},
    {'name': 'Arizona', 'votes': 11, 'days': 2},
    {'name': 'North Carolina', 'votes': 15, 'days': 3},
    {'name': 'Georgia', 'votes': 16, 'days': 3},
]


def calculate_score(state):
    state['score'] = state['votes']/state['days']
    return state


def calculate_states_scores(states):
    states_scores = [calculate_score(state) for state in states]
    return states_scores


def max_votes(states):
    days = 10
    votes = 0
    while days > 0:
        for state in states:
            maybe_days = days - state['days']
            if maybe_days >= 0:
                days = maybe_days
                votes = votes + state['votes']
    return (days, votes)


def main():
    states_scores = calculate_states_scores(states_dict)
    states_sorted_by_score_votes = sorted(states_scores,
                                          key=itemgetter('score','votes'), reverse=True)
    for state in states_sorted_by_score_votes:
        print(state)
    days, votes = max_votes(states_sorted_by_score_votes)
    print(f'\ndays left: {days}, votes: {votes}')            

if __name__ in '__main__':
    main()
