
#数据的读取
def get_content(file):
    with open(file,'r',encoding='utf-8') as f:
        content = ''
        for i in f:
            i = i.strip()
            content += i
    return content

#高频词统计的函数
def get_TF(words,topK=10):
    tf_dic ={}
    for w in words:
        tf_dic[w] = tf_dic.get(w,0)+1
    return sorted(tf_dic.items(),key=lambda x:x[1],reverse=True)[:topK]

def stop_words(path):
    with open(path,encoding='utf-8') as f:
        return [l.strip() for l in f]
stop_words('stop_words.utf8')


#分词
def main():
    import glob
    import random
    import jieba
    
    files = glob.glob('data/content.txt')#查找符合特定规则的文件路径名 意思是后缀为.txt全部使用

    print("使用文本为",files)  

    try:
        corpus = [get_content(x) for x in files]
        print("全部样本corpus:\n",corpus)
        
        sample_inx = random.randint(0, len(corpus))
        print("sample_inx:\n",sample_inx)
        #增加效率
        # sample_inx = 1
        
        #split_words = list(jieba.cut(corpus[sample_inx]))
        #进行修改
        split_words = [x for x in jieba.cut(corpus[sample_inx]) if x not in stop_words('stop_words.utf8')]
        
        
        # print('样本之一：\n'+corpus[sample_inx])
        print('样本分词效果：'+'/ '.join(split_words))
        print('样本的topK(10)词:\n'+str(get_TF(split_words)))
        print(type(str(get_TF(split_words))))
        #高频词写入txt文件
        with open('data/word.txt','w') as f:
            f.write(str(get_TF(split_words)))  

    except Exception as err:
        print(err)

   
main()