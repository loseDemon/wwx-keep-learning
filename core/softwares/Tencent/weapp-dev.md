# 微信小程序开发

## UI框架

see: - [8个最热门的微信小程序 UI 组件库 - V2OA - Way To Office Automation](https://v2oa.com/archives/3/)

### 基于vue

比较推荐的框架是 `weui` 和 `colorui`，其中直接用微信开发工具其实无法获得自动补全的功能，但是可以使用HBuilderX这款软件。

![在HBuilderX中可以对`weui`进行自动补全](https://mark-vue-oss.oss-cn-hangzhou.aliyuncs.com/weapp-dev-1656383048007-b3ec18d7dee03f441494ef939c15ea67a326ef00eb8e52cc309c175901b6f75d.png)  

![在微信开发工具中不可以对`weui`进行自动补全](https://mark-vue-oss.oss-cn-hangzhou.aliyuncs.com/weapp-dev-1656383051926-0b9d3c66753fb388346443e89ec6764f3cc3f5357b0b26720bc23e8b72a17212.png)  

所以使用`HBuilderX`加上一套主流小程序UI框架，然后基于typescript与vue将有不错的开发体验。

或者就要使用基于react的taro框架了，不过小程序端就缺少高质量的ui组件。

### 基于react

据说vant是gitee年度最有价值开源项目之一：[小程序UI框架推荐：Vant让你优雅的飞_牛客博客](https://blog.nowcoder.net/n/e9e2bc2bbbba483aac52ecb6e9d878b8?from=nowcoder_improve)

我看了一下好像确实不错：[Field 输入框 - react vant](https://react-vant.3lang.dev/components/field)

反正比taro-ui要好很多，而weui-wxss又很难用。

