import os

def GetMsgLines(file, lines):
    """
    获取要copy的行 
    file : 文件名
    lines: 行列表
    """
    start = "enum S2C_EVENT"
    over = "// class def for"
    cp_flag = False
    
    with open(file, "r", encoding='utf-8') as sfile:
        for line in sfile.readlines():
            # 开始复制
            if start in line:
                cp_flag = True
                pass

            # 结束复制
            if over in line:
                cp_flag = False
                break
                pass

            if not line.isspace() and cp_flag:
                if '\n' not in line:
                    line = line + '\n'
                #print(line)
                lines.append(line)
            pass
        pass
    pass

def FindFilesByExt(path, ext):
    """
    通过关键字word查询path目录下带有关键字的文件列表
    path:  目录路径
    ext :  匹配扩展名  比如 ".proto"
    """
    all_file = os.listdir(path)
    match_list = [] # 全路径
    name_list = []  # 文件名
    for file in all_file:
        filename = os.path.splitext(file)[0]
        fileext  = os.path.splitext(file)[1]
        if ext == fileext:
            match_list.append(os.path.join(path, file))
            name_list.append(filename+ext)
            pass
        pass
    
    return match_list,name_list

def PasteLines(lines, file):
    """
    行列表粘贴到一个新文件中
    lines : 行列表
    file  : 文件名
    """
    with open(file, "w+", encoding="utf-8") as cfile:
        cfile.writelines(lines)
        pass
    pass

def CopyFile(srcfile, dstfile):
    """
    将srcfile的内容拷贝到dstfile中
    srcfile : 源文件
    dstfile : 目标文件
    """
    with open(srcfile, "r", encoding="utf-8") as f1:
        with open(dstfile, "w", encoding="utf-8") as f2:
            f2.writelines(f1.readlines())
            pass
        pass
    pass

def FindDiffFiles(spath, dpath, filelist):
    """
    找出两个目录下同名文件内容不同的文件
    spath    : 源目录
    dpath    : 目标目录
    filelist : 文件名列表
    """
    diffs = []
    for name in filelist:
        sname = spath + name
        dname = dpath + name
        if os.path.exists(dname) and os.path.getsize(sname) != os.path.getsize(dname):
            diffs.append(name)
            pass
        pass
    return diffs

def PrintList(list):
    for item in list:
        print(item)

if __name__ == "__main__":
    svr_proto_path = "C:/DragonGirls/DragonGirlsServer/trunk/DragonGirlServer/Game/ProtoMessage/"
    cli_proto_path = "c:/DragonGirls/DragonGirlsConfig/工具/前端proto/__proto/"
    
    svr_msg = "c:/DragonGirls/DragonGirlsServer/trunk/DragonGirlServer/Game/event/MessageDef.h"
    cli_msg = "c:/DragonGirls/DragonGirlsConfig/工具/前端proto/__proto/_Protocol.proto"
    copy_lines = []
    diff_files = []
    
    # 1.同步msg到客户端_Protocol.proto文件
    GetMsgLines(svr_msg, copy_lines)
    #print(copy_lines)
    PasteLines(copy_lines, cli_msg)
    
    # 2.同步修改的proto文件到客户端
    match_list, name_list = FindFilesByExt(svr_proto_path, ".proto")
    PrintList(name_list)
    diff_files = FindDiffFiles(svr_proto_path, cli_proto_path, name_list)
    PrintList(diff_files)
    
    for diff in diff_files:
        CopyFile(svr_proto_path + diff, cli_proto_path + diff)
        pass
    pass