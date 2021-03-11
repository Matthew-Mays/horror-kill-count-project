This project will be an analysis of horror movie's and their kills.
Current plans are to have a kill table and a movie meta data table.
Using these I want to look into the statistics of many different things like #1 most common murder weapon, the average kills per movie, and how those statistics compare to the movies Rotten Tomatoes Score.

Data Dictionary
kc-kill-count features:
Name: Name of or alias of characters, non main unnamed characters will go under Unnamed
Kill Order: The order of kills that take place in their respective movie
mtype: How the victim died
mwep: What weapon or item was used to kill the victim
gc: This comes straight from the Youtube Kill Count series, the Golden Chainsaw. This is given to the coolest kill of the movie as awarded by the Kill Count creater
dm: Same as above but this is the Dull Machete awarded for the lamest kill of the movie.
title: The title of the film the kills take place in
gender: This is not only human genders with a 0 for male and 1 for female, but also contains non-humans with the #2 and unknowns with the #3.

kc-movie-data features:
title: The title of the movie
date: The release date of the movie
rt_score: This is the rotten tomatoes review score for the movie using the RT score and not the audience score
kc: The total number of kills in the movie
length: The total runtime of the movie