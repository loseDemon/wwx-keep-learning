# Keep Learning (V0.15.42)

- [Background](#background)
- [environment (not necessary)](#environment-not-necessary)
- [project contents](#project-contents)

## Background

我认为集中化管理、持续更新工作笔记，长期来看，是有所益的。

## environment (not necessary)

1. zsh(`zsh --version`): zsh 5.8 (x86_64-apple-darwin20.0)
2. vscode(`code --version | tr "\n" " "`): 1.63.2 899d46d82c4c95423fb7e10e68eba52050e30ba3 x64
3. os(`uname -a`): Darwin mark-mac.local 20.6.0 Darwin Kernel Version 20.6.0: Wed Jan 12 22:22:42 PST 2022; root:xnu-7195.141.19~2/RELEASE_X86_64 x86_64

## project contents

```sh
core
├── AndroidFramework
│   ├── TaskA1-aosp-pull
│   │   └── aosp-pull.md
│   ├── TaskA2-aosp-compile
│   │   ├── aosp-compile-bugfix.md
│   │   └── aosp-compile-howto.md
│   ├── TaskA3-aosp-changes
│   │   └── aosp-changes.md
│   ├── TaskA4-sf-research
│   │   ├── arpara-distortion-logic.md
│   │   ├── drawLayersArpara.cpp
│   │   ├── logcat_settings-gallery3d.log
│   │   └── sf-howto.md
│   ├── TaskA5-sf-patches
│   │   ├── sf-patch-research-2021.md
│   │   └── sf-patch-research-2022.md
│   ├── TaskA6-aosp-read
│   │   └── aosp-read-howto.md
│   ├── TaskA7-aosp-coding
│   │   └── aosp-coding-howto.md
│   ├── TaskB1-hmdservice-compile
│   │   └── how-to-compile-arpara-hmdservice-on-AOSP10.md
│   ├── TaskB2-hmdservice-integration
│   │   └── native-service-integration-howto.md
│   ├── TaskC1-timewarp
│   │   ├── define_shader.h
│   │   ├── tw-bugfix.md
│   │   ├── tw-research.md
│   │   └── tw-research.png
│   ├── TaskC2-opengl
│   │   └── opengl-howto.md
│   ├── TaskD1-arpara-glass
│   │   └── arpara-glass-howto.md
│   ├── TaskE1-rockchip4
│   │   ├── depreciated
│   │   ├── rockchip4-flash-manual.md
│   │   ├── rockchip4-howto.md
│   │   └── rockchip4-vr-manual.md
│   ├── adb-howto.md
│   ├── arpara-vr-logic.md
│   ├── depreciated
│   │   ├── TaskA6-emulator
│   │   └── depreciated-surfaceflinger-patch-research.md
│   ├── frameworks-howto.md
│   └── mark_vr-principle-and-implementation.md
├── OS
│   ├── Linux
│   │   ├── android-repo-init.sh
│   │   ├── centos-init-manual.md
│   │   ├── depreciated
│   │   ├── linux-commands.md
│   │   ├── linux-debug.md
│   │   ├── linux-howto.md
│   │   ├── linux-init.sh
│   │   ├── linux-terminator-howto.md
│   │   ├── sed
│   │   └── ubuntu-init-manual.md
│   ├── Mac
│   │   ├── alfred-howto.md
│   │   ├── auto-scripts.app
│   │   ├── auto-scripts.applescript
│   │   ├── ios-hack.md
│   │   ├── mac-apps.md
│   │   ├── mac-automation.md
│   │   ├── mac-bugfix.md
│   │   ├── mac-howto.md
│   │   ├── mac-migrate.md
│   │   ├── mac-todo.md
│   │   ├── mac-wechat-hack.md
│   │   └── mac-what.md
│   ├── Windows
│   │   └── windows-howto.md
│   ├── cross-platform-howto.md
│   ├── iOS.md
│   └── virtual-machine
│       ├── virtualbox-howto.md
│       └── vmware-howto.md
├── SLAM
│   ├── ORB-SLAM3_learning.md
│   ├── slam-research.md
│   ├── slambook2-ch13.md
│   ├── slambook2_coding-part.md
│   ├── slambook2_learning.md
│   └── slambook2_theoretical-part.md
├── ai
│   ├── 1.1.李航-统计学习与方法
│   ├── 1.2.周志华-机器学习
│   ├── 1.3.PRML
│   ├── 2.1.花书
│   ├── 3.1.推荐系统
│   └── 3.2.NLP
├── coding
│   ├── CPP
│   │   ├── build
│   │   ├── cpp-howto.md
│   │   ├── hanoi
│   │   ├── kmp
│   │   └── test
│   ├── CSS
│   │   ├── css-howto.md
│   │   ├── flex
│   │   └── scss
│   ├── Go
│   │   └── go-howto.md
│   ├── HTML
│   │   └── html-howto.md
│   ├── JS
│   │   ├── CodeQuality_eslint_prettier_jest
│   │   ├── Electron
│   │   ├── React
│   │   ├── Vue
│   │   ├── database.md
│   │   ├── develop-remark-plugin.md
│   │   ├── js-bugfix.md
│   │   ├── js-discuss.md
│   │   ├── js-howto.md
│   │   ├── npm_yarn-bugfix.md
│   │   ├── npm_yarn-howto.md
│   │   └── redux.md
│   ├── Java
│   │   ├── java-howto.md
│   │   └── maven-howto.md
│   ├── Latex
│   │   ├── out
│   │   ├── problem_01.tex
│   │   └── test.tex
│   ├── Markdown
│   │   └── markdown-howto.md
│   ├── Python
│   │   ├── Python-Finance
│   │   ├── fastapi
│   │   ├── jupyter-howto.md
│   │   ├── pandas-howto.md
│   │   ├── python-bugfix.md
│   │   ├── python-howto.md
│   │   └── python开发笔记.md
│   ├── TS
│   │   ├── ts-bugfix.md
│   │   └── ts-howto.md
│   ├── Unity
│   │   └── unity-howto.md
│   ├── coding-best-practice.md
│   ├── coding-design.md
│   └── regex
│       └── regex-howto.md
├── cs
│   ├── 1.1.计组
│   ├── 2.1.操作系统
│   ├── 2.2.汇编
│   ├── 3.1.计网
│   ├── 4.1.数据结构
│   └── 4.2.算法
├── index.yaml
├── math
│   ├── 1.1.数学分析
│   └── 2.1.概率论
├── notes
│   ├── discarded
│   │   ├── fengxian
│   │   ├── gopro-wireless-communication-research.md
│   │   ├── mark_0519.md
│   │   ├── mark_wxmp-dev-note.md
│   │   └── soulmate
│   ├── finished-but-not-uploaded
│   │   └── mark_assist-zkj-flask-route_record.md
│   ├── ios-ssh.md
│   ├── jkb_bj_forge-howto.md
│   ├── mark_the-world-from-the-eye-of-a-coder.md
│   ├── styles
│   │   ├── mdnice-purple.css
│   │   ├── mdnice-自定义-红绯.css
│   │   └── mdnice-自定义-对抗紫.css
│   ├── uploaded
│   │   ├── 2022-I-am-me.md
│   │   ├── DataAnalysis-Gaokao.md
│   │   ├── auto-voice2srt.md
│   │   ├── douban_rent-houses
│   │   ├── gopro-timestamp.md
│   │   ├── ios-automation.md
│   │   ├── life-is-not-easy.md
│   │   ├── mark_12h-struggle-with-webpack.md
│   │   ├── mark_2022-live
│   │   ├── mark_2022-live.md
│   │   ├── mark_beike-hr.md
│   │   ├── mark_core-notes-of-linux.md
│   │   ├── mark_eidt-mp3-meta.md
│   │   ├── mark_happy-new-year-of-2022.md
│   │   ├── mark_im-working-now.md
│   │   ├── mark_massage_breo-dream6.md
│   │   ├── mark_my2021.md
│   │   ├── mark_our-lives.md
│   │   ├── mark_self-cultivation_of_engineer.md
│   │   ├── mbti
│   │   └── my-gopro.md
│   └── wechat-moments-dump.md
├── scripts
│   ├── __init__.py
│   ├── __pycache__
│   ├── aosp_download
│   │   ├── __init__.py
│   │   └── aosp_specific_dir_download.py
│   ├── base
│   │   ├── __init__.py
│   │   ├── __pycache__
│   │   ├── logging.py
│   │   └── settings.py
│   ├── boilerplate_electron_archive
│   │   ├── demo1.sh
│   │   ├── demo2.sh
│   │   ├── demo3.sh
│   │   ├── demo4.sh
│   │   ├── demo5.sh
│   │   ├── demo6.sh
│   │   ├── demo7.sh
│   │   └── readme.md
│   ├── boilerplate_electron_ts_react_antd_tailwindcss
│   │   ├── boilerplate_electron_ts_react_antd_tailwindcss.md
│   │   └── boilerplate_electron_ts_react_antd_tailwindcss.sh
│   ├── china_cities
│   │   ├── __init__.py
│   │   ├── city_convert_from_list.py
│   │   ├── city_convert_from_raw.py
│   │   ├── city_data_list.json
│   │   └── city_data_raw.json
│   ├── fast_cnki_translate
│   │   ├── __init__.py
│   │   ├── __pycache__
│   │   ├── base.py
│   │   ├── gen_num.py
│   │   ├── icons
│   │   ├── main.py
│   │   ├── readme.md
│   │   ├── scrape_covers
│   │   ├── settings.py
│   │   ├── test
│   │   └── workflow.py
│   ├── git_auto_version
│   │   └── git_auto_version.sh
│   ├── github_download
│   │   ├── __init__.py
│   │   ├── __pycache__
│   │   ├── github-dir-download-main.py
│   │   ├── speak_selection
│   │   └── test_main.py
│   ├── merge_imgs
│   │   ├── __init__.py
│   │   └── migrate_imgs.py
│   ├── mp42mp3
│   │   ├── __init__.py
│   │   └── main.py
│   ├── my-pdf-parser
│   │   ├── __pycache__
│   │   ├── data
│   │   ├── readme.md
│   │   └── src
│   ├── ncm2pm3
│   │   ├── __init__.py
│   │   └── main.py
│   ├── ocr
│   │   ├── __init__.py
│   │   └── huawei_ocr.py
│   ├── voice2srt
│   │   ├── __init__.py
│   │   └── main.py
│   └── web_scrape
│       ├── __init__.py
│       └── scrapeAudioFromMorganStanleyForTanKunming
└── softwares
    ├── Adobe
    │   └── PS
    ├── Charles
    │   └── charles-howto.md
    ├── Database
    │   └── Mysql
    ├── FCPX
    │   └── my318-2021
    ├── Git
    │   ├── git-bugfix.md
    │   └── git-howto.md
    ├── Google
    │   ├── ChromeUsage
    │   └── GoogleSearch
    ├── JetBrains
    │   ├── AndroidStudio
    │   ├── Clion
    │   ├── Idea
    │   ├── Pycharm
    │   ├── WebStorm
    │   └── jetbrains-howto.md
    ├── MiniProgramme
    │   └── MiniProgramme-howto.md
    ├── TamperMonkey
    │   ├── CompTag.tsx
    │   ├── TamperMonkey-howto.md
    │   ├── bilibili-video2title
    │   ├── composite-search-engine
    │   ├── douban-filter-houses
    │   ├── node_modules
    │   ├── package-lock.json
    │   ├── package.json
    │   ├── tm.sh
    │   ├── tsconfig.json
    │   ├── utils.js
    │   └── utils.ts
    ├── Tencent
    │   ├── weapp-dev.md
    │   └── wechat-todo.md
    ├── VSCode
    │   ├── vscode-bugfix.md
    │   ├── vscode-extensions-howto.md
    │   ├── vscode-howto.md
    │   └── vscode-todo.md
    ├── Vim
    │   └── vim-howto.md
    ├── docs
    ├── mark-recommended-softwares.md
    ├── mongodb
    │   ├── mongodb-bugfix.md
    │   └── mongodb-howto.md
    └── nginx
        └── nginx-howto.md

137 directories, 184 files
```