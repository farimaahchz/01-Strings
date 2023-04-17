# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line

player_1 = "Ruud Gullit"
player_2 = "Marco van Basten"

# defining a variable for the exact moment of goals
goal_0 = int(32)
goal_1 = int(54)

# scorers = reports on who scored when in 

scorers = player_1 + " " + str(goal_0) + "," + " " + player_2 + " " + str(goal_1)     # adding " " as space in between the variables
print(scorers)  

# report = creating a single string with information on who scored when in the format of <scorer_name> scored in the <when_they_scored>nd minute

who_scored_when = "{} scored in the {}nd minute"+ "\n" + "{} scored in the {}th minute"
report= who_scored_when.format(player_1, goal_0, player_2, goal_1)
print(report)

# part2.

player = "Ronald Koeman"
first_name = player[:player.find(" ")]
print (first_name)

last_name = player[player.find(" ")+1:]
last_name_len = len(last_name)
print(last_name)
print (last_name_len)

name_short = first_name[0]+"."+ " " + last_name
print(name_short)

#chanting

chant = ((first_name + "!" + " ")*len(first_name)).rstrip()

print(chant)

chant_with_space = ((first_name + "!" + " ")*len(first_name))

print(chant_with_space)

good_chant = chant_with_space!=chant
print(good_chant)
