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
        ext  = os.path.splitext(file)[1]
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
    game_path        = "C:/DragonGirls/DragonGirlsServer/trunk/DragonGirlServer/Game/"
    g_proj_name      = "Game.vcxproj"
    g_filter_name    = "Game.vcxproj.filters"
    abs_g_proj       = os.path.join(game_path, g_proj_name)
    abs_g_filter     = os.path.join(game_path, g_filter_name)
    #print(abs_g_proj)
    #print(abs_g_filter)
    
    
    #####################################################################################
    #keys    = ["CopyUpdate", "JjcReward", "MseManual", "MseUpdateSkill"]
    keys    = ["ElevateCard"]
        
    # 1.获取包含关键字的所有文件
    proto_dirs  = []
    proto_names = []
    pb_dirs     = []
    deal_dirs   = []
    for key in keys:
        dirs, names = FindProtosByStr(proto_path, key)
        proto_dirs  += dirs
        proto_names += names
        dirs, _ = FindProtosByStr(event_path, key)
        pb_dirs += dirs
        dirs, _ = FindProtosByStr(deal_path, key)
        deal_dirs += dirs
        pass
        
    PrintList(proto_dirs)
    PrintList(proto_names)
    PrintList(pb_dirs)
    PrintList(deal_dirs)
    
    # 2.删除proto pb deal文件
    #RemoveFiles(proto_dirs)
    #RemoveFiles(pb_dirs)
    #RemoveFiles(deal_dirs)
    
    # 3.删除工程文件中的引用
    #for name in proto_names:
    #    RemoveLineByWord(abs_e_proj, name, 0)
    #    RemoveLineByWord(abs_e_filter, name, 2)
    #    RemoveLineByWord(abs_g_proj, name, 0)
    #    RemoveLineByWord(abs_g_filter, name, 2)
    #    pass
    #pass