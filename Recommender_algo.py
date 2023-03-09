# Importing libraries
import pandas as pd

# Creating a function to recommend hotels based on user preferences
def recommend_hotel(preferences):
    df = pd.read_csv(r"C:\Users\user\Diani_Hotels.csv")
    # Calculating the similarity score between each hotel and the user preferences
    df['similarity_score'] = 0
    for feature, value in preferences.items():
        df['similarity_score'] += (df[feature] == value)
    # Sorting the hotels by similarity score and ratings
    df = df.sort_values(['similarity_score','Rating'], ascending=False)
    # Returning the top recommended hotel name
    return list(df['Hotel'][:5])


# Get user preferences
preferences = {}
preferences['Distance_from_beach'] = input('Enter your preferred distance from the beach (e.g. Beachfront, 500m, 1km): ')
preferences['Description'] = input('Enter your preferred hotel description (e.g. Travel Sustainable Property, Family-friendly): ')
preferences['Rating'] = input('Enter your preferred hotel rating (e.g. 5, 4): ')

# Get recommended hotel
recommended_hotels = recommend_hotel(preferences)
print('Recommended hotel:', recommended_hotels)

