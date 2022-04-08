# Module 1 - Create a Blockchain

# mine some block, get actual state blockchain

import datetime
import hashlib
# block hash 전에 인코딩을 위해 json의 dumps함수 사용
import json
# jsonify를 사용해 postman과 상호작용 때 msg를 주고 받음
from flask import Flask, jsonify
# 1. block chain architecture 설계 [building a blockchain]

class Blockchains:
    def __init__(self):
        self.chain = []
        # prev_hash가 0인 이유는 해당 block이 genesis이기 때문에
        self.create_block(proof=1, previous_hash = '0')
    
    # 작업 증명, 블록 채굴 직 후 사용할 함
    def create_block(self, proof, previous_hash):
        block = {'index': len(self.chain) + 1,
                 'timestamp': str(datetime.datetime.now()),
                 'proof': proof,
                 'previous_hash': previous_hash}
        self.chain.append(block)
        return block
    
    def get_previous_block(self):
        return self.chain[-1]
    
    def proof_of_work(self, previous_proof):
        new_proof = 1
        check_proof = False
        while check_proof is False:
            hash_operation = hashlib.sha256(str(new_proof**2 - previous_proof**2).encode()).hexdigest()
            if hash_operation[:4] == '0000':
                check_proof=True
            else:
                new_proof += 1 
        return new_proof
# 2. block chain state 표시 함수(postman) + new block mining 함수


