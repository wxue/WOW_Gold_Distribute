# WOW_Gold_Distribute

### Motivation 
My friend is a big fan of WOW, he ask me to build a tool to calculator the gold after their group mission. So here it is ...

### How to use
###### en
  1. `python WOW_GD.py [input_file.txt]`

    replace `input_file.txt` with your raw data file(the file export from MiDKP)


  2. check the file in the current directory called result.txt

###### zh-CN
  1. 键入命令 `python WOW_GD.py [input_file.txt]`

    将 `input_file.txt` 替换为你的原始数据文件名称(即从MiDKP中导出的txt标记文档)


  2. 查看此目录/文件夹中名为`result.txt`的文档，便是分配结果

### Install Python
###### en
This simple script is written in Python. To use this tool you must have python installed. If you are a Linux or Mac user, you may already got that in your system, but if you are a MS Windows user, I'm afraid you have to install it first.

You can [download python here](https://ironpython.codeplex.com/releases/view/90087).

[Official Python](http://www.python.org/).

###### zh-CN
这个简易工具是用python写的，那么你的电脑便需要安装了python编译器才能来跑它。如果你是Linux或者Mac苹果用户，你便不用再装了（python是这些系统自带的）。但是如果你是微软Windows用户，恐怕你得略麻烦一下去装个python。

[戳这里](https://ironpython.codeplex.com/releases/view/90087)下载python.

[Python官网](http://www.python.org/).

##### Python Version: 2.7

### Tips
###### About Punish
###### en
Make sure no one is punished to negative point(all points should be positive in total).

###### zh-CN
确保你记录MiDKP的时候没有队员惩罚到负值一下（即保证所有人的总得分都是正的，其实零也可以，但是何必呢，呵呵）。

### Version
##### v1.0
* 2013/9/28

匆匆写完，待各种Debug和优化。欢迎report bug。

### License
有任何问题，bug，修改建议请邮件联系我< [Email:T-Wind@xiakelite.com](mailto:T-Wind@xiakelite.com) >

The MIT License (MIT)

Copyright (c) 2013 Weiyu Xue

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
the Software, and to permit persons to whom the Software is furnished to do so,
subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.