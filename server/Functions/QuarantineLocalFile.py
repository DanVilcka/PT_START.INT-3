import shutil


def QuarantineLocalFile(path, file):
    try:
        shutil.move(path, file)
        return True
    except:
        return False
