# VotingSystem

### Description

> This is a blockchain voting system based on TrustNote, developed using python's flask framework.

### principle

The system first imports [pythonSDK](https://github.com/TrustNoteDevelopers/pythonSDK), the SDK file is rpc.py, which is the interface that Python calls [headlessRPC](https://github.com/TrustNoteDevelopers/RPC).

```
import rpc
```

Each voting option generates a unique TrustNote wallet address.

Key code:

```
rpc.make_a_new_address()
```

Users need to use the TrustNote wallet to scan the code. The voting process is the process of transferring money to the option's TrustNote wallet.

The generation of the address and the query of the balance are all implemented by calling headlessRPC.

For each voting option, the balance is checked every 2-3 seconds, and the percentage is calculated based on the total amount of the overall vote, which is the proportion of the vote.

Key code:

```
rpc.get_balance_of(address)
```

### install

The voting system needs to be used with headlessRPC.

1. Install headlessRPC

```
git clone https://github.com/TrustNoteDevelopers/RPC.git
cd RPC
npm install
```

2. Installation voting system

```
git clone https://github.com/TrustNoteSamples/VotingSystem.git
cd VotingSystem
pip3 install -r install
```

### run

1. Run headlessRPC
Execute in the headlessRPC directory:

```
node rpc_service.js
```

Running the voting system

Execute in the voting system directory:

```
python3 app.py -p 8000
```

### Experience

Open a browser and visit: http://localhost:8000

### Demonstration

We recorded the video and can watch it by downloading it at https://github.com/TrustNoteSamples/VotingSystem/raw/master/demo.mp4.

If you find bugs, feel free to check out https://github.com/TrustNoteSamples/VotingSystem/issues.

If you still have questions about this, you can talk to us at http://trustnote.slack.com/.
