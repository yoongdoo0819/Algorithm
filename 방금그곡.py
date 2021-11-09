import datetime

def solution(m, musicinfos):
    answer = []
    minutes, max = 0, 0
    m = m.replace('C#', 'c')
    m = m.replace('D#', 'd')
    m = m.replace('F#', 'f')
    m = m.replace('G#', 'g')
    m = m.replace('A#', 'a')
    
    for musicinfo in musicinfos:
        splitMusicInfo = musicinfo.split(',')
        
        timeInfo1 = datetime.datetime.strptime(splitMusicInfo[0], '%H:%M')
        timeInfo2 = datetime.datetime.strptime(splitMusicInfo[1], '%H:%M')
        diff = timeInfo2-timeInfo1
        
        HM = str(diff).split(':')
        if HM[0] != 0:
            minutes += int(HM[0]) * 60
        
        minutes += int(str(HM[1]))
        
        splitMusicInfo[3] = splitMusicInfo[3].replace('C#', 'c')
        splitMusicInfo[3] = splitMusicInfo[3].replace('D#', 'd')
        splitMusicInfo[3] = splitMusicInfo[3].replace('F#', 'f')
        splitMusicInfo[3] = splitMusicInfo[3].replace('G#', 'g')
        splitMusicInfo[3] = splitMusicInfo[3].replace('A#', 'a')
        
        a = minutes//len(splitMusicInfo[3])
        b = minutes%len(splitMusicInfo[3])
        splitMusicInfo[3] = splitMusicInfo[3] * a + splitMusicInfo[3][0:b]
        
        if m in splitMusicInfo[3]:
            answer.append([minutes, splitMusicInfo[2]])
            if max < minutes:
                max = minutes
        
        minutes = 0
    
    result = []
    if len(answer) >= 2:
        for musicinfo in answer:
            if musicinfo[0] >= max:
                result.append(musicinfo)
    elif len(answer) == 1:
        return answer[0][1]
    elif len(answer) == 0:
        return "(None)"
    
    return result[0][1]
   