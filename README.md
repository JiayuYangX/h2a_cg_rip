# 《光环2：周年版》全CG导出

本仓库存储的是个人用于《光环2：周年版》CG 导出的相关脚本。导出的 CG 经过修正优化和重新编排。

导出的 CG 下载地址如下：

通过网盘分享的文件：Halo.2.Anniversary.Cinematics.mkv
链接: https://pan.baidu.com/s/1NvWXRHolRUOrxCl5_DgDoA?pwd=6223 提取码: 6223

如果想自行导出，可参考以下流程。

## 特色

本工作流程致力于导出游戏 CG 文件中的所有信息，所有语言都被囊括进来，具体如下：

> 配音：英语、国语（台配）、法语、德语、意大利语、日语、韩语、西班牙语（墨西哥）

> 字幕：英文、简体中文、繁体中文、法文、德文、意大利文、日文、韩文、西班牙文（墨西哥）、西班牙文（西班牙）、葡萄牙文（巴西）

由于 MKV 视频支持设置版本（Edition），本文通过有序章节的形式编排了 9 个版本，具体如下：

> Easy、Normal、Heroic、Legendary、Easy (with Halo 5 Bookends)、Normal (with Halo 5 Bookends)、Heroic (with Halo 5 Bookends)、Legendary (with Halo 5 Bookends)、Full Episodes

不过目前只有部分播放器支持视频版本，而且大多无法查看版本标题。这里推荐我个人的 mpv 播放器配置文件，其中的脚本可以实现显示版本标题的功能：<https://github.com/JiayuYangX/mpv-custom>。

## 错误修复

原本游戏文件里的 CG 有相当多的问题，本导出流程进行了修复，具体如下：

- Ep_032_Post_Credits_Teaser 和 Ep_035_Bookend_Outro 色彩范围转换错误，画面泛白，已修复
- Ep_031_Finale 后半部分字幕与音频时间不同步，已修复
- Ep_033_Day_at_the_Beach 除英文和简体中文外的其他语言字幕都缺失，已修复
- Ep_035_Bookend_Outro 所有语言字幕缺失，已修复
- Ep_004_Theyll_Regret_That_Too 日文字幕出现翻译缺失导致的错误提示，已修复

## 工具依赖

- Rad Video Tools
- FFmpeg
- MKVToolNix
- Python

## 导出流程

1. 准备好剩余空间至少 800 GB 的硬盘（你没听错，导出的未压缩视频就有这么大）
2. 下载相关工具，其中 FFmpeg 和 MKVToolNix 最好配置环境变量
3. 修改 `config.ini` 里的游戏路径、中转路径（就是放 800 GB 临时文件的地方）和导出路径
4. 用 Rad Video Tools 执行 `1.vid.rlst`，将 Bink 文件的视频轨导出为未压缩的 AVI 视频
5. 执行 `2.vid.py`，用 FFmpeg 将刚才的 AVI 视频压缩为 YUV420p、H.264 编码的 MP4 视频
6. 执行 `3.vid.py`，用 FFmpeg 将 Bink 文件中的音频轨混合为多语言的双声道音频
7. 执行 `4.mix2.py`，用 MKVToolNix 里的 mkvmerge 工具将每一段 CG 的视频轨、音频轨、字幕轨合并为 MKV 视频，添加语言信息（`4.mix1.py` 用的是 FFmpeg，但和后面的工作流程不兼容）
8. 执行 `5.merge.py`，用 mkvmerge 将多段 MKV 视频合并为一个单一的 MKV 视频，添加章节信息
9. 执行 `6.chapter.py`，用 MKVToolNix 里的 mkvextract 和 mkvpropredict 导出、读取并修改原视频章节和版本信息

