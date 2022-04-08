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

# 2. block chain state 표시 함수(postman) + new block mining 함수
