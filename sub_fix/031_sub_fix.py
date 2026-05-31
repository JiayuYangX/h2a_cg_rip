import pysrt

input_dir = 'E:\\SteamLibrary\\steamapps\\common\\Halo The Master Chief Collection\\halo2\\prebuild\\subtitles'
output_dir = 'D:\\JiaYu\\Desktop\\h2a_cg_rip\\sub_fix'
title = 'Ep_031_Finale'

lang = ['en', 'chs', 'zh', 'fr', 'de', 'it', 'ja', 'ko', 'es', 'es_es', 'pt_br']

for l in lang:
    subs = pysrt.open(f'{input_dir}\\{l}\\{title}.srt')

    for sub in subs[:14]:
        sub.shift(seconds=-2)

    for sub in subs[14:]:
        sub.shift(seconds=-3.2)

    subs.clean_indexes()

    subs.save(f'{output_dir}\\{title}\\{title}.{l}.srt', encoding='utf-16')