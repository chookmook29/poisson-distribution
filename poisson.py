# Poisson distribution
# test
from fractions import Fraction



print ('How many home team goals?')
h_goals = input()
h_goals = float(h_goals)
print ('In how many games?')
h_games = input()
h_games = float(h_games)
print ('How many away team goals?')
a_goals = input()
a_goals = float(a_goals)
print ('In how many games?')
a_games = input()
a_games = float(a_games)
h = h_goals / h_games
h = float(h)
print ("%.2f" % h)

ha = a_goals / a_games
ha = float(ha)
print ("%.2f" % ha)


# For n goals from team in question it will be
x_0 = 1
x_1 = 1
x_2 = 2
x_3 = 6
x_4 = 24
x_5 = 120


# ...and now the formula

h_raisedh0 = h ** 1
h_raisedh1 = h ** 1
h_raisedh2 = h ** 2
h_raisedh3 = h ** 3
h_raisedh4 = h ** 4
h_raisedh5 = h ** 5


h_minus = -h
e_minus_raised_h = 2.718281828459 ** h_minus
e_minus_raised_h = float(e_minus_raised_h)

p_0 = 1 * e_minus_raised_h
p_0 = p_0 / 1
p_0 = p_0 * 100

p_1 = h_raisedh1 * e_minus_raised_h
p_1 = p_1 / 1
p_1 = p_1 * 100

p_2 = h_raisedh2 * e_minus_raised_h
p_2 = p_2 / 2
p_2 = p_2 * 100

p_3 = h_raisedh3 * e_minus_raised_h
p_3 = p_3 / 6
p_3 = p_3 * 100

p_4 = h_raisedh4 * e_minus_raised_h
p_4 = p_4 / 24
p_4 = p_4 * 100

p_5 = h_raisedh5 * e_minus_raised_h
p_5 = p_5 / 120
p_5 = p_5 * 100

p_6 = p_1 + p_2 + p_3 + p_4 + p_5 + p_0
p_6 = 100 - p_6 

totall = p_1 + p_2 + p_3 + p_4 + p_5 + p_0 + p_6


# For n goals from team in question it will be
x_0 = 1
x_1 = 1
x_2 = 2
x_3 = 6
x_4 = 24
x_5 = 120


# ...and now the formula

ha_raisedh0 = ha ** 1
ha_raisedh1 = ha ** 1
ha_raisedh2 = ha ** 2
ha_raisedh3 = ha ** 3
ha_raisedh4 = ha ** 4
ha_raisedh5 = ha ** 5


ha_minus = -ha
e_minus_raised_ha = 2.718281828459 ** ha_minus
e_minus_raised_ha = float(e_minus_raised_ha)

pa_0 = 1 * e_minus_raised_ha
pa_0 = pa_0 / 1
pa_0 = pa_0 * 100

pa_1 = ha_raisedh1 * e_minus_raised_ha
pa_1 = pa_1 / 1
pa_1 = pa_1 * 100

pa_2 = ha_raisedh2 * e_minus_raised_ha
pa_2 = pa_2 / 2
pa_2 = pa_2 * 100

pa_3 = ha_raisedh3 * e_minus_raised_ha
pa_3 = pa_3 / 6
pa_3 = pa_3 * 100

pa_4 = ha_raisedh4 * e_minus_raised_ha
pa_4 = pa_4 / 24
pa_4 = pa_4 * 100

pa_5 = ha_raisedh5 * e_minus_raised_ha
pa_5 = pa_5 / 120
pa_5 = pa_5 * 100

pa_6 = pa_1 + pa_2 + pa_3 + pa_4 + pa_5 + pa_0
pa_6 = 100 - pa_6 

totalla = pa_1 + pa_2 + pa_3 + pa_4 + pa_5 + pa_0 + pa_6


print ('There is ' + "%.2f" % p_0 + '% chance of 0 goals') 
print ('There is ' + "%.2f" % p_1 + '% chance of 1 goal') 
print ('There is ' + "%.2f" % p_2 + '% chance of 2 goals') 
print ('There is ' + "%.2f" % p_3 + '% chance of 3 goals') 
print ('There is ' + "%.2f" % p_4 + '% chance of 4 goals') 
print ('There is ' + "%.2f" % p_5 + '% chance of 5 goals')
print ('There is ' + "%.2f" % p_6 + '% chance of 6 or more goals')
print ('Home total is ' +  "%.2f" % totall + '%.') 

print ('Away team has ' + "%.2f" % pa_0 + '% chance of 0 goals') 
print ('Away team has ' + "%.2f" % pa_1 + '% chance of 1 goal') 
print ('Away team has ' + "%.2f" % pa_2 + '% chance of 2 goals') 
print ('Away team has ' + "%.2f" % pa_3 + '% chance of 3 goals') 
print ('Away team has ' + "%.2f" % pa_4 + '% chance of 4 goals') 
print ('Away team has ' + "%.2f" % pa_5 + '% chance of 5 goals')
print ('Away team has ' + "%.2f" % pa_6 + '% chance of 6 or more goals')
print ('Away total is ' + "%.2f" % totalla + '%.')


p_00 = p_0 * pa_0
p_00 = p_00 / 100

p_10 = p_1 * pa_0
p_10 = p_10 / 100

p_20 = p_2 * pa_0
p_20 = p_20 / 100

p_30 = p_3 * pa_0
p_30 = p_30 / 100

p_40 = p_4 * pa_0
p_40 = p_40 / 100

p_50 = p_5 * pa_0
p_50 = p_50 / 100

p_60 = p_6 * pa_0
p_60 = p_60 / 100

p_11 = p_1 * pa_1
p_11 = p_11 / 100

p_21 = p_2 * pa_1
p_21 = p_21 / 100

p_31 = p_3 * pa_1
p_31 = p_31 / 100

p_41 = p_4 * pa_1
p_41 = p_41 / 100

p_51 = p_5 * pa_1
p_51 = p_51 / 100

p_61 = p_6 * pa_1
p_61 = p_61 / 100

p_12 = p_1 * pa_2
p_12 = p_12 / 100

p_22 = p_2 * pa_2
p_22 = p_22 / 100

p_32 = p_3 * pa_2
p_32 = p_32 / 100

p_42 = p_4 * pa_2
p_42 = p_42 / 100

p_52 = p_5 * pa_2
p_52 = p_52 / 100

p_62 = p_6 * pa_2
p_62 = p_62 / 100

p_13 = p_1 * pa_3
p_13 = p_13 / 100

p_23 = p_2 * pa_3
p_23 = p_23 / 100

p_33 = p_3 * pa_3
p_33 = p_33 / 100

p_43 = p_4 * pa_3
p_43 = p_43 / 100

p_53 = p_5 * pa_3
p_53 = p_53 / 100

p_63 = p_6 * pa_3
p_63 = p_63 / 100

p_54 = p_5 * pa_4
p_54 = p_54 / 100

p_64 = p_6 * pa_4
p_64 = p_64 / 100

p_65 = p_6 * pa_5
p_65 = p_65 / 100


p_44 = p_4 * pa_4
p_44 = p_44 / 100
p_55 = p_5 * pa_5
p_55 = p_55 / 100
p_66 = p_6 * pa_6
p_66 = p_66 / 100

p_poisson_draw = p_00 + p_11 + p_22 + p_33 + p_44 + p_55 + p_66
p_poisson_home = p_10 + p_20 + p_30 + p_40 + p_50 + p_60 + p_21 + p_31 + p_41 + p_51 + p_61 + p_32 + p_42 + p_52 + p_62 + p_43 + p_53 + p_63 + p_54 + p_64 + p_65

print ('Chance for 0-0 is ' + "%.2f" % p_00 + '%.')
print ('Chance for 1-0 is ' + "%.2f" % p_10 + '%.')
print ('Chance for 2-0 is ' +  "%.2f" % p_20 + '%.')
print ('Chance for 3-0 is ' +  "%.2f" % p_30 + '%.')
print ('Chance for 4-0 is ' +  "%.2f" % p_40 + '%.')
print ('Chance for 5-0 is ' +  "%.2f" % p_50 + '%.')
print ('Chance for 6-0 or more is ' +  "%.2f" % p_60 + '%.')
print ('Chance for 1-1 is ' +  "%.2f" % p_11 + '%.')
print ('Chance for 2-1 is ' +  "%.2f" % p_21 + '%.')
print ('Chance for 3-1 is ' +  "%.2f" % p_31 + '%.')
print ('Chance for 4-1 is ' +  "%.2f" % p_41 + '%.')
print ('Chance for 5-1 is ' +  "%.2f" % p_51 + '%.')
print ('Chance for 6-1 or more is ' +  "%.2f" % p_61 + '%.')
print ('Chance for 1-2 is ' +  "%.2f" % p_12 + '%.')
print ('Chance for 2-2 is ' +  "%.2f" % p_22 + '%.')
print ('Chance for 3-2 is ' +  "%.2f" % p_32 + '%.')
print ('Chance for 4-2 is ' +  "%.2f" % p_42 + '%.')
print ('Chance for 5-2 is ' +  "%.2f" % p_52 + '%.')
print ('Chance for 6-2 or more is ' + "%.2f" % p_62 + '%.')
print ('Chance for 1-3 is ' +  "%.2f" % p_13 + '%.')
print ('Chance for 2-3 is ' +  "%.2f" % p_23 + '%.')
print ('Chance for 3-3 is ' +  "%.2f" % p_33 + '%.')
print ('Chance for 4-3 is ' +  "%.2f" % p_43 + '%.')
print ('Chance for 5-3 is ' +  "%.2f" % p_53 + '%.')
print ('Chance for 6-3 or more is ' +  "%.2f" % p_63 + '%.')
print ('Chance for a draw is ' +  "%.2f" % p_poisson_draw + '%.')
print ('Chance for a home win is ' +  "%.2f" % p_poisson_home + '%.')
