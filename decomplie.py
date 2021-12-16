# coding=utf-8
import os
import shutil
import zipfile


# 删除文件
def remove_file(path):
    try:
        os.remove(path)
    except BaseException:
        pass


# 自动反编译的脚本

# -------定义的常量-----
# 需要源Apk拷贝到指定路径
target_path = "D:/develop/decompile/apk/"
# Apk改为zip,解压的路径
unzip_path = target_path + "unzip/"
# dex2jar的路径
dex2jar_path = "D:/develop/decompile/dex2jar-2.0/"
# 反编译jar的path
de_complie_path = dex2jar_path
# ---------------------

# --------复制到指定目录，且改为zip后缀-----------
# 输入源Apk地址
origin_file_path = input().replace("\\", "/")
full_file_name = os.path.basename(origin_file_path)
file_name = full_file_name[:-4]
target_file_path = target_path + file_name + ".zip"
shutil.copy(origin_file_path, target_file_path)
# ---------------------------------------------

# 解压
zip_file = zipfile.ZipFile(target_file_path, "r", zipfile.ZIP_DEFLATED)
zip_file.extractall(unzip_path)
zip_file.close()

# copy class.dex 到dex2jar目录去
origin_class_path = unzip_path + "classes.dex"
target_class_path = dex2jar_path + "classes.dex"
shutil.copy(origin_class_path, target_class_path)

# 反编译
de_complie_file = de_complie_path + "classes-dex2jar.jar"
remove_file(de_complie_file)
cmd = dex2jar_path + "d2j-dex2jar " + target_class_path + " --force -o " + de_complie_file
os.system(cmd)
remove_file("classes-error.zip")
