# Movie-Recommender
* A simple movie recommender which uses [Movielens Dataset](https://grouplens.org/datasets/movielens/) and recommends top 5 movies based on the movie you input by applying content based filtering on the dataset. <br>
* This script generates a csv file named `last.csv` in your current durectory with 5 movies that are recommended in decreasing order of suggestion. <br>
* The scores of each five movies are also there in the output file so that you can analyse how strongly the other movies are recommended relative to others. <br> <br>

# Requirements
* Numpy
* Pandas
* Movielens Dataset

# How to use
1. First you have to input the correct path of the downloaded dataset into the respective line of code (lines are commented where each dataset should go).
2. Then you need to install all the libraries required.
3. At last run the script. It will take almost 8-10 seconds to generate the output file.

# To-Do
* Create a gui interface using tkinter
