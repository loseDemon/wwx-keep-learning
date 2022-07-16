# miniprogramme-howto

## how to parse exif info from image

核心参考实现：

- [找回微信小程序丢失的Exif-实战教程-小程序社区-微信小程序-微信小程序开发社区-小程序开发论坛-微信小程序联盟](https://www.wxapp-union.com/article-7247-1.html)
- [mattiasw/ExifReader: A JavaScript Exif info parser.](https://github.com/mattiasw/ExifReader)

其他失败的实现：

- [前端图片信息解析Exif.js_偶尔躲躲乌云_0的博客-CSDN博客_exif.js官方实例](https://blog.csdn.net/Aurora_1970s/article/details/122845070)

其他参考实现：

- 貌似可用，但现在不需要了：[获取图片exif元数据信息 | 微信开放社区](https://developers.weixin.qq.com/community/develop/doc/00040c207383783880b79b3cb56804)
- [Exif大师--小程序 - 简书](https://www.jianshu.com/p/d50596296143)

相关问题：

- [微信小程序chooseImage接口，IOS返回的照片丢失exif信息问题 | 微信开放社区](https://developers.weixin.qq.com/community/develop/doc/0000a44e964e68c6019c080b55b000)

### 图片转base64

- [Taro 本地图片上传转Base64 - KevinTseng - 博客园](https://www.cnblogs.com/KevinTseng/p/14722649.html)

## 微信文件位置相关

- [图片、缓存与文件_微信云开发学习指南 | 云开发CloudBase - 一站式后端云服务](https://cloudbase.net/community/guides/handbook/tcb16.html)

- 回复需要上传：[wx.chooseImage返回的tempFilePaths路径为什么读不出图片？ | 微信开放社区](https://developers.weixin.qq.com/community/develop/doc/000228ddb9ca281b3c2b0bb1356c00)、 [关于小程序临时文件如何解析？如HTTP://TMP 这种。 | 微信开放社区](https://developers.weixin.qq.com/community/develop/doc/000622528b4c1075464be1eb45d000)

- [存储 | 微信开放文档](https://developers.weixin.qq.com/miniprogram/dev/framework/ability/storage.html)

- uniapp相关：[小程序 本地临时文件tempFilePaths和base64互转_liu__software的博客-CSDN博客_base64转临时文件](https://blog.csdn.net/a460550542/article/details/122079028)