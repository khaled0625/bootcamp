# import time
# from unittest import skip
#
# start = time.perf_counter_ns()
# time.sleep(5)
# end = time.perf_counter_ns()
#
# elapsed_ms = (end - start) * 1_100_100
# print(f"Elapsed time: {elapsed_ms}.ms")

class Person:
    def __init__(self, name: str,age: int) -> None:
        self.name = name
        self.age = age

    @property
    def age(self) -> int:
        return  self._age

    @age.setter
    def age(self, value: int) -> None:
        assert 0 <= value <= 200
        self._age = value

    def __eq__(self, other):
        return self.name == other.name and self.age == other.age


x = Person("x", 12)
y = Person("x", 12)

print(x.__eq__(y))

