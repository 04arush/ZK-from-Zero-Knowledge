claims = {
    "I paid you, but nobody else can see the amount":      "hiding",
    "These 5,000 transactions were executed correctly":     "compression",
    "I'm over 18 (and that's all you'll learn)":            "hiding",
    "I'm one of the 300 people allowed to vote":            "hiding",
    "Our users' balances add up to $Y, none are negative":  "both",
}

score = 0
for claim, answer in claims.items():
    guess = input(f'"{claim}"\n  hiding / compression / both? ').strip().lower()
    if guess == answer:
        score += 1
        print("  ✅ yep")
    else:
        print(f"  ❌ it's mostly {answer}")
print(f"\nYou got {score}/{len(claims)}")
