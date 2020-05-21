import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

super_bowls = pd.read_csv('datasets/super_bowls.csv')
print(super_bowls.head())
tv = pd.read_csv('datasets/tv.csv')
print(tv.head())
halftime_musicians = pd.read_csv('datasets/halftime_musicians.csv')
print(halftime_musicians.head())

# using info() method to inspect missing values of datasets 
super_bowls.info()
print('\n')
tv.info()
print('\n')
halftime_musicians.info()
print('\n')

# histogram of combined points
plt.style.use('seaborn')
plt.hist(super_bowls['combined_pts'])
plt.xlabel('Combined Points')
plt.ylabel('Number Of Super Bowls')
plt.show()

# display superbowl with highest and lowest points 
highest = super_bowls[super_bowls['combined_pts'] > 70]
print(highest)

lowest = super_bowls[super_bowls['combined_pts'] < 25]
print(lowest)

# histogram of point differences
plt.hist(super_bowls.difference_pts)
plt.xlabel('Point differences')
plt.ylabel('Number of Super Bowls')
plt.show()

# Display the closest game(s) and biggest blowouts

closest = super_bowls[super_bowls['difference_pts'] == 1]
print(closest)

biggest = super_bowls[super_bowls['difference_pts'] >= 35]
print(biggest)

# join games and tv data 

games_tv = pd.merge(tv[tv['super_bowl'] > 1], super_bowls, on = "super_bowl")

sns.regplot(x = 'difference_pts', y = 'share_household', data = games_tv)
plt.show()

# viewership and ad industry over time 

plt.subplot(3, 1, 1)
plt.plot(tv.super_bowl, tv.avg_us_viewers, color = '#648FFF')
plt.title('Average Number of US Viewers')
plt.show()

plt.subplot(3, 1, 2)
plt.plot(tv.super_bowl, tv.rating_household, color = '#DC267F')
plt.title('Household Rating')
plt.show()

plt.subplot(3, 1, 3)
plt.plot(tv.super_bowl, tv.ad_cost, color = '#FFB000')
plt.title('Ad Cost')
plt.xlabel('SUPER BOWL')
plt.show()

# Display all halftime musicians for Super Bowls up to and including Super Bowl 27

musicians = halftime_musicians[halftime_musicians.super_bowl <= 27]
print(musicians)

# Who has the most halftime show appearances?

halftime_appearences = halftime_musicians.groupby('musician').count()['super_bowl'].reset_index()
halftime_appearences = halftime_appearences.sort_values('super_bowl', ascending = False)

print(halftime_appearences[halftime_appearences['super_bowl'] > 1])

#  Who performed the most songs in a halftime show?
#A lot of the marching bands don't have num_songs entries.
#For non-marching bands, missing data starts occurring at Super Bowl XX.

# filter  out most marching bands
no_bands = halftime_musicians[~halftime_musicians.musician.str.contains('Marching')]
no_bands = no_bands[~no_bands.musician.str.contains('Spirit')]

# histogram of number of songs per performance
most_songs = int(max(no_bands['num_songs'].values))
plt.hist(no_bands.num_songs.dropna(), bins = 11)
plt.xlabel('Number of songs per Halftime show Performance')
plt.ylabel('Number of Musicians')
plt.show()

# top 15
no_bands = no_bands.sort_values('num_songs', ascending = False)
print(no_bands.head(15))

# 2018-2019 conference champians


# who will be winner LIII?
super_bowl_LIII_winner = input("who will bw winner from 'New England Patriots' and 'Los Angeles Rams'  = ")
print("\n")

print("The winner of super bowl will be ", super_bowl_LIII_winner)