# gopro蓝牙与wifi无线通信研究

## 背景

根据[Open GoPro](https://gopro.github.io/OpenGoPro/)，我们已知gopro需要通过蓝牙进行配对，然后启动gopro的无线网络，继而可以被手机与mac电脑通过无线连接，并获取资源管理权限。

![picture 1](https://mark-vue-oss.oss-cn-hangzhou.aliyuncs.com/gopro-wireless-communication-research-1654569155579-9e8f57e526bb4480bb596a1bf693ed3c9eb6294659151125d801d2b584e9b7d2.png)  

问题在于蓝牙部分，直接搜索是搜索不到的，需要通过手机的app：GoPro Quik。see： [How-to-Pair-the-Camera-with-the-GoPro-App](https://gopro.com/help/articles/block/How-to-Pair-the-Camera-with-the-GoPro-App?fbclid=IwAR2d_xqmcIdRE1XMKMUuP83p0I0H9O-bS8PllFN6mZSfeLkVtMXvpmqPZKs#HERO9Black)

![picture 19](https://mark-vue-oss.oss-cn-hangzhou.aliyuncs.com/gopro-wireless-communication-research-1654567873832-05980ed13118afa50698539554d758271092cfb5cdd1c597c0589b4613574118.png)  

我们感兴趣的部分是，为什么如此，以及如何才能实现在mac电脑上直接连接gopro，从而完成gopro控制服务自动化。

## 如何实现mac电脑上直连gopro：基于`Open-GoPro`

ref:

- [Tutorials : Open GoPro](https://gopro.github.io/OpenGoPro/tutorials/)

### fixed: pass: `macOS 12 requires non-empty service_uuids`

这个不用管，bleak的问题，mac12.4已经修复了，目前我的系统是12.5。

### fixed: cannot receive response when executing `tutorial_2_send_ble_commands/ble_command_set_shutter.py.py`

这个问题其实归根结底，是蓝牙部分的问题，参考：[Getting Response Timeout Running the Tutorial · Issue #172 · gopro/OpenGoPro](https://github.com/gopro/OpenGoPro/issues/172)可以得知，只要在`client.write_gatt_char`函数里带上`True`参数，就可以正确返回了。

我的做法是，直接把整个文件夹里的这个函数，都正则替换了。不然就要改底层的`bleak`，不太合适。

### fixed: wifi无法连接上

这个问题，是因为我原先的gopro名（手机quik第一次连上gopro后为其取的名）为`MarkShawn's GoPro9 Black`里包含了一个单引号。

而`open-gopro`的无线模块的源代码`venv/lib/python3.9/site-packages/open_gopro/wifi/adapters/wireless.py`中执行mac系统调用时的外层也是单引号，导致命令被转义从而执行失败。这部分代码有优化的空间，可以提个PR，不过目前最好的做法是断开自己的gopro重新连接然后取个不带单引号的名字，就没问题了。

![picture 1](https://mark-vue-oss.oss-cn-hangzhou.aliyuncs.com/gopro-wireless-communication-research-1654619256564-a7a72cb7843648e4b99d617c0bda1a2cd08ffcdd916d145a046857bbe99e590f.png)  

### TODO: 提个gopro的pr

## PASS: 另一种解决方案：`GoPro WebCam`

参考：

- [How To Use Your GoPro As A Webcam](https://community.gopro.com/s/article/GoPro-Webcam?language=en_US#Mac%20Webcam)
- [(129) GoPro Webcam Mode! Setup guide for Zoom, OBS, Skype, Teams, and more! - YouTube](https://www.youtube.com/watch?v=UsPEK5Mo7UA)

不过我目前遇到的问题是，下载安装`GoPro WebCam`后就提示重启，重启后它就不见了，所以暂时还没法用`GoPro WebCam`，不知道为啥。

