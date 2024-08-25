import hashlib
import json
from time import time
import random

def generateHash(input_string):
    hashObject = hashlib.sha256()
    hashObject.update(input_string.encode('utf-8'))
    hashValue = hashObject.hexdigest()
    return hashValue

class BlockChain():
    def __init__(self):
        self.chain = []

    def length(self):
        return len(self.chain)
        
    def addBlock(self, currentBlock):
        if(len(self.chain) == 0):
            self.createGensisBlock()
        currentBlock.previousHash = self.chain[-1].currentHash
        isBlockMined = currentBlock.mineBlock()
        if(isBlockMined):
            self.chain.append(currentBlock)
            return True
        return False
    
    def createGensisBlock(self):
        genesisBlock = Block(0, time(), "No Previous Hash.")
        self.chain.append(genesisBlock)
    
    def printChain(self):
        for block in self.chain:
            print("Block Index", block.index)
            print("Timestamp", block.timestamp)
            print("Transactions", block.transactions)
            print( "Previous Hash",block.previousHash)
            print( "Current Hash",block.currentHash)
            print( "Is Valid Block",block.isValid)

            print("*" * 100 , "\n")

    def validateBlock(self, currentBlock):
        previousBlock = self.chain[currentBlock.index - 1]
        if(currentBlock.index != previousBlock.index + 1):
            return False
        
        previousBlockHash = previousBlock.calculateHash()        
        if(previousBlockHash != currentBlock.previousHash):
            return False
        
        # Validating Proof of work
        # Calculate hash for currentBlock and save it in validationHash
        
        
        # Check if letters upto difficulty index are equal to 0 in the validationHash
        
            # Return False
        
        
        return True

class Block:
    def __init__(self, index, timestamp, previousHash):
        self.index = index
        self.transactions = []
        self.timestamp = timestamp
        self.previousHash = previousHash
        self.isValid = None
        self.difficulty = 3
        # Create nonce variable and set it to 0
        
        self.currentHash = self.calculateHash()
       

    def calculateHash(self, timestamp=None):
        if(timestamp == None):
            timestamp = self.timestamp
        blockString = str(self.index) + str(timestamp) + str(self.previousHash) + json.dumps(self.transactions, default=str) + str(self.nonce)
        return generateHash(blockString)

    def mineBlock(self):
        target = "0" * self.difficulty
        # Set the nonce limit (set lower limit to see if code works fine)
        
        
        while self.currentHash[:self.difficulty] != target:
           # Increment self.nonce 
           
            # Update the timestamp as extra nonce
           
            self.currentHash = self.calculateHash()        
            # Break the loop once attempts reach the mining limit 
           
           
                # Instead of exiting the loop set the nonce to 0
        
        return True

    def addTransaction(self, transaction):
        if transaction:
            self.transactions.append(transaction)
            if len(self.transactions) == 3:
                return "Ready"
            return "Add more transactions"


       
