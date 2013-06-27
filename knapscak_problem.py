#!/usr/bin/env python
# encoding: utf-8
from backpack import BackPack

class KnapsackProblem():
    def __init__(self, items, backpack ):
        self.items = items
        self.backpack = backpack

    def insert_items_in_backpack_biggest_reason(self):
        while True:
            try:
                average_item_cost, weight, cost = max(
                                                        (cost/float(weight),weight, cost)
                                                        for weight, cost in self.items
                                                        if not((weight, cost)) in self.backpack.items
                                                        if ((weight + self.backpack.get_total_weight()) <= self.backpack.capacity)
                                                        )
                self.backpack.insert_item((weight, cost))
            except ValueError:
                break
    
    def insert_items_in_backpack_lowest_weight(self):
        while True:
            try:
                weight, cost = min(
                                    (weight, cost)
                                    for weight, cost in self.items
                                    if not((weight, cost)) in self.backpack.items
                                    if ((weight + self.backpack.get_total_weight()) <= self.backpack.capacity)
                                    )
                self.backpack.insert_item((weight, cost))
            except ValueError:
                break
    
    def insert_items_in_backpack_biggest_cost(self):
        while True:
            try:
                cost, weight = max(
                                    (cost, weight)
                                    for weight, cost in self.items
                                    if not((weight, cost)) in self.backpack.items
                                    if ((weight + self.backpack.get_total_weight()) <= self.backpack.capacity)
                                    )
                self.backpack.insert_item((weight, cost))
            except ValueError:
                break

if __name__ == '__main__':
    items = [
            (10,20),
            (5,10),
            (3,7),
            (8,13),
            (4,10)
            ]

    print "#### Biggest Reason ####"
    backpack = BackPack(12)
    p_backpack = KnapsackProblem(items, backpack)
    p_backpack.insert_items_in_backpack_biggest_reason()
    print "Items in backpack : %s" %p_backpack.backpack.items
    print "Total Cost : %s" %p_backpack.backpack.get_total_cost()

    print "\n"
    
    print "#### Lowest Weight ####"
    backpack = BackPack(12)
    p_backpack = KnapsackProblem(items, backpack)
    p_backpack.insert_items_in_backpack_lowest_weight()
    print "Items in backpack : %s" %p_backpack.backpack.items
    print "Total Cost : %s" %p_backpack.backpack.get_total_cost()
    
    print "\n"
    
    print "#### Biggest Cost ####"
    backpack = BackPack(12)
    p_backpack = KnapsackProblem(items, backpack)
    p_backpack.insert_items_in_backpack_biggest_cost()
    print "Items in backpack : %s" %p_backpack.backpack.items
    print "Total Cost : %s" %p_backpack.backpack.get_total_cost()

