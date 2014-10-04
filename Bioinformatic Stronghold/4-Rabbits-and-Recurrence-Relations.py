#!/usr/bin/env python

months = 5
litters = 3
total_pairs = 0

pairs = {'newborn':1, 'reproductive':0, 'incubating':0}

# We remove one month because the first month is manually added
for i in range(months-1):
    # Runs current reproductive cycle
    pairs['reproductive'] += pairs['newborn']
    mates_current_cycle = pairs['reproductive']
    pairs['newborn'] = pairs['incubating']
    pairs['incubating'] = mates_current_cycle*litters

print pairs['reproductive']+pairs['newborn']
