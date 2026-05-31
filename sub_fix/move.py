import shutil
import os

ep = [
    'Ep_031_Finale',
    'Ep_033_Day_at_the_Beach',
    'Ep_034_Bookend_Intro',
    'Ep_035_Bookend_Outro'
]

lang = ['en', 'chs', 'zh', 'fr', 'de', 'it', 'ja', 'ko', 'es', 'es_es', 'pt_br']

dir = 'D:\\JiaYu\\Desktop\\h2a_cg_rip\\sub_fix'

for i in ep:
    for l in lang:
        src = f'{dir}\\{i}\\{i}.{l}.srt'
        if not os.path.exists(src):
            continue
        dst = f'{dir}\\replacement\\{l}\\{i}.srt'
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        shutil.copyfile(src, dst)