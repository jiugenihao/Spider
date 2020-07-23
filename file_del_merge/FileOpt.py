"""
文件操作模块
1.查询目录下符合条件的文件列表
2.
"""
import os
import os.path

def ListFileByExt(path, ext):
    """
    查找path目录下扩展名为ext的文件列表
    path: string 查找的目录
    ext : string 匹配的扩展名 eg:".proto"
    return value: 返回找到的所有文件名列表,不带路径
    """
    allFiles = os.listdir(path)
    retFiles = []
    for file in allFiles:
        if os.path.splitext(file)[1] == ext:
            retFiles.append(file)
            pass
        pass

    return retFiles

def ListFileByWord(path, word):
    """
    查询path目录下文件名中包含word关键字的的文件列表
    path: string 目录路径
    word: string 匹配关键字  比如Card，Guild
    """
    all_file = os.listdir(path)
    match_list = [] # 全路径
    name_list = []  # 文件名
    for file in all_file:
        name = os.path.splitext(file)[0]
        #ext  = os.path.splitext(file)[1]
        if word in name:
            #print(name)
            match_list.append(os.path.join(path, file))
            name_list.append(name)
            pass
        pass
    
    return match_list,name_list

