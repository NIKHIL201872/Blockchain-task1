import random
# PoW miner: selected by highest computational power
pow_miners = {
    "MinerA": random.randint(50, 100),
    "MinerB": random.randint(50, 100),
    "MinerC": random.randint(50, 100)
}

# PoS stakers: selected by highest stake
pos_stakers = {
    "StakerX": random.randint(1000, 5000),
    "StakerY": random.randint(1000, 5000),
    "StakerZ": random.randint(1000, 5000)
}

# DPoS voters: voting for delegates
delegates = ["Delegate1", "Delegate2", "Delegate3"]
votes = {
    "Voter1": random.choice(delegates),
    "Voter2": random.choice(delegates),
    "Voter3": random.choice(delegates)
}

# Proof of Work (PoW)
pow_winner = max(pow_miners, key=pow_miners.get)
print(" PoW (Proof-of-Work):")
print(f"Miner Powers: {pow_miners}")
print(f"Selected: {pow_winner} with highest power {pow_miners[pow_winner]}")
print("Logic: Highest computational power wins (most work done).\n")

# Proof of Stake (PoS)
pos_winner = max(pos_stakers, key=pos_stakers.get)
print(" PoS (Proof-of-Stake):")
print(f"Staker Stakes: {pos_stakers}")
print(f"Selected: {pos_winner} with highest stake {pos_stakers[pos_winner]}")
print("Logic: Higher stake = higher chance of selection (more invested).\n")

# Delegated Proof of Stake (DPoS)
vote_count = {}
for vote in votes.values():
    vote_count[vote] = vote_count.get(vote, 0) + 1

# Get delegates with most votes
max_votes = max(vote_count.values())
top_delegates = [d for d, v in vote_count.items() if v == max_votes]
dpos_winner = random.choice(top_delegates)

print(" DPoS (Delegated Proof-of-Stake):")
print(f"Votes Cast: {votes}")
print(f"Vote Count: {vote_count}")
print(f"Selected: {dpos_winner} from top-voted delegates {top_delegates}")
print("Logic: Voters elect trusted delegates; one is randomly chosen to produce block.\n")
