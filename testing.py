from gensim.models import word2vec
from matplotlib import pylab
from sklearn.manifold import TSNE

def plot(embeddings, labels):
    assert embeddings.shape[0] >= len(labels), 'More labels than embeddings'
    pylab.figure(figsize=(15,15))  # in inches
    for i, label in enumerate(labels):
        x, y = embeddings[i, :]
        pylab.scatter(x, y, color='blue')
        pylab.annotate(label, xy=(x, y), xytext=(5, 2), textcoords='offset points',
                   ha='right', va='bottom')
    pylab.show()

visualization_words = 800
# transform embeddings to 2D by t-SNE
embed = model_SkipGram.embedding_matrix()[1:visualization_words+1, :]
tsne = TSNE(perplexity=30, n_components=2, init='pca', n_iter=5000, method='exact')
two_d_embed = tsne.fit_transform(embed)
# list labels
words = [model_SkipGram.reverse_dictionary[i] for i in range(1, visualization_words+1)]
# plot
plot(two_d_embed, words)



















# word = input('輸入詞𢑥：')
# def main():
# 	try:
# 		model1 = word2vec.Word2Vec.load("word2vec1.model")
# 		#print (model[word])
# 		print (model1.most_similar(word))
# 	except KeyError:
# 		print('No such word')
# 	try:
# 		model2 = word2vec.Word2Vec.load("word2vec2.model")
# 		print (model2.most_similar(word))
# 	except KeyError:
# 		print('No such word')
# if __name__ == "__main__":
# 	main()