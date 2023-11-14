def first(iterable):
    iterator = iter(iterable)
    try:
        print(next(iterator))
    except StopIteration:
        raise ValueError("Iterable is empty")

    
first ([])

first ([1, 2, 3])

first ([1, 2, 3])

first ({1, 2, 3})
