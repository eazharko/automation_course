results = [
    "calculation result: 15",
    "operation finished: 204",
    "final value: 7",
    "extra result: 33"
]

processed = []

for result in results:
    index = result.index(":")
    number = int(result[index + 2:]) + 10
    processed.append(number)
print(processed)

