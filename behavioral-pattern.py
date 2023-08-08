"""
Behavioral Pattern
- Strategy

https://www.youtube.com/watch?v=tAuRQs_d9F8
"""
from abc import ABC, abstractmethod


class FilterStrategy(ABC):
    @abstractmethod
    def remove_value(self, val):
        raise NotImplementedError


class RemoveNegativeStrategy(FilterStrategy):
    def remove_value(self, val):
        return val < 0
    

class RemoveOddStrategy(FilterStrategy):
    def remove_value(self, val):
        return abs(val) % 2
    

class Values:
    def __init__(self, vals):
        self.vals = vals
    
    def filter(self, strategy):
        res = []
        for n in self.vals:
            if not strategy.remove_value(n):
                res.append(n)
        return res


def main():
    values = Values([-7, -4, -1, 0, 2, 6, 9])

    print(values.filter(RemoveNegativeStrategy()))
    print(values.filter(RemoveOddStrategy()))


if __name__ == '__main__':
    main()
