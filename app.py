import time
from flask import Flask, request
import requests, json
from bc.block import Block

from bc.blockchain import Blockchain

app =  Flask(__name__)

blockchain = Blockchain()

@app.route('/chain', methods=['GET'])
def get_chain():
    chain_data = []
    for block in blockchain.chain:
        chain_data.append(block.__dict__)
    data=json.dumps({"length": len(chain_data), "chain": chain_data})
    return data

@app.route('/add')
def add_block():
    last_block=blockchain.last_block
    block=Block(last_block.index + 1, [], time.time(), last_block.hash)
    proof=blockchain.proof_of_work(block)
    added_block=blockchain.add_block(block, proof)
    print( str(added_block))
    res=blockchain.add_to_chain(block)
    return str(res)

@app.route('/add_transaction')
def add_tr():
    transaction=1
    blockchain.add_new_transaction(transaction)
    return 'done'

app.run(debug=True, port=5000)