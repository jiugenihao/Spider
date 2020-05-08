import os
import shutil

def FindProtosByStr(path, word):
    """
    通过关键字word查询path目录下带有关键字的文件列表
    path:  目录路径
    word:  匹配关键字  比如Card，Guild
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

def RemoveFiles(file_list):
    """
    删除文件列表中的文件
    file_list:  文件列表
    """
    for file in file_list:
        os.remove(file)
        pass
    pass


def RemoveLineByWord(file, word, count):
    """
    删除带有某个字符串的行
    :param file: 文件路径
    :param word: 包含这个字符串的行
    :param count: 删除的行数
    :return: None
    """
    lines = []
    with open(file, "r", encoding="utf-8") as f1:
        lines = f1.readlines()

    cnt = 0
    with open(file, "w", encoding="utf-8") as f2:
        for line in lines:
            if word in line:
                cnt = count
                continue
            if cnt != 0:
                cnt -= 1
                continue
            f2.write(line)
            pass
        pass
    pass

def PrintList(list):
    for item in list:
        print(item)
        
# 将文件中符合条件的行复制到一个新的列表中
def GetFileLines(file_name, line_list):
    """
    获取文件所有行数据，保存到行列表
    file_name:  文件名
    line_list:  行列表
    """
    file = open(file_name, 'r', encoding='utf-8')
    #is_copy = False
    
    head_1 = "syntax"
    head_2 = "import "
    for line in file.readlines():
        if not line.isspace() and head_1 not in line and head_2 not in line:
            if '\n' not in line:
                line = line + '\n'
            line_list.append(line)
            pass
        #if line[0:7] == "message":
        #    is_copy = True
        #    pass
        #if not line.isspace() and is_copy:
        #    if '\n' not in line:
        #        line = line + '\n'
        #    line_list.append(line)
        #    pass
        #pass
    file.close()
    pass

def CreateNewProto(path, file_name, protos):
    """
    生成一个新proto文件，存所有的行数据
    path     :  文件路径
    file_name:  文件名
    protos   :  proto文件列表
    """
    all_line = []
    for proto in protos:
        GetFileLines(proto, all_line)
        pass
    #print(all_line)
    
    # 文件头
    file_start = """
syntax = "proto2";
import "ReturnValue.proto";
import "MDefines.proto";
import "Constant.proto";

"""
    with open(os.path.join(path, file_name), "w+", encoding="utf-8") as file:
        file.write(file_start)
        file.writelines(all_line)
        pass
    pass

if __name__ == "__main__":
    proto_path  = "C:/DragonGirls/DragonGirlsServer/trunk/DragonGirlServer/Game/ProtoMessage/"
    event_path  = "C:/DragonGirls/DragonGirlsServer/trunk/DragonGirlServer/Game/Event/"
    deal_path   = "C:/DragonGirls/DragonGirlsServer/trunk/DragonGirlServer/Game/game/auto/"
    
    # Event 工程目录
    event_proj_path  = "C:/DragonGirls/DragonGirlsServer/trunk/DragonGirlServer/Event/"
    e_proj_name      = "Event.vcxproj"
    e_filter_name    = "Event.vcxproj.filters"
    abs_e_proj       = os.path.join(event_proj_path, e_proj_name)
    abs_e_filter     = os.path.join(event_proj_path, e_filter_name)
    #print(abs_e_proj)
    #print(abs_e_filter)
    # Game 工程目录
    #game_path        = "C:/DragonGirls/DragonGirlsServer/trunk/DragonGirlServer/Game/"
    #g_proj_name      = "Game.vcxproj"
    #g_filter_name    = "Game.vcxproj.filters"
    #abs_g_proj       = os.path.join(game_path, g_proj_name)
    #abs_g_filter     = os.path.join(game_path, g_filter_name)
    #print(abs_g_proj)
    #print(abs_g_filter)
    
    #####################################################################################
    keys    = ["Arena", "Entrust", "KingTower", "Maze", "Recruit", "RankList", "WorldBoss"]
    pre = "Mse"
    
    new_name = "Activity.proto"
    new_file = pre + new_name
    # 1.获取包含关键字的所有文件
    proto_dirs  = []
    proto_names = []
    pb_dirs     = []
    
    for key in keys:
        key = pre + key
        dirs, names = FindProtosByStr(proto_path, key)
        proto_dirs  += dirs
        proto_names += names
        dirs, _ = FindProtosByStr(event_path, key)
        pb_dirs += dirs
        pass
        
    PrintList(proto_dirs)
    PrintList(proto_names)
    PrintList(pb_dirs)
    
    # 2.将这些文件内容合并到同一个文件中
    CreateNewProto(proto_path, new_file, proto_dirs)
    
    # 2.删除proto pb deal文件
    RemoveFiles(proto_dirs)
    RemoveFiles(pb_dirs)
    
    # 3.删除工程文件中的引用
    for name in proto_names:
        RemoveLineByWord(abs_e_proj, name, 0)
        RemoveLineByWord(abs_e_filter, name, 2)
        pass
    pass

    # 4.执行生成event工具 proto文件转换工具