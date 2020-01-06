import logging
from gensim.models import word2vec
import re

def main():
    # logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
    # sentences1 = word2vec.LineSentence("data/segments/楊丞琳.txt")
    # model1 = word2vec.Word2Vec(sentences1, window=5, min_count=5, size=300, sg=0, workers=32, hs=1, iter=5)
    # model1.save("word2vec1.model")
    # sentences2 = word2vec.LineSentence("data/segments/4 In Love.txt")
    # model2 = word2vec.Word2Vec(sentences2, window=5, min_count=5, size=300, sg=0, workers=32, hs=1, iter=5)
    # model2.save("word2vec2.model")
    comp = input('1~3:')
    if comp == '1':
        file_before = 'data/segments/4 In Love.txt'
        file_after = 'data/segments/楊丞琳.txt'
    elif comp == '2':
        file_before = 'data/segments/信樂團.txt'
        file_after = 'data/segments/信.txt'
    elif comp == '3':
        file_before = 'data/segments/SHE.txt'
        file_after = 'data/segments/田馥甄.txt'
    with open(file_before, 'r') as f:
        before = f.read()
    with open(file_after, 'r') as f:
        after = f.read()
    with open('data/fake_token.txt', 'r') as f:
        faketoken = f.read()
    word = input('輸入要比較的字：')
    word_bl = word + ' '
    word_nl = word + '\n'
    wbib = word_bl in before
    wbia = word_bl in after
    wnib = word_nl in before
    wnia = word_nl in after
    if (wbib | wnib) & (wbia | wnia):
        before = before.replace(word_bl, 'b' + word_bl)
        before = before.replace(word_nl, 'b' + word_nl)
        after = after.replace(word_bl, 'a' + word_bl)
        after = after.replace(word_nl, 'a' + word_nl)
        with open('data/segments/comparison.txt', 'w') as f:
            f.write(before.replace('\n', '') + faketoken.replace('\n', '') + after.replace('\n', ''))
        sentences = word2vec.LineSentence("data/segments/comparison.txt")
        model = word2vec.Word2Vec(sentences, window=5, min_count=5, size=300, sg=0, workers=32, hs=1, iter=5)
        model.save("word2vec.model")
        #model1 = word2vec.Word2Vec.load("word2vec.model")
		#print(model[word])
        print(model.most_similar('b'+word))
        #print(model1.most_similar('b'+word))
        print(model.most_similar('a'+word))
        #print(model1.most_similar('a'+word))
    else:
        print('Try another word')
if __name__ == "__main__":
    main()