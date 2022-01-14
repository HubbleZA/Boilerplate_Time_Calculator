def add_time(start, duration, day = None):
    ampm = {
        'AM': 1,
        'PM': 2
    }
    pos = start.index(':')
    #print(start)
    #print(duration)
    hstart = int(start[:pos])
    mstart = int(start[pos+1:start.index(' ')])
    ampmstart = (start[start.index(' ')+1:])
    pos = duration.index(':')
    hduration = int(duration[:pos])
    mduration = int(duration[pos+1:])
    hend = hstart + hduration
    mend = mstart + mduration
    mremaing = mend % 60
    madd = mend // 60
    hend = hend + madd
    hremaing = hend % 12
    hadd = hend // 12
    if ampmstart in ampm:
        ampmint = ampm.get(ampmstart)
    if hadd == 0:
        ampmint = ampmint
    else:
        ampmint = (ampmint+hadd) % 2
    for key, value in ampm.items():
        if ampmint == value:
            ampmend = key
    if len(str(mremaing)) == 1:
        mremaing = '0' + str(mremaing)
    if hremaing == 0:
        hremaing = 12

    newtime = (str(hremaing) + ':' + str(mremaing) + ' ' + ampmend)
    #newtime = "1"

    # use MOD 60 for Mins and MOD 12 for hours 10 % 3 = 1
    # use Floor division for the amount of hours or mins needed to pass 10 // 3 = 3
    new_time = (newtime)

    return new_time