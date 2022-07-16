# aosp coding howto

## use `androidmk` to change `mk` file into `bp` file

path: `out/soong/host/linux-x86/bin/androidmk`

```sh
# create soft link
ln -s out/soong/host/linux-x86/bin/androidmk androidmk
```

ref:

- official intro:[Soong 编译系统  |  Android 开源项目  |  Android Open Source Project](https://source.android.google.cn/setup/build?hl=zh-cn)

- [android mk与bp,Android.bp你真的了解吗_方萌-CFT的博客-程序员信息网 - 程序员信息网](https://www.i4k.xyz/article/weixin_34342589/117589957)

- [(23条消息) Android.bp入门指南之Android.mk转换成Android.bp_IT先森-CSDN博客_android.mk转android.bp](https://blog.csdn.net/tkwxty/article/details/104411520)
