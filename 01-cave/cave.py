import random

def run_cave(knows_secret: bool, rounds: int) -> bool:
    for _ in range(rounds):
        peggy_side = random.choice("AB")
        victor_asks = random.choice("AB")
        if peggy_side != victor_asks and not knows_secret:
            return False          # stuck on the wrong side of the door
    return True

trials = 100_000
for rounds in (1, 5, 10, 20):
    wins = sum(run_cave(False, rounds) for _ in range(trials))
    print(f"{rounds:>2} rounds: bluffer wins {wins / trials:.5%} of the time")
