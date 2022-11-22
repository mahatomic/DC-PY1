def delete(list_, index=None):
    if index is None:
        index = len(list_) - 1
    return list_[:index] + list_[index + 1:]

print(delete([0, 0, 1, 2], index=0))  # [0, 1, 2]
print(delete([0, 1, 1, 2, 3], index=1))  # [0, 1, 2, 3]
print(delete([0, 1, 2, 3, 4, 4]))  # [0, 1, 2, 3, 4]

print(delete([1, 2, 3], index=-1))  # [1, 2, 1, 2, 3]

def another_version_delete(list_, index=-1):
    if index < 0:
        index += len(list_)
    return list_[:index] + list_[index + 1:]

print(another_version_delete([0, 0, 1, 2], index=0))  # [0, 1, 2]
print(another_version_delete([0, 1, 1, 2, 3], index=1))  # [0, 1, 2, 3]
print(another_version_delete([0, 1, 2, 3, 4, 4]))  # [0, 1, 2, 3, 4]

print(another_version_delete([1, 2, 3]))  # [1, 2]
print(another_version_delete([1, 2, 3], index=-3))  # [2, 3]
