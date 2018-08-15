### 说明

> 这是一个基于TrustNote的区块链投票系统，使用python的flask框架开发。
> 每个投票的选项都会生成一个唯一的TrustNote的钱包地址。
> 用户需要使用TrustNote钱包扫码，投票的过程就是向该选项的TrustNote钱包转账的过程。
> 地址的生成和余额的查询，都是调用headlessRPC实现的。
> 每个投票选项，每隔2-3秒钟检查一次余额，根据整体投票的总额计算出百分比，就是投票的比例。

### 安装

```
sudo pip install -r install
```

### 运行

```
python app.py -p 5000
```

### 体验

打开浏览器，访问：http://localhost:5000

### 演示

我们录制了视频，点击 https://github.com/TrustNoteSamples/VotingSystem/raw/master/demo.mp4 下载后可以观看。

