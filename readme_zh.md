### 说明

> 这是一个基于TrustNote的区块链投票系统，使用python的flask框架开发。

### 原理

系统首先导入pythonSDK，该SDK文件为rpc.py，是python调用headlessRPC的接口。

```
import rpc
```

1. 每个投票的选项都会生成一个唯一的TrustNote的钱包地址。

关键代码：
```
rpc.make_a_new_address()
```
2. 用户需要使用TrustNote钱包扫码，投票的过程就是向该选项的TrustNote钱包转账的过程。
3. 地址的生成和余额的查询，都是调用headlessRPC实现的。
4. 每个投票选项，每隔2-3秒钟检查一次余额，根据整体投票的总额计算出百分比，就是投票的比例。

关键代码：
```
rpc.get_balance_of(address)
```

### 安装

投票系统需要配合headlessRPC才能使用。

1. 安装headlessRPC

```
git clone https://github.com/TrustNoteDevelopers/RPC.git
cd RPC
npm install
```

2. 安装投票系统
```
git clone https://github.com/TrustNoteSamples/VotingSystem.git
cd VotingSystem
sudo pip3 install -r install
```

### 运行

1. 运行headlessRPC

在headlessRPC目录下执行：
```
node rpc_service.js
```

2. 运行投票系统

在投票系统目录下执行：
```
python3 app.py -p 8000
```

### 体验

打开浏览器，访问：http://localhost:8000

### 演示

我们录制了视频，点击 https://github.com/TrustNoteSamples/VotingSystem/raw/master/demo.mp4 下载后可以观看。

如果发现bug，欢迎到 https://github.com/TrustNoteSamples/VotingSystem/issues 反馈。

如果对此还有问题不清楚，可以到 http://trustnote.slack.com/ 与我们交流。
