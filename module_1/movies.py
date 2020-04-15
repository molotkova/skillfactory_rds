import pandas as pd
from collections import Counter
import math
data = pd.read_csv('data.csv')
answer_ls = []
answer_ls.append(data.original_title[data.budget.idxmax()])
answer_ls.append(data.original_title[data.runtime.idxmax()])
answer_ls.append(data.original_title[data.runtime.idxmin()])
answer_ls.append(round(data.runtime.mean()))
answer_ls.append(math.floor(data.runtime.median()))
money = data.revenue - data.budget
data.insert(3, 'profit', money, True)
answer_ls.append(data.original_title[data.profit.idxmax()])
answer_ls.append(data.original_title[data.profit.idxmin()])
answer_ls.append(len(data[data.revenue > data.budget]))
year08 = data[data.release_year == 2008]
answer_ls.append(year08.original_title[year08.revenue.idxmax()])
year = data[(data.release_year >= 2012)
            & (data.release_year <= 2014)]
answer_ls.append(year.original_title[year.profit.idxmin()])
data_plot = data['genres'].str.cat(sep='|')
dat = pd.Series(data_plot.split('|'))
info = dat.value_counts(ascending=False)
answer_ls.append(info[info == info.max()].index[0])
genres = ['Action', 'Adventure', 'Drama', 'Comedy', 'Thriller']
prof = data[data.profit > 0]
def num1(genre):
    return len(prof[prof.genres.str.contains(genre)])
count = {}
for gen in genres:
    count[gen] = num1(gen)
answer_ls.append(max(count, key=count.get))
d = data['director'].value_counts()
answer_ls.append((d.loc[d == d.max()]).index[0])
d = (data[data.profit > 0])['director'].value_counts()
answer_ls.append((d.loc[d == d.max()]).index[0])
gr = data.groupby(['director'])['profit'].sum()
answer_ls.append((gr.loc[gr == gr.max()]).index[0])
act = ['Emma Watson', 'Johnny Depp', 'Michelle Rodriguez', 'Orlando Bloom', 'Rupert Grint']
def num2(name):
    return (prof[prof.cast.str.contains(name)])['profit'].sum()
count = {}
for name in act:
    count[name] = num2(name)
answer_ls.append(max(count, key=count.get))
data12 = data[data.release_year == 2012]
act = ['Nicolas Cage', 'Danny Huston', 'Kristen Dunst', 'Jim Sturgess', 'Sami Gayle']
def num3(name):
    return (data12[data12.cast.str.contains(name)])['profit'].sum()
count = {}
for name in act:
    count[name] = num2(name)
answer_ls.append(min(count, key=count.get))
act = ['Tom Cruise', 'Mark Wahlberg', 'Matt Damon', 'Angelina Jolie', 'Adam Sandler']
b = data[data.budget > data.budget.mean()]
def num4(name):
    return len(b[b.cast.str.contains(name)])
count = {}
for name in act:
    count[name] = num4(name)
answer_ls.append(max(count, key=count.get))
genres = ['Drama', 'Action', 'Thriller', 'Adventure', 'Crime']
NC = data[data.cast.str.contains('Nicolas Cage')]
def num5(name, col, data): # более универсальная функция
    return len(data[data[col].str.contains(name)])
count = {}
for genre in genres:
    count[genre] = num5(genre, 'genres', NC)
answer_ls.append(max(count, key=count.get))
studios = ['Universal', 'Paramount Pictures', 'Columbia Pictures',
           'Warner Bros', 'Twentieth Century Fox Film Corporation']
count = {}
for studio in studios:
    count[studio] = num5(studio, 'production_companies', data)
answer_ls.append(max(count, key=count.get))
data15 = data[data.release_year == 2015]
studios = ['Universal Pictures', 'Paramount Pictures', 'Columbia Pictures',
           'Warner Bros', 'Twentieth Century Fox Film Corporation']
count = {}
for studio in studios:
    count[studio] = num5(studio, 'production_companies', data15)
answer_ls.append(max(count, key=count.get))
c = data[data['genres'].str.contains('Comedy')]
studios = ['Universal', 'Paramount Pictures', 'Columbia Pictures',
           'Warner Bros', 'Walt Disney']
count = {}
def num6(name, col, data): # более универсальная функция, считает профит
    return (data[data[col].str.contains(name)])['profit'].sum()
for studio in studios:
    count[studio] = num6(studio, 'production_companies', c)
answer_ls.append(max(count, key=count.get))
studios = ['Universal', 'Paramount Pictures', 'Columbia Pictures',
           'Warner Bros', 'Lucasfilm']
count = {}
for studio in studios:
    count[studio] = num6(studio, 'production_companies', data12)
answer_ls.append(max(count, key=count.get))
par_pic = data[data['production_companies'].str.contains('Paramount Pictures')]
answer_ls.append(par_pic.original_title[par_pic.profit.idxmin()])
grouped = data.groupby(['release_year'])['profit'].sum()
answer_ls.append(grouped[grouped == grouped.max()].index[0])
gr = (data[data['production_companies'].str.contains('Warner Bros')]).groupby(['release_year'])['profit'].sum()
answer_ls.append(gr[gr == gr.max()].index[0])
months = ['1/', '6/', '12/', '9/', '5/']
names = ['Январь', 'Июнь', 'Декабрь', 'Сентябрь', 'Май']
count = {}
def num7(name, col, data): # более универсальная функция
    return len(data[data[col].str.startswith(name)])
for month, name in zip(months, names):
    count[name] = num7(month, 'release_date', data)
answer_ls.append(max(count, key=count.get))
summer = ['6/', '7/', '8/']
films = 0
for month in summer:
    films += num7(month, 'release_date', data)
answer_ls.append(films)
winter = tuple(['12/', '1/', '2/'])
w = data[data['release_date'].str.startswith(winter)]
direct = ['Steven Soderbergh', 'Christopher Nolan', 'Clint Eastwood', 'Ridley Scott',
          'Peter Jackson']
count = {}
for name in direct:
    count[name] = num5(name, 'director', w)
answer_ls.append(max(count, key=count.get))
def num8(name, col, data): # более универсальная функция, считает профит
    return (data[data[col].str.startswith(name)])['profit'].sum()
count = {}
months = ['1/', '6/', '12/', '9/', '5/']
for year in range(2000, 2016):
    y = data[data.release_year == year]
    l = {}
    for month, name in zip(months, names):
        l[name] = num8(month, 'release_date', y)
    count[year] = max(l, key=l.get)
track = {}
for key, value in count.items():
    if value not in track:
        track[value]= 0
    else:
        track[value]+= 1
answer_ls.append(max(track, key=track.get))
studios = ['Universal', 'Warner Bros', 'Jim Henson Company', 'Paramount Pictures',
           'Four By Two Productions']
count = {}
for studio in studios:
    s = data[data['production_companies'].str.contains(studio)]
    count[studio] = s.original_title.str.count('\S').mean()
answer_ls.append(max(count, key=count.get))
count = {}
for studio in studios:
    s = data[data['production_companies'].str.contains(studio)]
    count[studio] = s.original_title.str.count('\S+').mean()
answer_ls.append(max(count, key=count.get))
title = data.original_title.str.lower().to_list()
answer_ls.append(len(Counter((' '.join(title)).split(' ')).keys()))
ind = (data.vote_average.sort_values(ascending=False).iloc[range(math.ceil(0.01*len(data)))]).index
best = data.iloc[list(ind)].original_title.tolist()
first = ['Inside Out', 'Gone Girl', '12 Years a Slave']
second = ['Blood Rayne, The Adventures of Rocky and Bullwinkle']
third = ['The Lord of the Rings: The Return of the King', 'Upside Down']
forth = ['300', 'Lucky Number Slevin']
fifth = ['Upside Down', '300', 'Inside Out', 'The Lord of the Rings: The Return of the King']
answ = [first, second, third, forth, fifth]
for l in answ:
    result = all(elem in best for elem in l)
    if result:
        answer_ls.append(l)
pair1 = ['Johnny Depp', 'Helena Bonham Carter']
pair2 = ['Hugh Jackman', 'Ian McKellen']
pair3 = ['Vin Diesel', 'Paul Walker']
pair4 = ['Adam Sandler', 'Kevin James']
pair5 = ['Daniel Radcliffe', 'Rupert Grint']
act = [pair1, pair2, pair3, pair4, pair5]
def num9(name0, name1):
    return len(data[(data.cast.str.contains(name0)) & (data.cast.str.contains(name1))])
count = {}
for pair in act:
    count[', '.join(pair)] = num9(pair[0], pair[1])
answer_ls.append(max(count, key=count.get))
directors = ['Quentin Tarantino', 'Steven Soderbergh', 'Robert Rodriguez',
             'Christopher Nolan', 'Clint Eastwood']
count = {}
for name in directors:
    dir = data[data['director'].str.contains(name)]
    count[name] = len(dir[dir.profit > 0]) / len(dir)
answer_ls.append(max(count, key=count.get))
answer_df = pd.DataFrame({'Id': range(1, len(answer_ls)+1), 'Answer': answer_ls}, columns=['Id', 'Answer'])
