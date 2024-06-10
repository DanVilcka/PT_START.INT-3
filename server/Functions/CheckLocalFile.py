
def CheckLocalFile(file_path, sinature):
    arr = []
    with open(file_path) as fp:
        for l_no, line in enumerate(fp):
            if sinature in line:
                arr.append([l_no + 1, line.index(sinature)])

    if len(arr) == 0:
        return "No signature in file"
    else:
        return arr