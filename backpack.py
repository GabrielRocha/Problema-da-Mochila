#!/usr/bin/env python
# encoding: utf-8

class BackPack():
    def __init__(self, capacity):
        self.capacity = capacity
        self.items = []

    def get_total_cost(self):
        return sum(cost for weight, cost in self.items)
    
    def get_total_weight(self):
        return sum(weight for weight, cost in self.items)
    
    def insert_item(self,item):
        self.items.append(item)

