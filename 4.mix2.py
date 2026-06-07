import configparser
import os
import subprocess

config = configparser.ConfigParser()
config.read(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'config.ini'))

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
    'en': ['en', 'English'],
    'cht': ['zh', '中文（台灣）'],
    'fr': ['fr', 'Français'],
    'de': ['de', 'Deutsch'],
    'it': ['it', 'Italiano'],
    'jpn': ['ja', '日本語'],
    'kor': ['ko', '한국어'],
    'sp': ['es', 'Español']
}
lang_sub = {
    'en': ['en', 'English'],
    'chs': ['zh-Hans', '简体中文'],
    'zh': ['zh-Hant', '繁體中文'],
    'fr': ['fr', 'Français'],
    'de': ['de', 'Deutsch'],
    'it': ['it', 'Italiano'],
    'ja': ['ja', '日本語'],
    'ko': ['ko', '한국어'],
    'es': ['es-MX', 'Español (México)'],
    'es_es': ['es-ES', 'Español (España)'],
    'pt_br': ['pt', 'Português']
}

dir = config['paths']['intermediate_dir'] + '\\'
sub_dir = config.get('paths', 'subtitle_dir',
    fallback=config['paths']['game_dir'] + '\\subtitles')
fix_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'sub_fix')

blank_list = [
    'Ep_010_Hot_Pursuit',
    'Ep_011_Dead_or_Alive',
    'Ep_024_So_Thats_How_It_Is'
]

cmd = [
    'chcp 65001',
    f'cd /d "{dir}"'
]

for i in ep:
    cmd.append(f'mkvmerge -o "{i}.mkv" "{i}.mp4"')
    for l in lang_aud:
        cmd[-1] += f' --language 0:{lang_aud[l][0]} --track-name 0:"{lang_aud[l][1]}" "{i}.{l}.m4a"'
    not_blank = os.path.exists(f'{sub_dir}\\en\\{i}.srt')
    for l in lang_sub:
        path = f'{fix_dir}\\replacement\\{l}\\{i}.srt'
        if not os.path.exists(path):
            if i in blank_list:
                path = f'{fix_dir}\\blank.srt'
            else:
                path = f'{sub_dir}\\{l}\\{i}.srt'
                cmd[-1] += ' --sync 0:-2000'
        cmd[-1] += f' --language 0:{lang_sub[l][0]} --track-name 0:"{lang_sub[l][1]}" "{path}"'

f = open('mix2.bat', 'w', encoding='utf-8')
for line in cmd:
    f.write(line + '\n')
f.close()

subprocess.run('mix2.bat')