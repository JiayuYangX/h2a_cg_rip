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

input_dir = config['paths']['intermediate_dir']
output_dir = config['paths']['export_dir']
output = config['paths']['export_name']

cmd = [
    'chcp 65001',
    f'cd /d "{input_dir}"'
]

cmd.append(f'mkvmerge -o "{output_dir}\\{output}.mkv" ^\n'
    + '  --generate-chapters when-appending ^\n'
    + '  --generate-chapters-name-template "<FILE_NAME>"')
cmd[-1] += f' ^\n  "{ep[0]}.mkv"'
for i in ep[1:]:
    cmd[-1] += f' ^\n  +"{i}.mkv"'

f = open('merge.bat', 'w', encoding='utf-8')
for line in cmd:
    f.write(line + '\n')
f.close()

subprocess.run('merge.bat')