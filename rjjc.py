print('统计字符数：wc.exe -c 文件名')
print('统计单词数：wc.exe -w 文件名')
print('统计句子数：wc.exe -c 文件名')
print('统计注释行数：wc.exe -note 文件名')
print('统计空行数：wc.exe -spa 文件名')
print('统计代码行数：wc.exe -code 文件名')
a,b,name = input('输入指令：').split()  #定义指令格式
s = 0
if a == 'wc.exe' :
   if b == '-c' :
      filename = open(name,'r')   #打开文档，以只读方式
      file_contents = filename.read()   #读取文档内容，并保存到file_contents
      for file_content in file_contents:   
         if(file_content == '\n' or file_content == ' '):
                    continue
         else:
                    s = s + 1  #统计字符个数
      print('%s一共有%d个字符' % (name, s))
   if b == '-w' :
        filename = open(name,'r')
        file_contents= filename.read()
        words = file_contents.split()  
        num_words = len(words)
        print('%s一共有' % (name) + str(num_words) + '个单词')
   if b == '-sen' :
        filename = open(name,'r')
        file_contents = filename.read()       
        for file_content in file_contents:    
            if (file_content == '.'or file_content == '!'or file_content == '?'or file_content == ','):#判断句子是否完结
                    s = s + 1
        print('%s一共有%d个句子' % (name, s))
     
   if b == '-note' :
        filename = open(name,'r')
        file_contents = filename.read()       
        for file_content in file_contents:    
            if file_content == '*': #根据注释符号“*”判断注释行
                    s = s + 1
        print('%s一共有%d个注释行' % (name, s))
   if b == '-spa' :
        filename = open(name,'r')
        for file_content in filename.readlines():
            file_content = file_content.strip()  #去掉每行头尾空白   
            if file_content == "":
                s = s + 1
        print('%s一共有%d个空行' % (name, s))       
   if b == '-code' :       
        filename = open(name,'r')
        t = len(open(name,'r').readlines())#统计总行数t
        filename = open(name,'r')
        for file_content in filename.readlines():
            file_content = file_content.strip()     
            if file_content == "":
                s = s + 1  #统计空行
        file_contents = filename.read()       
        for file_content in file_contents:    
            if file_content == '*':
                    s = s + 1 #统计空行与注释行
        t = t - s #最后的代码行等于总行数减去空行与注释行之和
        print('%s一共有%d个代码行' % (name, t))
