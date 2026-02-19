from collections.abc import Collection

def contains(key, data: Collection) -> bool:
    """
    :param key: The key being searched for
    :param data: A sequence of keys in increasing order
    :return: True if key is in data
    """
    lo = 0
    hi = len(data)
    while lo <= hi:
        mid = (lo + hi) // 2
        if key < data[mid]:
            hi = mid - 1
        elif key == data[mid]:
            return True
        else:
            lo = mid + 1
    return False


# d = list(range(6))
# d = ['a', 'b', 'c', 'd']
d = 'abcd'
for i in d:
    assert contains(i, d)