import os
import shutil

def r_cp_tree(nodepath, targetpath):
    if not os.path.exists(nodepath):
        raise Exception("Not a valid path")
    content = os.listdir(nodepath)
    if len(content) == 0:
        return None
    for node in content:
        npath = os.path.join(nodepath, node)
        print("current path is: ", npath)
        if not os.path.isfile(npath):
            newTargetDir = os.path.join(targetpath, node)
            print("targetDir is: ", newTargetDir)
            if not os.path.exists(newTargetDir):
                os.mkdir(newTargetDir)
                print("creating new dir: ", newTargetDir)
            print("recursing to npath=", npath, " and newTargetDir=", newTargetDir)
            r_cp_tree(npath, newTargetDir)
        else:
            shutil.copy(npath, targetpath)
            print("file: ", npath, " copied to targetPath: ", targetpath)
    return None

def copy_files_recursive(to_copy, target):
    shutil.rmtree(target)
    os.mkdir(target)
    r_cp_tree(to_copy,target)