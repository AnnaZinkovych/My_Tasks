import numpy as np
import pandas as pd
import spacy
import warnings
warnings.filterwarnings("ignore", #warnings hendling
message=r".*\[W007\].*",
category=UserWarning)
nlp = spacy.load('en_core_web_md')

def movie_serch_function(sentences):
    my_sentence = nlp(sentences) #in this example we use certain sentence but we could also ask user to input any sentence
    movie_list = pd.read_csv("movies.txt", sep =":", header=None, names =["Title", "Description"])
    compare_similarity = 0 # I use this variable to make search quicker. If we need list of movies - we can use list structure instead of one variable.
    popular_film = 0 # I use this variable to make search quicker. If we need list of movies - we can use list structure instead of one variable.
    for i in range(len(movie_list)):
        similarity = nlp(movie_list.iloc[i, -1]).similarity(my_sentence)
        film_title = movie_list.iloc[i, 0]
        if similarity > compare_similarity:
            compare_similarity = similarity
            popular_film = film_title
    return popular_film

print(movie_serch_function("Will he save their world or destroy it? When the Hulk become too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk lands on the planet Sakeer where he is sold into slavery and trained as a gladiator."))

