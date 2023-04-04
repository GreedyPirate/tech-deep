import fileinput
import path

# 如果要修改文件，设置inplace为true
for line in fileinput.input(path.root_path + '/pom.xml', inplace=False):
    print(line)




