import jieba
import logging
import os
rootDir = os.getcwd()
def segment(input_path, output_path):
    logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
    global rootDir
    jieba.set_dictionary(rootDir + '/data/jieba-zh_TW/jieba/dict.txt')
    stopword_set = {' ', '\n'}
    with open(rootDir + '/data/stop_words.txt','r', encoding='utf-8') as stopwords:
        for stopword in stopwords:
            stopword_set.add(stopword.strip('\n'))
    output = open(output_path, 'a', encoding='utf-8')
    with open(input_path, 'r', encoding='utf-8') as f :
        content = f.read()
        words = jieba.lcut(content, cut_all=False)
        for word in words:
            if word not in stopword_set:
                output.write(word + ' ')
        output.write('\n')
    output.close()


curDir = os.getcwd()
curDir += '/data/lyrics'
os.chdir(curDir)
for subDir in os.listdir(curDir):
    os.chdir(curDir + '/' + subDir)
    if not os.path.exists('segments.txt'):
        f = open('segments.txt', 'a', encoding='utf-8')
        f.close()
        print('File \"segments.txt\" Created ')
    else:
        print('Directory \"segments.txt\" already exists')

    a = os.listdir(os.getcwd())[:]
    a.remove('segments.txt')
    for filename in a:
        segment(os.getcwd() + '/' + filename, 'segments.txt')