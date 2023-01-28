import matplotlib.pyplot as plt 
import seaborn as sns
import pandas as pd

#importing DataSet Named 'Movies'
movies = pd.read_csv('movies.csv')

# Create a bar chart for movie genre 
sns.countplot(x='genre', data=movies)
plt.title('Movie Genres')
plt.xlabel("Genres")
plt.ylabel("Counts")
plt.show()
plt.close()

# Create a pie chart for movie genre
movies.genre.value_counts().plot.pie()
plt.axis('equal')
plt.title('Movie Genres')
plt.show()
plt.close()

