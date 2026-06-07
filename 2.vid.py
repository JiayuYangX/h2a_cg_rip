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

dir = config['paths']['intermediate_dir']
crop = '1920:816:0:132'
h264_metadata = [
    'video_full_range_flag=0',
    'colour_primaries=1',
    'matrix_coefficients=1',
    'transfer_characteristics=1'
]
g = 30
keyint_min = 15
sc_threshold = 0
crf = 18
preset = "veryslow"
pix_fmt = "yuv420p"

cmd = [
    'chcp 65001',
    f'cd /d "{dir}"'
]

for i in ep:
    cmd.append(f'ffmpeg -i "{i}.avi"'
        + f' -vf crop="{crop}'
        # + (',lutyuv=y=\'clip((val-16)*(255/219),0,255)\'"' if i == ep[-1] else '"')
        + (',scale=in_range=limited:out_range=full,setparams=range=limited"' if i == ep[-1] or i == ep[-4] else '"')
        + f' -pix_fmt {pix_fmt}'
        # + f' -bsf:v h264_metadata={':'.join(h264_metadata)}'
        + f' -c:v libx264 -crf {crf} -preset {preset}'
        + f' -g {g} -keyint_min {keyint_min} -sc_threshold {sc_threshold}'
        +  ' -movflags +faststart'
        + f' -y "{i}.mp4"')

f = open('vid.bat', 'w', encoding='utf-8')
for line in cmd:
    f.write(line + '\n')
f.close()

subprocess.run('vid.bat')