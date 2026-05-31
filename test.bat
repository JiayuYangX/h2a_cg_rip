ffmpeg -i Ep_002_Home_Field_Advantage.bk2
  -filter_complex "[0:1][0:2][0:3]amerge=inputs=3[a_3ch];
                   [a_3ch]pan=stereo|FL=c0+c2|FR=c1+c2[a_out]"
  -map "[a_out]" -c:a aac -b:a 256k
  -y F:\Videos\h2a_cg\Ep_002_Home_Field_Advantage_en1.m4a

ffmpeg -i Ep_002_Home_Field_Advantage.avi
  -c:v libx264 -crf 18 -preset slower
  -movflags +faststart
  -y Ep_002_Home_Field_Advantage.mp4

ffmpeg -i Ep_002_Home_Field_Advantage.mp4
  -i Ep_002_Home_Field_Advantage_en.m4a
  -i Ep_002_Home_Field_Advantage_cht.m4a
  -i Ep_002_Home_Field_Advantage_fr.m4a
  -i Ep_002_Home_Field_Advantage_de.m4a
  -i Ep_002_Home_Field_Advantage_it.m4a
  -i Ep_002_Home_Field_Advantage_jpn.m4a
  -i Ep_002_Home_Field_Advantage_kor.m4a
  -i Ep_002_Home_Field_Advantage_sp.m4a
  -itsoffset -2 -i subtitles\en\Ep_002_Home_Field_Advantage.srt
  -itsoffset -2 -i subtitles\chs\Ep_002_Home_Field_Advantage.srt
  -itsoffset -2 -i subtitles\zh\Ep_002_Home_Field_Advantage.srt
  -itsoffset -2 -i subtitles\fr\Ep_002_Home_Field_Advantage.srt
  -itsoffset -2 -i subtitles\de\Ep_002_Home_Field_Advantage.srt
  -itsoffset -2 -i subtitles\it\Ep_002_Home_Field_Advantage.srt
  -itsoffset -2 -i subtitles\ja\Ep_002_Home_Field_Advantage.srt
  -itsoffset -2 -i subtitles\ko\Ep_002_Home_Field_Advantage.srt
  -itsoffset -2 -i subtitles\es\Ep_002_Home_Field_Advantage.srt
  -itsoffset -2 -i subtitles\es_es\Ep_002_Home_Field_Advantage.srt
  -itsoffset -2 -i subtitles\pt_br\Ep_002_Home_Field_Advantage.srt
  -map 0:v
  -map 1:a -map 2:a -map 3:a -map 4:a -map 5:a -map 6:a -map 7:a -map 8:a
  -map 9:s -map 10:s -map 11:s -map 12:s -map 13:s -map 14:s -map 15:s -map 16:s -map 17:s -map 18:s -map 19:s
  -c copy
  -metadata:s:a:0 language=eng -metadata:s:a:0 title="English"
  -metadata:s:a:1 language=zho -metadata:s:a:1 title="中文（台灣）"
  -metadata:s:a:2 language=fra -metadata:s:a:2 title="Français"
  -metadata:s:a:3 language=deu -metadata:s:a:3 title="Deutsch"
  -metadata:s:a:4 language=ita -metadata:s:a:4 title="Italiano"
  -metadata:s:a:5 language=jpn -metadata:s:a:5 title="日本語"
  -metadata:s:a:6 language=kor -metadata:s:a:6 title="한국어"
  -metadata:s:a:7 language=spa -metadata:s:a:7 title="Español"
  -metadata:s:s:0 language=eng -metadata:s:s:0 title="English"
  -metadata:s:s:1 language=zho -metadata:s:s:1 title="简体中文"
  -metadata:s:s:2 language=zho -metadata:s:s:2 title="繁體中文"
  -metadata:s:s:3 language=fra -metadata:s:s:3 title="Français"
  -metadata:s:s:4 language=deu -metadata:s:s:4 title="Deutsch"
  -metadata:s:s:5 language=ita -metadata:s:s:5 title="Italiano"
  -metadata:s:s:6 language=jpn -metadata:s:s:6 title="日本語"
  -metadata:s:s:7 language=kor -metadata:s:s:7 title="한국어"
  -metadata:s:s:8 language=spa -metadata:s:s:8 title="Español (México)"
  -metadata:s:s:9 language=spa -metadata:s:s:9 title="Español (España)"
  -metadata:s:s:10 language=por -metadata:s:s:10 title="Português"
  -movflags +faststart
  -y Ep_002_Home_Field_Advantage.mkv


ffmpeg -i Ep_002_Home_Field_Advantage.mp4 -i Ep_002_Home_Field_Advantage_en.m4a -i Ep_002_Home_Field_Advantage_cht.m4a -i Ep_002_Home_Field_Advantage_fr.m4a -i Ep_002_Home_Field_Advantage_de.m4a -i Ep_002_Home_Field_Advantage_it.m4a -i Ep_002_Home_Field_Advantage_jpn.m4a -i Ep_002_Home_Field_Advantage_kor.m4a -i Ep_002_Home_Field_Advantage_sp.m4a -itsoffset -2 -i subtitles\en\Ep_002_Home_Field_Advantage.srt -itsoffset -2 -i subtitles\chs\Ep_002_Home_Field_Advantage.srt -itsoffset -2 -i subtitles\zh\Ep_002_Home_Field_Advantage.srt -itsoffset -2 -i subtitles\fr\Ep_002_Home_Field_Advantage.srt -itsoffset -2 -i subtitles\de\Ep_002_Home_Field_Advantage.srt -itsoffset -2 -i subtitles\it\Ep_002_Home_Field_Advantage.srt -itsoffset -2 -i subtitles\ja\Ep_002_Home_Field_Advantage.srt -itsoffset -2 -i subtitles\ko\Ep_002_Home_Field_Advantage.srt -itsoffset -2 -i subtitles\es\Ep_002_Home_Field_Advantage.srt -itsoffset -2 -i subtitles\es_es\Ep_002_Home_Field_Advantage.srt -itsoffset -2 -i subtitles\pt_br\Ep_002_Home_Field_Advantage.srt -map 0:v -map 1:a -map 2:a -map 3:a -map 4:a -map 5:a -map 6:a -map 7:a -map 8:a -map 9:s -map 10:s -map 11:s -map 12:s -map 13:s -map 14:s -map 15:s -map 16:s -map 17:s -map 18:s -map 19:s -c copy -metadata:s:a:0 language=eng -metadata:s:a:0 title="English" -metadata:s:a:1 language=zho -metadata:s:a:1 title="中文（台灣）" -metadata:s:a:2 language=fra -metadata:s:a:2 title="Français" -metadata:s:a:3 language=deu -metadata:s:a:3 title="Deutsch" -metadata:s:a:4 language=ita -metadata:s:a:4 title="Italiano" -metadata:s:a:5 language=jpn -metadata:s:a:5 title="日本語" -metadata:s:a:6 language=kor -metadata:s:a:6 title="한국어" -metadata:s:a:7 language=spa -metadata:s:a:7 title="Español" -metadata:s:s:0 language=eng -metadata:s:s:0 title="English" -metadata:s:s:1 language=zho -metadata:s:s:1 title="简体中文" -metadata:s:s:2 language=zho -metadata:s:s:2 title="繁體中文" -metadata:s:s:3 language=fra -metadata:s:s:3 title="Français" -metadata:s:s:4 language=deu -metadata:s:s:4 title="Deutsch" -metadata:s:s:5 language=ita -metadata:s:s:5 title="Italiano" -metadata:s:s:6 language=jpn -metadata:s:s:6 title="日本語" -metadata:s:s:7 language=kor -metadata:s:s:7 title="한국어" -metadata:s:s:8 language=spa -metadata:s:s:8 title="Español (México)" -metadata:s:s:9 language=spa -metadata:s:s:9 title="Español (España)" -metadata:s:s:10 language=por -metadata:s:s:10 title="Português" -movflags +faststart -y Ep_002_Home_Field_Advantage.mkv

mkvmerge -o Ep_002_Home_Field_Advantage.mkv
  Ep_002_Home_Field_Advantage.mp4
  --language 0:en --track-name 0:"English" Ep_002_Home_Field_Advantage_en.m4a
  --language 0:zh --track-name 0:"中文（台灣）" Ep_002_Home_Field_Advantage_cht.m4a
  --language 0:fr --track-name 0:"Français" Ep_002_Home_Field_Advantage_fr.m4a
  --language 0:de --track-name 0:"Deutsch" Ep_002_Home_Field_Advantage_de.m4a
  --language 0:it --track-name 0:"Italiano" Ep_002_Home_Field_Advantage_it.m4a
  --language 0:ja --track-name 0:"日本語" Ep_002_Home_Field_Advantage_jpn.m4a
  --language 0:ko --track-name 0:"한국어" Ep_002_Home_Field_Advantage_kor.m4a
  --language 0:es --track-name 0:"Español" Ep_002_Home_Field_Advantage_sp.m4a
  --sync 0:-2000 --language 0:en --track-name 0:"English" subtitles\en\Ep_002_Home_Field_Advantage.srt
  --sync 0:-2000 --language 0:zh-Hans --track-name 0:"简体中文" subtitles\chs\Ep_002_Home_Field_Advantage.srt
  --sync 0:-2000 --language 0:zh-Hant --track-name 0:"繁體中文" subtitles\zh\Ep_002_Home_Field_Advantage.srt
  --sync 0:-2000 --language 0:fr --track-name 0:"Français" subtitles\fr\Ep_002_Home_Field_Advantage.srt
  --sync 0:-2000 --language 0:de --track-name 0:"Deutsch" subtitles\de\Ep_002_Home_Field_Advantage.srt
  --sync 0:-2000 --language 0:it --track-name 0:"Italiano" subtitles\it\Ep_002_Home_Field_Advantage.srt
  --sync 0:-2000 --language 0:ja --track-name 0:"日本語" subtitles\ja\Ep_002_Home_Field_Advantage.srt
  --sync 0:-2000 --language 0:ko --track-name 0:"한국어" subtitles\ko\Ep_002_Home_Field_Advantage.srt
  --sync 0:-2000 --language 0:es-MX --track-name 0:"Español (México)" subtitles\es\Ep_002_Home_Field_Advantage.srt
  --sync 0:-2000 --language 0:es-ES --track-name 0:"Español (España)" subtitles\es_es\Ep_002_Home_Field_Advantage.srt
  --sync 0:-2000 --language 0:pt --track-name 0:"Português" subtitles\pt_br\Ep_002_Home_Field_Advantage.srt

mkvmerge -o Ep_002_Home_Field_Advantage.mkv Ep_002_Home_Field_Advantage.mp4 --language 0:en --track-name 0:"English" Ep_002_Home_Field_Advantage_en.m4a --language 0:zh --track-name 0:"中文（台灣）" Ep_002_Home_Field_Advantage_cht.m4a --language 0:fr --track-name 0:"Français" Ep_002_Home_Field_Advantage_fr.m4a --language 0:de --track-name 0:"Deutsch" Ep_002_Home_Field_Advantage_de.m4a --language 0:it --track-name 0:"Italiano" Ep_002_Home_Field_Advantage_it.m4a --language 0:ja --track-name 0:"日本語" Ep_002_Home_Field_Advantage_jpn.m4a --language 0:ko --track-name 0:"한국어" Ep_002_Home_Field_Advantage_kor.m4a --language 0:es --track-name 0:"Español" Ep_002_Home_Field_Advantage_sp.m4a --sync 0:-2000 --language 0:en --track-name 0:"English" subtitles\en\Ep_002_Home_Field_Advantage.srt --sync 0:-2000 --language 0:zh-Hans --track-name 0:"简体中文" subtitles\chs\Ep_002_Home_Field_Advantage.srt --sync 0:-2000 --language 0:zh-Hant --track-name 0:"繁體中文" subtitles\zh\Ep_002_Home_Field_Advantage.srt --sync 0:-2000 --language 0:fr --track-name 0:"Français" subtitles\fr\Ep_002_Home_Field_Advantage.srt --sync 0:-2000 --language 0:de --track-name 0:"Deutsch" subtitles\de\Ep_002_Home_Field_Advantage.srt --sync 0:-2000 --language 0:it --track-name 0:"Italiano" subtitles\it\Ep_002_Home_Field_Advantage.srt --sync 0:-2000 --language 0:ja --track-name 0:"日本語" subtitles\ja\Ep_002_Home_Field_Advantage.srt --sync 0:-2000 --language 0:ko --track-name 0:"한국어" subtitles\ko\Ep_002_Home_Field_Advantage.srt --sync 0:-2000 --language 0:es-MX --track-name 0:"Español (México)" subtitles\es\Ep_002_Home_Field_Advantage.srt --sync 0:-2000 --language 0:es-ES --track-name 0:"Español (España)" subtitles\es_es\Ep_002_Home_Field_Advantage.srt --sync 0:-2000 --language 0:pt --track-name 0:"Português" subtitles\pt_br\Ep_002_Home_Field_Advantage.srt