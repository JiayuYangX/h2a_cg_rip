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
lang = {
    "en": 3,
    "cht": 11,
    "fr": 14,
    "de": 17,
    "it": 20,
    "jpn": 23,
    "kor": 26,
    "sp": 29
}

input_dir = 'E:\\SteamLibrary\\steamapps\\common\\Halo The Master Chief Collection\\halo2\\prebuild\\video'
output_dir = 'F:\\Videos\\h2a_cg'
bitrate = "256k"

cmd = [
    'chcp 65001',
    f'cd /d "{input_dir}"'
]

for i in ep:
    for l, idx in lang.items():
        cmd.append(f'ffmpeg -i "{i}.bk2"'
            + ' -filter_complex "'
            + f'[0:{idx-2}][0:{idx-1}][0:{idx}]amerge=inputs=3[a_3ch];'
            +  '[a_3ch]pan=stereo|FL=c0+c2|FR=c1+c2[a_out]"'
            + f' -map "[a_out]" -c:a aac -b:a {bitrate}'
            + f' -y "{output_dir}\\{i}.{l}.m4a"')

f = open('aud.bat', 'w', encoding='utf-8')
for line in cmd:
    f.write(line + '\n')
f.close()

# subprocess.run('aud.bat')