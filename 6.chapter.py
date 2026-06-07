import configparser
import os
import xml.etree.ElementTree as ET
import subprocess

config = configparser.ConfigParser()
config.read(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'config.ini'))


chapters = [
    ['01. One Size Fits All - The Heretic', '01. One Size Fits All'],
    ['02. Home Field Advantage - Cario Station', '02. Home Field Advantage'],
    ['03. Return to Sender - Cario Station', '03. Return to Sender'],
    ['04. They\'ll Regret That Too - Outskirts', '04. They\'ll Regret That Too'],
    ['05. Ladies Like Armor Plating - Metropolis', '05. Ladies Like Armor Plating (Easy)'],
    ['05. Ladies Like Armor Plating - Metropolis', '05. Ladies Like Armor Plating (Normal)'],
    ['05. Ladies Like Armor Plating - Metropolis', '05. Ladies Like Armor Plating (Heroic)'],
    ['05. Ladies Like Armor Plating - Metropolis', '05. Ladies Like Armor Plating (Legendary)'],
    ['06. Field Experiment - Metropolis', '06. Field Experiment'],
    ['07. A Whisper in the Storm - The Arbiter', '07. A Whisper in the Storm'],
    ['08. Juggernaut - The Oracle', '08. Juggernaut'],
    ['09. Hey Watch This - The Oracle', '09. Hey Watch This'],
    ['10. Hot Pursuit - The Oracle', '10. Hot Pursuit'],
    ['11. Dead or Alive - The Oracle', '11. Dead or Alive'],
    ['12. The Oracle - The Oracle', '12. The Oracle'],
    ['13. Edification - The Oracle', '13. Edification'],
    ['14. Helljumpers - Deta Halo', '14. Helljumpers (Easy)'],
    ['14. Helljumpers - Deta Halo', '14. Helljumpers (Normal)'],
    ['14. Helljumpers - Deta Halo', '14. Helljumpers (Heroic)'],
    ['14. Helljumpers - Deta Halo', '14. Helljumpers (Legendary)'],
    ['15. Testament - Regret', '15. Testament'],
    ['16. One Way Ticket - Regret', '16. One Way Ticket'],
    ['17. Sorry Were You in the Middle - Regret', '17. Sorry Were You in the Middle'],
    ['18. Uncomfortable Silence - Sacred Icon', '18. Uncomfortable Silence'],
    ['19. Objects in the Mirror - Quarantine Zone', '19. Objects in the Mirror'],
    ['20. Shooting Gallery - Quarantine Zone', '20. Shooting Gallery'],
    ['21. Familiar Feeling - Quarantine Zone', '21. Familiar Feeling'],
    ['22. Inside Job - Gravemind', '22. Inside Job'],
    ['22. Inside Job - Gravemind', '22. Inside Job (Legendary)'],
    ['23. Hopes and Dreams of the Cov - Gravemind', '23. Hopes and Dreams of the Cov'],
    ['24. So That\'s How It Is - Uprising', '24. So That\'s How It Is'],
    ['25. Fight Club - Uprising', '25. Fight Club'],
    ['26. Cross Purposes - High Charity', '26. Cross Purposes'],
    ['27. Once Again with Feeling - High Charity', '27. Once Again with Feeling'],
    ['28. Your Ass My Hoof - Great Journey', '28. Your Ass My Hoof'],
    ['29. Backseat Driver - Great Journey', '29. Backseat Driver'],
    ['30. Delusions of Grandeur - Great Journey', '30. Delusions of Grandeur'],
    ['31. Finale - Great Journey', '31. Finale'],
    ['32. Post Credits Teaser', '32. Post Credits Teaser'],
    ['Day at the Beach', '33. Day at the Beach'],
    ['Halo 5 Bookend Intro', '34. Bookend Intro'],
    ['Halo 5 Bookend Outro', '35. Bookend Outro']
]

diff = [[0, 0, 0, 0]] * 36
pre = [0] * 36
diff[5] = [0, 1, 2, 3]
for i in range(6, 36):
    pre[i] += 3
diff[14] = [0, 1, 2, 3]
for i in range(15, 36):
    pre[i] += 3
diff[22] = [0, 0, 0, 1]
for i in range(23, 36):
    pre[i] += 1

start = []
end = []

def parse_ts(ts: str) -> float:
    h, m, rest = ts.split(':')
    sec, nsec = rest.split('.')
    return int(h) * 3600 + int(m) * 60 + int(sec) + int(nsec) / 10 ** len(nsec)

def format_ts(seconds: float) -> str:
    h = int(seconds // 3600)
    m = int((seconds % 3600) // 60)
    s = int(seconds % 60)
    ns = round((seconds - int(seconds)) * 1_000_000_000)
    return f'{h:02d}:{m:02d}:{s:02d}.{ns:09d}'

def parse_time(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()
    edition = root.find('.//EditionEntry')
    for chap in edition.findall('ChapterAtom'):
        start.append(chap.find('ChapterTimeStart').text)
        if chap.find('.//ChapterString').text == 'Ep_034_Bookend_Intro':
            start[-1] = format_ts(parse_ts(start[-1]) - 0.001)
        if len(start) > 1:
            end.append(start[-1])
    end.append(total_duration)

def generate_edition(index, title, sign, default=False):
    edition = ET.Element('EditionEntry')
    if default:
        ET.SubElement(edition, 'EditionFlagDefault').text = '1'
    ET.SubElement(edition, 'EditionFlagOrdered').text = '1'
    disp = ET.SubElement(edition, 'EditionDisplay')
    ET.SubElement(disp, 'EditionString').text = title
    ET.SubElement(disp, 'EditionLanguageIETF').text = 'en'
    if sign != 0:
        for i, id in enumerate(index):
            index[i] += pre[id] + diff[id][sign - 1] - 1
    for i in index:
        chap = ET.SubElement(edition, 'ChapterAtom')
        ET.SubElement(chap, 'ChapterTimeStart').text = start[i]
        ET.SubElement(chap, 'ChapterTimeEnd').text = end[i]
        disp = ET.SubElement(chap, 'ChapterDisplay')
        ET.SubElement(disp, 'ChapterString').text = chapters[i][sign == 0]
        ET.SubElement(disp, 'ChapLanguageIETF').text = 'en'
    return edition

input_dir = config['paths']['export_dir']
work_dir = os.path.dirname(os.path.abspath(__file__))
file_name = config['paths']['export_name'] + '.mkv'
input_xml = "chapters.xml"
output_xml = "chapters_multiedit.xml"

subprocess.run(['mkvextract', f'{input_dir}\\{file_name}', 'chapters', f'{work_dir}\\{input_xml}'])

total_duration = format_ts(parse_ts(subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration',
                                       '-of', 'default=noprint_wrappers=1:nokey=1', '-sexagesimal', f'{input_dir}\\{file_name}'],
    capture_output=True, text=True
).stdout.strip()))

parse_time(input_xml)
editions = [
    {
        'title': 'Easy',
        'index': list(range(1, 33)),
        'sign': 1,
        'default': False
    },{
        'title': 'Normal',
        'index': list(range(1, 33)),
        'sign': 2,
        'default': True
    },{
        'title': 'Heroic',
        'index': list(range(1, 33)),
        'sign': 3,
        'default': False
    },{
        'title': 'Legendary',
        'index': list(range(1, 33)),
        'sign': 4,
        'default': False
    },{
        'title': 'Easy (with Halo 5 Bookends)',
        'index': [34] + list(range(1, 32)) + [35],
        'sign': 1,
        'default': False
    },{
        'title': 'Normal (with Halo 5 Bookends)',
        'index': [34] + list(range(1, 32)) + [35],
        'sign': 2,
        'default': False
    },{
        'title': 'Heroic (with Halo 5 Bookends)',
        'index': [34] + list(range(1, 32)) + [35],
        'sign': 3,
        'default': False
    },{
        'title': 'Legendary (with Halo 5 Bookends)',
        'index': [34] + list(range(1, 32)) + [35],
        'sign': 4,
        'default': False
    },{
        'title': 'Day at the Beach',
        'index': [33],
        'sign': 2,
        'default': False
    },{
        'title': 'Full Episodes',
        'index': list(range(42)),
        'sign': 0,
        'default': False
    }
]

root = ET.Element('Chapters')
for e in editions:
    index = e['index']
    title = e['title']
    sign = e['sign']
    default = e['default']
    ed = generate_edition(index, title, sign, default)
    root.append(ed)

tree = ET.ElementTree(root)
ET.indent(tree, space='  ')
tree.write(output_xml, encoding='utf-8', xml_declaration=True)

subprocess.run(['mkvpropedit', f'{input_dir}\\{file_name}', '--chapters', f'{work_dir}\\{output_xml}'])
