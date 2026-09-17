def calPoints(self, operations: list[str]) -> int:
    record = []
    rules = {
        "+": lambda arr: arr.append(arr[-1]+arr[-2]),
        "D": lambda arr: arr.append(arr[-1]*2),
        "C": lambda arr: arr.pop()
    }
    for operation in operations:
        if operation in rules:
            rules[operation](record)
            continue
        record.append(int(operation))
    return sum(record)
        