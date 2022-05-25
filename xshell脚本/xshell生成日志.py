import os


def getFiles(path):
    for root, dirs, files in os.walk(file_dir):
        print("root_dir:", root)
        print("sub_dirs:", dirs)
        print("files:", files)
    return files


if __name__ == '__main__':
    file_dir = "C:\\Users\\cai\\Documents\\NetSarang Computer\\7\\Xshell\\Sessions"
    getFiles(file_dir)
