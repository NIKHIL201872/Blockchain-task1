import hashlib
import time

class Block:
    def __init__(self, index, data, previous_hash):
        self.index = index
        self.timestamp = time.time()
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = None

    def generate_hash(self):
        block_content = f"{self.index}{self.timestamp}{self.data}{self.previous_hash}{self.nonce}"
        return hashlib.sha256(block_content.encode()).hexdigest()

    def mine_block(self, difficulty):
        prefix = '0' * difficulty
        start_time = time.time()

        while True:
            self.hash = self.generate_hash()
            if self.hash.startswith(prefix):
                break
            self.nonce += 1

        end_time = time.time()
        print(f"Block {self.index} mined! ")
        print(f"Nonce attempts: {self.nonce}")
        print(f"Time taken   : {round(end_time - start_time, 4)} seconds")
        print(f"Hash         : {self.hash}\n")

    def __str__(self):
        return (f"Block {self.index}:\n"
                f"  Timestamp     : {self.timestamp}\n"
                f"  Data          : {self.data}\n"
                f"  Previous Hash : {self.previous_hash}\n"
                f"  Hash          : {self.hash}\n"
                f"  Nonce         : {self.nonce}\n")

# Difficulty level 
difficulty = 4

# Create blockchain with mining
blockchain = []
genesis_block = Block(0, "Genesis Block", "0")
genesis_block.mine_block(difficulty)
blockchain.append(genesis_block)

block_1 = Block(1, "Alice pays Bob 20 coins", blockchain[-1].hash)
block_1.mine_block(difficulty)
blockchain.append(block_1)

block_2 = Block(2, "Bob pays Charlie 15 coins", blockchain[-1].hash)
block_2.mine_block(difficulty)
blockchain.append(block_2)

# Display all blocks
print("\n--- Final Blockchain ---\n")
for block in blockchain:
    print(block)
