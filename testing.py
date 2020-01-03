from gensim.models import word2vec
def main():
	model = word2vec.Word2Vec.load("word2vec.model")
	print (model['音樂'])
	print (model.most_similar("音樂"))
if __name__ == "__main__":
	main()