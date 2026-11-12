#import pandas, set the database var connection and make pandas read it
#Make an input section; maybe as a loop to make it more robust if the year entered is not in the database
#have a dictionary with lists after each key correlating to the team reqs
#design a for loop to the keys to receive their related categories
#print the updated lists so they contain the right teams from the requested year
import pandas as pd

df = pd.read_csv('cfb.csv')


while True: # I made the while loop so we can filter out requests for years before the database begins
    season_choice = int(input("Which season would you like to analyze?")) #putting the input inside the loop allows it to ask again
    if season_choice >= 2013:
        season_df = df[df["Season"] == season_choice]
        break
    else:
        print("That season is not in this database. Please choose a season after 2013.")

#we made the keys as the titles of categories for the teams with related lists
win_categories = {
    "10 or more wins": [],
    "8-9 wins": [],
    "6-7 wins": [],
    "Fewer than 6 wins": []
}

#the format of this table is long format, meaning each team's info (year, stats) is found in rows, so we use rows
# this connects to the wins the team had in each of it's season rows
for _, row in season_df.iterrows():
    wins = row["Win"]
    team = row["Team"]

#this if loop allows us to add team to its correlating key in the dictionary
    if wins >= 10:
        win_categories["10 or more wins"].append(team)
    elif wins >= 8 and wins <= 9:
        win_categories["8-9 wins"].append(team)
    elif wins >= 6 and wins <= 7:
        win_categories["6-7 wins"].append(team)
    else:
        win_categories["Fewer than 6 wins"].append(team)

#this is a simple way to call on the keys and their correlated items and print them in an organized fashion
for key, items in win_categories.items(): 
    print(key)
    print()
    for item in items:
        print(item)
    print()
