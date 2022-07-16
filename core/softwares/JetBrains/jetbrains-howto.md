# jetbrains-howto

1. [nbsp空格显示设置](#nbsp空格显示设置)
2. [jetbrains各版本下载链接生成脚本](#jetbrains各版本下载链接生成脚本)
3. [BEST-PRACTICE: jetbrains version manage](#best-practice-jetbrains-version-manage)
    1. [1. the plugin of `eval restart`](#1-the-plugin-of-eval-restart)
    2. [2. the approach to manage versions](#2-the-approach-to-manage-versions)
4. [improve jetbrains efficiency](#improve-jetbrains-efficiency)

## nbsp空格显示设置

see: - [2020.2 showing |NBSP| – IDEs Support (IntelliJ Platform) | JetBrains](https://intellij-support.jetbrains.com/hc/en-us/community/posts/360009442799-2020-2-showing-NBSP-)

在`Help | Find Action | Registry | editor.show.special.chars`里设置。

选择显示时的效果：

![picture 1](https://mark-vue-oss.oss-cn-hangzhou.aliyuncs.com/jetbrains-howto-1656906625520-b834c9aa7081ce0f8fea14255222028f1881e4618816dd8e13152c02a88fc208.png)  

选择不显示时的效果：

![picture 2](https://mark-vue-oss.oss-cn-hangzhou.aliyuncs.com/jetbrains-howto-1656906688216-fb4ab848042da8b9b6ae1b6cc157f786e80670190c1c525ca4d1a1c77c5873f8.png)  

## jetbrains各版本下载链接生成脚本

```python
def gen_download_url(software="webstorm", name="WebStorm", version="2020.3.3", suffix="exe"):
    """
    download page (webstorm as the example): https://www.jetbrains.com/webstorm/download/other.html 
    software: {pycharm, webstorm, ...}
    suffix: {exe, dmg}
    """
    url_pycharm_professional = "https://download-cdn.jetbrains.com/python/pycharm-professional-2020.3.5.dmg"
    url_webstorm = "https://download-cdn.jetbrains.com/webstorm/WebStorm-2020.3.3.exe"
    return f"https://download-cdn.jetbrains.com/{software}/{name}-{version}.{suffix}"
```

## BEST-PRACTICE: jetbrains version manage

### 1. the plugin of `eval restart`

plugin repo: https://plugins.zhile.io

plugin name: 'IDE Eval Reset'

![picture 6](https://mark-vue-oss.oss-cn-hangzhou.aliyuncs.com/jetbrains-howto-1642485827260-f451b4ff7ea352b26fd4c6d13a512ff88c8ff067dd754cb9d51e1d979e6af907.png)  

### 2. the approach to manage versions

Download the toolbox at here: [JetBrains Toolbox App: Manage Your Tools with Ease](https://w ww.jetbrains.com/toolbox-app/)

And then download or uninstall specific versions of jetbrains products.

For example, since the hack plugin of `eval start` (which allows you to use jetbrains product periodically freely) won't support the versions of webstorm after 2021.2, we can easily download the old version in toolbox.

![picture 4](https://mark-vue-oss.oss-cn-hangzhou.aliyuncs.com/jetbrains-howto-1642485538134-6f36f7277858541772744c00ac24f01f243fcfd7b282a5aceddd5df6fc72c798.png)  

![picture 5](https://mark-vue-oss.oss-cn-hangzhou.aliyuncs.com/jetbrains-howto-1642485565528-42c0dec28204e8878ecf4f1a59ed5d70ef5d6cb428377f11fcb7cc885e842fd1.png)  

ref:

- [JetBrains全系列软件激活教程激活码以及JetBrains系列软件汉化包](https://www.macwk.com/article/jetbrains-crack)

- [ide - How to downgrade IntelliJ to older version - Stack Overflow](https://stackoverflow.com/questions/18519560/how-to-downgrade-intellij-to-older-version)

## improve jetbrains efficiency

1. Disable all unnecessary plugins
2. Increase memory for IntelliJ IDEA [Help / Change memory settings]
3. Exclude folders and Unload modules
4. Disable on-the-fly import management
5. Pause inspections check

<img alt="picture 1" src="https://mark-vue-oss.oss-cn-hangzhou.aliyuncs.com/1640194669995-jetbrains-howto-bb60024de03a0f70a741740db732e6d44c514c077f1132051728b80595dcc2ae.png" width="480" />  

reference:
- [Simple Steps for Improving Your IDE Performance | The Kotlin Blog](https://blog.jetbrains.com/kotlin/2021/06/simple-steps-for-improving-your-ide-performance/)
