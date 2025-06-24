for i in range(1,6):
    print(f"{i:4}", end="")
    for j in range(1,6):
        result = i * j
        print(f"{result:4}", end="")
    print()