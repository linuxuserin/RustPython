import itertools

# count

# default arguments
c = itertools.count()
assert next(c) == 0
assert next(c) == 1
assert next(c) == 2

# positional
c = itertools.count(2, 3)
assert next(c) == 2
assert next(c) == 5
assert next(c) == 8

# backwards
c = itertools.count(1, -10)
assert next(c) == 1
assert next(c) == -9
assert next(c) == -19

# step = 0
c = itertools.count(5, 0)
assert next(c) == 5
assert next(c) == 5

# itertools.count TODOs: kwargs and floats

# step kwarg
# c = itertools.count(step=5)
# assert next(c) == 0
# assert next(c) == 5

# start kwarg
# c = itertools.count(start=10)
# assert next(c) == 10

# float start
# c = itertools.count(0.5)
# assert next(c) == 0.5
# assert next(c) == 1.5
# assert next(c) == 2.5

# float step
# c = itertools.count(1, 0.5)
# assert next(c) == 1
# assert next(c) == 1.5
# assert next(c) == 2

# float start + step
# c = itertools.count(0.5, 0.5)
# assert next(c) == 0.5
# assert next(c) == 1
# assert next(c) == 1.5
