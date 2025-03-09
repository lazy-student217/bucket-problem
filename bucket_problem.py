from collections import deque
from copy import copy
from functools import reduce
from operator import mul


def bucket_bfs(
    buckets: list[int], initial_state: list[int] | None = None
) -> list[list[list[int]]]:
    if initial_state is not None:
        assert len(buckets) == len(initial_state) and all(
            0 <= initial_state[i] <= buckets[i] for i in range(len(buckets))
        )
    else:
        initial_state = [0] * len(buckets)
    result = []
    visited = set([tuple(initial_state)])
    queue = deque()
    queue.append(initial_state)
    while len(queue) > 0:
        level = []
        for _ in range(len(queue)):
            bucket_state: list[int] = queue.popleft()
            level.append(bucket_state)
            for i in range(len(buckets)):
                # Fill
                if bucket_state[i] != buckets[i]:
                    copied_state = copy(bucket_state)
                    copied_state[i] = buckets[i]
                    if tuple(copied_state) not in visited:
                        visited.add(tuple(copied_state))
                        queue.append(copied_state)
                if bucket_state[i] != 0:
                    # Transfer
                    for j in range(len(buckets)):
                        if i != j and bucket_state[j] != buckets[j]:
                            copied_state = copy(bucket_state)
                            copied_state[j] += min(
                                buckets[j] - bucket_state[j], bucket_state[i]
                            )
                            copied_state[i] -= min(
                                buckets[j] - bucket_state[j], bucket_state[i]
                            )
                            if tuple(copied_state) not in visited:
                                visited.add(tuple(copied_state))
                                queue.append(copied_state)
                    # Dispose
                    copied_state = copy(bucket_state)
                    copied_state[i] = 0
                    if tuple(copied_state) not in visited:
                        visited.add(tuple(copied_state))
                        queue.append(copied_state)
        result.append(level)
    return result


def get_input() -> tuple[list[int], list[int] | None]:
    while True:
        buckets_capacity = input("Buckets capacity: ").strip()
        try:
            buckets = list(map(lambda s: int(s.strip()), buckets_capacity.split("|")))
            break
        except ValueError:
            print("Failed to parse... Please type again")
    while True:
        initial_state_str = input("Initial state: ").strip()
        if initial_state_str == "":
            initial_state = None
            break
        else:
            try:
                initial_state = list(
                    map(lambda s: int(s.strip()), initial_state_str.split("|"))
                )
                break
            except ValueError:
                print("Failed to parse... Please type again")

    return buckets, initial_state


def main() -> None:
    buckets, initial_state = get_input()
    print("-----")
    result = bucket_bfs(buckets, initial_state=initial_state)
    for level_num, level in enumerate(result):
        print(f"{level_num}: ", end="")
        for bucket_state in level:
            print(f" {'|'.join(map(str, bucket_state))} ", end="")
        print("")  # newline
    print("-----")
    # Data
    state_count = sum(len(level) for level in result)
    ideal_state = reduce(mul, map(lambda x: x + 1, buckets), 1)
    cover_rate = state_count / ideal_state * 100
    print(
        f"STATE COUNT: {state_count}\nIDEAL STATE COUNT: {ideal_state}\nCOVER RATE: {round(cover_rate, 1)}%"
    )


if __name__ == "__main__":
    main()
