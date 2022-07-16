# 一种基于自动化整理微信朋友圈的解决方案

1. [背景](#背景)
2. [需求分析](#需求分析)
3. [方案分析](#方案分析)
    1. [解决方案一：基于爬虫](#解决方案一基于爬虫)
    2. [解决方案二：基于运行时逆向](#解决方案二基于运行时逆向)
    3. [解决方案三：基于本地数据库破解](#解决方案三基于本地数据库破解)
    4. [解决方案四：基于自动化技术](#解决方案四基于自动化技术)
4. [自动化实现分析](#自动化实现分析)

## 背景

今天偶然之间，突然想看看自己最早阶段的朋友圈是什么样子，不看不知道，一看吓一跳，那是九年前、八年前、七年前的自己，十足的逗比、没有目标、没有方向，不能提供价值：

![picture 10](https://mark-vue-oss.oss-cn-hangzhou.aliyuncs.com/wechat-moments-dump-1656138484175-e1854677b109bae6e14c030da09b246d9ef728c94647185e7d9ad520f10c5e7b.png)  

我第一时间想到的就是删除：赶紧和那个中二少年一刀两断，将它快快地挫骨扬灰，仿佛从不存在一样。

但很快地我就挫败了，因为竟然会有一天连续发如此多条消息，以至于删都来不及：

![picture 11](https://mark-vue-oss.oss-cn-hangzhou.aliyuncs.com/wechat-moments-dump-1656138681921-d1416f216062f0966ab68b04140aa4aa74850e4663bf08843226661a62b256c6.png)  

同时，我发现了一件有趣的事：绝大多数几年前转的消息，都已经无法再查看了，而这其中的又绝大多数都是营销号。由此可见，“做时间的朋友”真地一点都没错。我也绝不容许自己再浪费无数的时间与青春在各种营销号上，如果可以，短文章、短视频之类的也要尽可能地规避。

当然，删除难免产生代价，我们不得不承认，无论过去的自己好不好看、辉不辉煌、认不认可，那都真实地属于自己，是自己密不可分的一部分。

因此，一键删除是对自己成长的不负责任，也许我们可以做的是，先保存，再按条件删除。

但这样的目标，显然需要借助程序的手段。

## 需求分析

1. 支持导出自己微信朋友圈的所有内容
    1. 导出的内容应可复现，即能够保有至少不少于原有朋友圈内展示的信息量
2. 支持删除特定的朋友圈

## 方案分析

从需求分析来看，需求1属于批量数据获取(get)，需求2属于服务器请求(put/post)，两者尚有区别。

从技术角度看，目前有几类不同的解决方案。

### 解决方案一：基于爬虫

第一类是传统的爬虫，对微信桌面端或者移动端进行抓包，分析数据包，得到目标网址与参数，然后程序化模拟。但实际情况是，由于微信对朋友圈的数据做了加密处理，因此抓包得到的数据都是密文，我们缺少解密算法，因此无法从中提取有效信息。此路不可行。

### 解决方案二：基于运行时逆向

第二类就是逆向。客户端在收到服务端的数据后，会在客户端内进行解密，然后渲染到最终的设备上，使用逆向的手段可以hook解密的关键时刻，从而获得真实的明文。在以前，普遍使用的是在安卓设备上root后基于xposed框架进行分析。逆向的门槛较高，对设备的破坏力度较大，并且封号风险较高，github上目前有以下几个项目均与这有关，可供参考：

- [Chion82/WeChatMomentExport: Xposed module to export WeChat moments data to JSON(微信朋友圈数据导出Xposed模块)](https://github.com/Chion82/WeChatMomentExport)

- [Chion82/WeChatMomentStat-Android: Get your WeChat Moment statistics and export Moments to JSON. 微信朋友圈数据统计、导出工具](https://github.com/Chion82/WeChatMomentStat-Android)

其他参考文章有：

- [微信逆向之朋友圈 - 掘金](https://juejin.cn/post/6844903846595002376)

### 解决方案三：基于本地数据库破解

在我之前研究整理的【公众号文章：微信数据库破解】中，已经实现了对PC端微信数据库的破解，能够完整还原微信聊天记录，不过当时并未涉及对朋友圈数据的获取与分析。

但原理是相通的。

参考[Mr0x01/WeChatMomentExport-iOS: iOS微信朋友圈数据库导出](https://github.com/Mr0x01/WeChatMomentExport-iOS)这篇文章可以知道，在我们刷朋友圈时微信会不断生成朋友圈的缓存数据写入数据库，这样，我们基于之前拿到的cipher秘钥就可以进入这个数据库查看明文信息。

本方案由于可以离线操作本地数据库，是所有实现方案中最安全的。但该方案不满足需求目标二，即不支持我执行删除的动作，所以不在本期考虑范围内。

我打算后续将基于本解决方案解析、操纵、可视化微信聊天记录与朋友圈记录综合起来再写篇文章。

### 解决方案四：基于自动化技术

自动化的解决方案应该来说是最直观的，因为它就是在模拟我们人的操作，程序执行的过程中，我们的手机也是处于一直开启并不断操作的状态。

自动化过程中，将涉及到一些内容识别的问题，不过这些问题在一个良好的自动化框架下，其实已经不是问题，因为它们可以自动识别自动化过程中的元素结点位置以及里面的内容。

本章将着重介绍使用自动化技术操作微信朋友圈的解决方案。

## 自动化实现分析
