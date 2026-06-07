# 《光环2：周年版》全CG导出

本仓库存储的是个人用于《光环2：周年版》CG 导出的相关脚本。

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
9. 执行 `6.chapter.py`，用 MKVToolNix 里的 mkvextract 和 mkvpropredict 导出、读取并修改原视频的章节和版本信息

