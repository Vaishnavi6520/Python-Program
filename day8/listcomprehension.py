Movie_names=["Lucy","incidious","IT","Considious","Conjuring","The Nun","Haunted"]
# New_movie =[]
# for i in Movie_names:
#     if 'a' in i:
#         New_movie.append(i)
new_movie=[i for i in Movie_names if 'a' in i]

print(new_movie)