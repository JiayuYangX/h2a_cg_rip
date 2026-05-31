import os
import subprocess

ep = [
    'Ep001_OneSizeFitsAll',
    'Ep_002_Home_Field_Advantage',
    'Ep_003_Return_to_Sender',
    'Ep_004_Theyll_Regret_That_Too',
    'Ep_005_Ladies_Like_Armor_Plating_Easy',
    'Ep_005_Ladies_Like_Armor_Plating_Normal',
    'Ep_005_Ladies_Like_Armor_Plating_Heroic',
    'Ep_005_Ladies_Like_Armor_Plating_Legendary',
    'Ep_006_Field_Experiment',
    'Ep_007_A_Whisper_in_the_Storm',
    'Ep_008_Juggernaut',
    'Ep_009_Hey_Watch_This',
    'Ep_010_Hot_Pursuit',
    'Ep_011_Dead_or_Alive',
    'Ep_012_The_Oracle',
    'Ep_013_Edification',
    'Ep_014_Helljumpers_Easy',
    'Ep_014_Helljumpers_Normal',
    'Ep_014_Helljumpers_Heroic',
    'Ep_014_Helljumpers_Legendary',
    'Ep_015_Testament',
    'Ep_016_One_Way_Ticket',
    'Ep_017_Sorry_Were_You_in_the_Middle',
    'Ep_018_Uncomfortable_Silence',
    'Ep_019_Objects_in_the_Mirror',
    'Ep020_ShootingGallery',
    'Ep_021_Familiar_Feeling',
    'Ep_022_Inside_Job',
    'Ep_022_Inside_Job_Legendary',
    'Ep_023_Hopes_and_Dreams_of_the_Cov',
    'Ep_024_So_Thats_How_It_Is',
    'Ep_025_Fight_Club',
    'Ep_026_Cross_Purposes',
    'Ep_027_Once_Again_With_Feeling',
    'Ep_028_Your_Ass_My_Hoof',
    'Ep_029_Backseat_Driver',
    'Ep_030_Delusions_of_Grandeur',
    'Ep_031_Finale',
    'Ep_032_Post_Credits_Teaser',
    'Ep_033_Day_at_the_Beach',
    'Ep_034_Bookend_Intro',
    'Ep_035_Bookend_Outro'
]
lang_aud = {
    'en': ['eng', 'English'],
    'cht': ['chi', '中文（台灣）'],
    'fr': ['fre', 'Français'],
    'de': ['ger', 'Deutsch'],
    'it': ['ita', 'Italiano'],
    'jpn': ['jpn', '日本語'],
    'kor': ['kor', '한국어'],
    'sp': ['spa', 'Español']
}
lang_sub = {
    'en': ['eng', 'English'],
    'chs': ['chi', '简体中文'],
    'zh': ['chi', '繁體中文'],
    'fr': ['fre', 'Français'],
    'de': ['ger', 'Deutsch'],
    'it': ['ita', 'Italiano'],
    'ja': ['jpn', '日本語'],
    'ko': ['kor', '한국어'],
    'es': ['spa', 'Español (México)'],
    'es_es': ['spa', 'Español (España)'],
    'pt_br': ['por', 'Português']
}

dir = 'F:\\Videos\\h2a_cg'
# sub_dir = 'E:\\SteamLibrary\\steamapps\\common\\Halo The Master Chief Collection\\halo2\\prebuild\\subtitles'
sub_dir = 'F:\\Videos\\h2a_cg\\subtitles'
offset = -2

cmd = [
    'chcp 65001',
    f'cd /d "{dir}"'
]

for i in ep:
    cmd.append(f'ffmpeg -i "{i}.mp4"')
    for l in lang_aud:
        cmd[-1] += f' -i "{i}.{l}.m4a"'
    if i == 'Ep_033_Day_at_the_Beach':
        i = 'Ep033_Day_at_the_Beach'
    not_blank = os.path.exists(f'{sub_dir}\\en\\{i}.srt')
    for l in lang_sub:
        cmd[-1] += f' -itsoffset {offset}'
        if not_blank:
            cmd[-1] += f' -i "{sub_dir}\\{l}\\{i}.srt"'
        else:
            cmd[-1] += ' -i "blank.srt"'
    cmd[-1] += ' -map 0:v'
    for j in range(len(lang_aud)):
        cmd[-1] += f' -map {j + 1}:a'
    for j in range(len(lang_sub)):
        cmd[-1] += f' -map {j + 1 + len(lang_aud)}:s'
    id = 0
    for l in lang_aud:
        cmd[-1] += f' -metadata:s:a:{id} language={lang_aud[l][0]}'
        cmd[-1] += f' -metadata:s:a:{id} title="{lang_aud[l][1]}"'
        id += 1
    id = 0
    for l in lang_sub:
        cmd[-1] += f' -metadata:s:s:{id} language={lang_sub[l][0]}'
        cmd[-1] += f' -metadata:s:s:{id} title="{lang_sub[l][1]}"'
        id += 1
    cmd[-1] += f' -c copy -movflags +faststart -y "{i}.mkv"'

f = open('mix1.bat', 'w', encoding='utf-8')
for c in cmd:
    f.write(c + '\n')
f.close()

# subprocess.run('mix1.bat')