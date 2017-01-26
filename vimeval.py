import vim


def sum_range():
    buf = vim.current.buffer
    (lnum1, col1) = buf.mark('<')
    (lnum2, col2) = buf.mark('>')
    lines = vim.eval('getline({}, {})'.format(lnum1, lnum2))
    mode = vim.eval('visualmode()')
    print("mode: %s" % mode)
    print(col1, "", col2)
    ret = []
    for line in lines:
        if mode != "v":
            print("strip")
            tmp = line[col1:col2 + 1]
        else:
            tmp = line.strip()
        ret.append(tmp)
    _sum = []
    for val in ret:
        try:
            fval = float(val)
            _sum.append(fval)
        except:
            print("Unable to convert %s" % val)
    return sum(_sum)
