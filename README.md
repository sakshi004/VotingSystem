## A Simple Blockchain Voting System

### Description

This is a blockchain voting system based on TrustNote, developed using Python Flask.

### Principle

The system first imports pythonSDK, the SDK file is rpc.py, which is the interface that Python calls headlessRPC.

```
import rpc
```
Then we need to generate a unique TrustNote wallet address for each candidate.

Key code:

```
rpc.make_a_new_address()

```

Users need to use the TrustNote wallet to scan the bar code along with the candidate he wants to vote. The voting process is actually the process of transferring token to the candidate's TrustNote wallet address.

The generation of the address and the query of the balance are all implemented by calling headlessRPC.

For each vote, the balance will be checked every 2-3 seconds, and the percentage of the votes for each candidate is calculated based on the amount of tokens each candidate receives versus the total.

Key code:

```
rpc.get_balance_of(address)
```

### Installation


The voting system needs to be used with headlessRPC.


1. Install headlessRPC

```
git clone https://github.com/TrustNoteDevelopers/RPC.git

cd RPC

npm install
```

2. Install voting system

```
git clone https://github.com/TrustNoteSamples/VotingSystem.git

cd VotingSystem

pip3 install -r install
```

### Run

1. Run headlessRPC Execute in the headlessRPC directory:

```
node rpc_service.js
```

Running the voting system

Execute in the voting system directory:

```
python3 app.py -p 8000
```

### Experience

Open your web browser and visit: http://localhost:8000

### Demonstration

We recorded the video and can watch it from at https://github.com/TrustNoteSamples/VotingSystem/raw/master/demo.mp4.

If you find bugs, feel free to submit it at https://github.com/TrustNoteSamples/VotingSystem/issues.

If you still have questions about this, you can talk to us at http://trustnote.slack.com/.
 
