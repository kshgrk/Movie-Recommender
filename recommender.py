# Commented out IPython magic to ensure Python compatibility.
import numpy as np
import pandas as pd
import sys

gs = pd.read_csv('../input/movie-recommendation/genome-scores.csv') # path of genome-scores.csv
gt = pd.read_csv('../input/movie-recommendation/genome-tags.csv')   # path of genome-tags.csv
mvs = pd.read_csv('../input/movie-recommendation/movies.csv')       # path of movies.csv

# genre = np.array(mvs.sep[mvs.title == str(sys.argv[1])])[0]
# mid = int(mvs.movieId[mvs.title == str(sys.argv[1])])

# genre = np.array(mvs.sep[mvs.title == 'Insidious: Chapter 2 (2013)'[0]
mid = int(mvs.movieId[mvs.title == 'Insidious: Chapter 2 (2013)'])
scores = gs[['relevance', 'tagId']][gs.movieId==mid][gs.relevance>0.8].sort_values(by = 'relevance', ascending=False)

tags = np.array(scores.tagId)

sugs = pd.DataFrame(columns = ['movieId', 'tagId', 'relevance'])
score = 0
for i in tags:
    tmp = pd.DataFrame(gs[['movieId', 'tagId', 'relevance']][gs.tagId==i][gs.relevance>0.8])
    sugs = pd.concat([sugs, tmp])

sugs

l = pd.DataFrame(sugs['movieId'].value_counts())

l = l.head(10).sort_index(ascending=False) ## For recent movies and [ascending == True] for release date wise.

scores = scores.sort_values('tagId')

main_matrix = np.array(scores.relevance)

tags.sort()

def movie_score(tmp_id):
  tmp_matrix = np.array([])
  for i in range(tags.shape[0]):
    x = float(gs.relevance[gs.movieId==tmp_id][gs.tagId==tags[i]])
    try:
      tmp_matrix = np.append(tmp_matrix, [x])
    except:
      tmp_matrix = np.append(tmp_matrix, [0])
  return np.matmul(tmp_matrix, np.array(scores['relevance']))

l = l.head(6)

best = l.index

last = pd.DataFrame(columns = ['movieId', 'score'])
for i in range(1,6):
  last.loc[len(last.index)] = [best[i], movie_score(best[i])]

movie_score(best[1])

last.sort_values('score', ascending=False)

m_finder = lambda x: mvs.loc[mvs.movieId==x, 'title'].reset_index(drop=True)[0]

last['movie'] = last.movieId.apply(m_finder)

last.sort_values('score', ascending=False)

last.to_csv('./last.csv')
