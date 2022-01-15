def add_time(start, duration, day = None):
    ampm = {
        'AM': 1,
        'PM': 2
    }
    #pulling data
    pos = start.index(':')
    hstart = int(start[:pos])
    mstart = int(start[pos+1:start.index(' ')])
    ampmstart = (start[start.index(' ')+1:])
    pos = duration.index(':')
    hduration = int(duration[:pos])
    mduration = int(duration[pos+1:])
    #Calculations
    hend = hstart + hduration
    mend = mstart + mduration
    mremaing = mend % 60
    madd = mend // 60
    hend = hend + madd
    hremaing = hend % 12
    hadd = hend // 12
    days = hadd // 24
    #AMPM Calculation
    if ampmstart in ampm:
        ampmint = ampm.get(ampmstart)
    if hadd % 2 == 0:
        ampmint += 0
    elif ampmint == 2:
        ampmint -= 1
    else:
        ampmint += 1
    for key, value in ampm.items():
        if ampmint == value:
            ampmend = key
    #Putting a 0 infront of a single digit
    if len(str(mremaing)) == 1:
        mremaing = '0' + str(mremaing)
    #making a 0 go to a 12 for the hour
    if hremaing == 0:
        hremaing = 12
    #Deciding on a print statement depending on how many days have passed
    if days <= 0:
        newtime = (str(hremaing) + ':' + str(mremaing) + ' ' + ampmend)
    elif days == 1:
        newtime = (str(hremaing) + ':' + str(mremaing) + ' ' + ampmend + ' (' + str(days) + ' days later)')
    else:
        newtime = (str(hremaing) + ':' + str(mremaing) + ' ' + ampmend + ' (next day)')

    # use MOD 60 for Mins and MOD 12 for hours 10 % 3 = 1
    # use Floor division for the amount of hours or mins needed to pass 10 // 3 = 3
    new_time = (newtime)

    return new_time