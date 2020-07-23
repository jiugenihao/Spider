import os
import os.path
from FileOpt import ListFileByExt

#proto_path  = "C:/DragonGirls/DragonGirlsServer/trunk/DragonGirlServer/Game/ProtoMessage/"
#files = ListFileByExt(proto_path, ".proto")
#print(files)

# 获取目录下所有配置文件
cfg_path = "c:/DragonGirls/DragonGirlsServer/trunk/DragonGirlServer/Debug/Config/"
config_names = ListFileByExt(cfg_path, ".txt")
print("file num is :",len(config_names))

# 获取填入转换表的配置文件
convert_file = "c:/DragonGirls/DragonGirlsServer/trunk/DragonGirlServer/Debug/Config/_converttxt.bat"
no_space_lines = [] # 去掉空行
with open(convert_file, "r", encoding="utf-8") as f1:
    for line in f1.readlines():
        if not line.isspace():
            no_space_lines.append(line)
        pass
    pass

convert_names = []
for line in no_space_lines:
    if "ConfigFileBuilder" in line:
        convert_names.append(line.split(" ")[1])
        #print(line.split(" ")[1])
    pass
print("line num is :", len(no_space_lines))

# 取差集
diff1 = [name for name in config_names if name not in convert_names]
diff2 = [name for name in convert_names if name not in config_names]

insect = [name for name in config_names if name in convert_names]
print("diff1:", diff1)
print("diff2:", diff2)
print(len(insect))
