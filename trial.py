import requests
name = 'https://tgftp.nws.noaa.gov/data/observations/metar/decoded/KSGS.TXT'
res = requests.get(name)
s = str(res.content)
s = s.split('\\n')
print(len(s))
s[0] = s[0].replace('b','')
s[0] = s[0].replace('"','')
s.remove(s[-1])
for i in range(len(s)):
	s[i] = s[i].replace("'",'')
print(s)






params['station'] = cleanedList[2]
        params['last_observed_on'] = cleanedList[0]+' at '+cleanedList[1]+' GMT'
        temp = ''
        print(cleanedList[8])
        t = cleanedList[9].split('/')
        current,dew = t[0],t[1]
        print(current,dew)
        if(current[0] == 'M'):
            temp = 'Current : -'+current[1:]+' C/ '
            c = int('-'+current[1:])
            f = (c * (9 / 5))+32
            temp += str(f)+' F and '
        else:
            temp = 'Current : '+current+' C/ '
            c = int(current)
            f = (c * (9 / 5))+32
            temp += str(f)+' F and '
        d = ''
        if(dew[0] == 'M'):
            d = 'Dew : -'+dew[1:]+' C/ '
            c = int('-'+dew[1:])
            f = (c * (9 / 5))+32
            d += str(f)+' F'
        else:
            d = 'Dew :'+dew+' C/ '
            c = int(dew)
            f = (c * (9 / 5))+32
            d += str(f)+' F'
        temp += d
        print(temp)
        params['temperature_recorded'] = temp
        if(cleanedList[3][:-1] == 'Z'):datetimeformat = 'Zulu'
        else:datetimeformat = 'Other'
        params['date_and_time_format'] = datetimeformat
        if(cleanedList[4] == 'AUTO'):params['Reporting Status'] = 'AUTO'
        else:params['Reporting Status'] = 'MANUAL'
        wind = cleanedList[5]
        direction = int(wind[:3])
        gusting = ''
        velocity = ''
        if(wind[5] == 'G'):
            gusting = wind[3:5]+' gusting with '
            vel = (wind[6:8])
        else:
            vel = (wind[3:5])
        velocity = vel+' i.e '+str((int(vel)*1.151))+' mph'
        if(direction < 90 or direction == 360):direction = 'North '
        elif(direction < 180 and direction >= 90):direction = 'East'
        elif(direction < 270 and direction >= 180):direction = 'South'
        else:direction = 'West'
        params['direction_and_velocity'] = direction+' '+gusting+' '+velocity
        params['visibility'] = cleanedList[6]+' (Statute Miles)'
        params['aerial_status'] = cleanedList[7]
        atm = cleanedList[9]
        params['atmospheric_pressure'] = atm[1:3]+'.'+atm[4:6]+' of Mercury'
        print('----',params)