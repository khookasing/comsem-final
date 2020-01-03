import logging
from gensim.models import word2vec
def main():
    logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
    sentences = word2vec.LineSentence("data/lyrics/4 In Love/segments.txt")
    model = word2vec.Word2Vec(sentences, window=5, min_count=5, size=300, sg=0, workers=32, hs=1, iter=5)
    model.save("word2vec.model")
    
if __name__ == "__main__":
    main()