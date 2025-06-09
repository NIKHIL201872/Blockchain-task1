import hashlib
import time

class Block:
    def __init__(self, index, data, previous_hash):
        self.index = index
        self.timestamp = time.time()
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.generate_hash()

    def generate_hash(self):
        block_content = f"{self.index}{self.timestamp}{self.data}{self.previous_hash}{self.nonce}"
        return hashlib.sha256(block_content.encode()).hexdigest()

    def __str__(self):
        return (f"Block {self.index}:\n"
                f"  Timestamp     : {self.timestamp}\n"
                f"  Data          : {self.data}\n"
                f"  Previous Hash : {self.previous_hash}\n"
                f"  Hash          : {self.hash}\n"
                f"  Nonce         : {self.nonce}\n")

# Create Genesis Block (first block)
blockchain = []
genesis_block = Block(0, "Genesis Block", "0")
blockchain.append(genesis_block)

# Add two more blocks
block_1 = Block(1, "Transaction A -> B: $50", blockchain[-1].hash)
blockchain.append(block_1)

block_2 = Block(2, "Transaction B -> C: $30", blockchain[-1].hash)
blockchain.append(block_2)

# Display all blocks
print("Initial Blockchain:\n")
for block in blockchain:
    print(block)

#Tampering 
print("\n--- Tampering with Block 1 ---\n")
blockchain[1].data = "Tampered Transaction A -> B: $5000"
blockchain[1].hash = blockchain[1].generate_hash()

# Show updated blocks
for block in blockchain:
    print(block)

# Validate the chain
print("\n--- Chain Validation ---\n")
for i in range(1, len(blockchain)):
    if blockchain[i].previous_hash != blockchain[i-1].hash:
        print(f"Block {i} is INVALID due to tampered hash!")
    else:
        print(f"Block {i} is VALID.")
