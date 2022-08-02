#This works for any game where number of prizes and tickets are predetermined (i.e., instant games).
#Assumption: total prizes run out at same rate as total tickets.

#Next step: Track projected payouts over time for each game...
#Figure out scraping...

from game import Game
game_list = []

# $500 FRENZY
frenzy = Game(name="$500 FRENZY", tickets=16128000, cost=10, standard=0.802)
frenzy_prizes = {

    # (Last updated: 6/30/22)
    500: [72016, 30018], 100: [239680, 100204], 50: [161280, 67594], \
    25: [161280, 67747], 20: [1290240, 544105], 15: [806400, 340750],\
    10: [1935360, 823551],
}
#game_list.append([frenzy, frenzy_prizes])

# 100X THE MONEY
hundrex = Game(name="100X THE MONEY", tickets=20160000, cost=10, standard=0.802)
hundrex_prizes = {

    # (Last updated: 7/1/22 @10:50pm ET)
    4000000: [4, 3], 1000000: [12, 10], 10000: [280, 241], \
    1000: [9660, 8270], 500: [16240, 13425], 200: [14560, 12000], \
    150: [17640, 14555], 100: [300440, 247897], 50: [201600, 166460], \
    25: [201600, 166625], 20: [1612800, 1333428], 15: [1008000, 834825], \
    10: [2419200, 2007466],
}
#game_list.append([hundrex, hundrex_prizes])

# $2,000,000 50X Cashword
cashword = Game(name="$2,000,000 50X Cashword", tickets=25200000, cost=10, standard=0.802)
cashword_prizes = {

    # (Last updated: 7/1/22 @3:04pm ET)
    2000000: [5, 5], 1000000: [10, 10], 10000: [250, 250], \
    2000: [700, 700], 1000: [6300, 6300], 500: [15575, 15570], \
    200: [31150, 31145], 100: [359625, 359553], 50: [252000, 251965], \
    40: [252000, 251962], 30: [252000, 251957], 25: [252000, 251967], \
    20: [2520000, 2519598], 15: [756000, 755883], 10: [3024000, 3023571],
}
#game_list.append([cashword, cashword_prizes])

# $4,000,000 MAYHEM
mayhem = Game(name="$4,000,000 MAYHEM", tickets=16128000, cost=10, standard=0.802)
mayhem_prizes = {

    # (Last updated: 7/2/22 @2:16pm ET)
    4000000: [3, 2], 1000000: [8, 6], 5000: [224, 149], \
    1000: [6832, 4786], 500: [24304, 16189], 100: [264656, 176213], \
    50: [161280, 107419], 25: [161280, 107724], 20: [1290240, 860880], \
    15: [806400, 539570], 10: [1935360, 1298414]
}
#game_list.append([mayhem, mayhem_prizes])

# LUCK OF THE IRISH TRIPLER
irish = Game(name="LUCK OF THE IRISH TRIPLER", tickets=8064000, cost=1, standard=0.700)
irish_prizes = {

    # (Last updated: 7/1/22)
    10000: [8, 3], 1000: [80, 10], 100: [8400, 524], \
    30: [14504, 1544], 25: [13440, 874], 10: [53760, 3718], \
    9: [53760, 6087], 5: [80640, 6057], 4: [80640, 6453], \
    3: [80640, 9839], 2: [564480, 50708], 1: [752640, 75891],
}
#game_list.append([irish, irish_prizes])

# Holiday Cash BLOWOUT
holiday = Game(name="Holiday Cash BLOWOUT", tickets=16128000, cost=10, standard=0.800)
holiday_prizes = {

    # (Last updated: 7/1/22 @4:35 ET)
    500: [29568, 116], 100: [497280, 4282], 50: [1290240, 11406],
}
#game_list.append([holiday, holiday_prizes])

# QUICK $500
quick = Game(name="QUICK $500", tickets=15120000, cost=10, standard=0.802)
quick_prizes = {

    # (Last updated: 7/1/22 @10:55pm ET)
    500: [67515, 646], 100: [224700, 2250], 50: [151200, 1796], \
    25: [151200, 2043], 20: [1209600, 19480], 15: [756000, 13149], \
    10: [1814400, 39720],
}
#game_list.append([quick, quick_prizes])

# $50,000 Jumbo BUCKS LIMITED EDITION (WINNER! +7% RETURN!)
jumbo = Game(name="$50,000 Jumbo BUCKS LIMITED EDITION", tickets=8064000, cost=10, standard=0.802)
jumbo_prizes = {

    # (Last updated: 7/1/22 @11:31pm ET)
    50000: [32, 6], 5000: [224, 23], 1000: [1568, 121], \
    500: [4144, 48], 200: [1792, 30], 150: [10024, 161], \
    100: [161280, 2813], 50: [806400, 15737],
}
#game_list.append([jumbo, jumbo_prizes])

# $10,000,000 Winter Riches
riches = Game(name="$10,000,000 Winter Riches", tickets=10080000, cost=20, standard=0.804)
riches_prizes = {

    # (Last updated: 7/2/22 @2:10pm ET)
    10000000: [2, 0], 1000000: [6, 2], 5000: [1750, 600], \
    2000: [1400, 493], 1000: [7980, 2786], 500: [12600, 3906], \
    200: [21280, 6598], 100: [359590, 111458], 50: [201600, 62977], \
    40: [201600, 63119], 30: [403200, 127404], 25: [806400, 263597], \
    20: [1411200, 450575],
}
#game_list.append([riches, riches_prizes])

# MONEY MONEY MONEY
money = Game(name="MONEY MONEY MONEY", tickets=12096000, cost=5, standard=0.771)
money_prizes = {

    # (Last updated: 7/2/22 @2:30pm ET)
    1000000: [3, 2], 2000: [168, 111], 1000: [2352, 1578], \
    500: [6888, 4390], 100: [94836, 60749], 50: [80640, 51851], \
    20: [241920, 156044], 15: [80640, 52085], 10: [1290240, 837310], \
    5: [1209600, 801900],
}
#game_list.append([money, money_prizes])

# DOUBLE your MONEY
double = Game(name="DOUBLE your MONEY", tickets=12096000, cost=5, standard=0.765)
double_prizes = {

    # (Last updated: 7/2/22 @2:40pm ET)
    1000000: [4, 3], 2000: [168, 114], 1000: [2016, 1368], \
    500: [7812, 4942], 100: [99120, 62952], 50: [80640, 51365], \
    20: [322560, 206122], 15: [161280, 103269], 10: [1451520, 932265],
}
#game_list.append([double, double_prizes])

# $4,000,000 Spectacular
spectacular = Game(name="4,000,000 Spectacular", tickets=15120000, cost=10, standard=0.802)
spectacular_prizes = {

    # (Last updated: 7/2/22 @2:54pm ET)
    4000000: [3, 2], 1000000: [5, 2], 10000: [210, 87], \
    1000: [7245, 3147], 500: [19950, 7879], 100: [255360, 101180], \
    50: [151200, 59951], 25: [604800, 239555], 20: [2116800, 845277],
}
#game_list.append([spectacular, spectacular_prizes])

# $15,000,000 MONEY MAKER
maker = Game(name="$15,000,000 MONEY MAKER", tickets=18144000, cost=30, standard=0.807)
maker_prizes = {

    # (Last updated: 7/2/22 @3:05pm ET)
    15000000: [3, 3], 1000000: [8, 8], 100000: [216, 175], \
    10000: [180, 143], 2000: [756, 612], 1000: [16884, 13635], \
    500: [82530, 64190], 200: [46242, 35900], 100: [1009260, 783216], \
    60: [362880, 282115], 50: [1451520, 1127063], 40: [2903040, 2255761],
}
#game_list.append([maker, maker_prizes])

# Lucky 7s
sevens = Game(name="Lucky 7s", tickets=12096000, cost=1, standard=0.700)
sevens_prizes = {

    # (Last updated: 7/2/22 @5:54pm ET)
    10000: [12, 3], 200: [1260, 314], 100: [8400, 2080], \
    40: [13524, 3397], 25: [16800, 4208], 20: [40320, 10199], \
    10: [120960, 31024], 5: [120960, 31870], 4: [120960, 31557], \
    3: [120960, 32267], 2: [846720, 229420], 1: [1128960, 326349],
}
#game_list.append([sevens, sevens_prizes])

# DECADE OF DOLLARS
decade = Game(name="DECADE OF DOLLARS", tickets=12096000, cost=1, standard=0.700)
decade_prizes = {

    # (Last updated: 7/2/22 @6:10pm ET)
    60000: [5, 1], 1000: [120, 35], 100: [11760, 3230], \
    40: [8400, 2302], 25: [13440, 3660], 20: [40320, 11122], \
    10: [120960, 33911], 5: [120960, 34243], 4: [120960, 34504], \
    3: [120960, 34964], 2: [846720, 249440], 1: [1128960, 351074],
}
#game_list.append([decade, decade_prizes])

# $10,000 BANKROLL
bankroll = Game(name="$10,000 BANKROLL", tickets=8064000, cost=1, standard=0.700)
bankroll_prizes = {

    # (Last updated: 7/2/22 @6:10pm ET)
    10000: [6, 3], 200: [840, 438], 100: [5600, 2934], \
    40: [9016, 4703], 25: [11984, 6206], 20: [26880, 14126], \
    10: [80640, 42368], 5: [80640, 42710], 4: [80640, 42974], \
    3: [80640, 43287], 2: [564480, 307174], 1: [752640, 415205],
}
#game_list.append([bankroll, bankroll_prizes])

# LOOSE CHANGE
change = Game(name="LOOSE CHANGE", tickets=10080000, cost=1, standard=0.700)
change_prizes = {

    # (Last updated: 7/2/22 @6:38pm ET)
    10000: [10, 1], 2000: [50, 8], 200: [1120, 71], \
    100: [9450, 555], 40: [11480, 713], 25: [8680, 545], \
    20: [33600, 2161], 10: [67200, 4232], 5: [100800, 6927], \
    4: [100800, 7441], 3: [100800, 8380], 2: [739200, 58433], \
    1: [974400, 87779],
}
#game_list.append([change, change_prizes])

# QUICK SILVER
silver = Game(name="QUICK SILVER", tickets=10080000, cost=1, standard=0.700)
silver_prizes = {

    # (Last updated: 7/2/22 @10:07pm ET)
    10000: [10, 4], 200: [1050, 516], 100: [7000, 3412], \
    40: [11270, 5541], 25: [14000, 6854], 20: [33600, 16552], \
    10: [100800, 49724], 5: [100800, 50294], 4: [100800, 50264], \
    3: [100800, 50873], 2: [705600, 362563], 1: [940800, 488792],
}
#game_list.append([silver, silver_prizes])

# WILD NUMBERS 5X
wild = Game(name="WILD NUMBERS 5X", tickets=10080000, cost=1, standard=0.700)
wild_prizes = {

    # (Last updated: 7/2/22 @10:54pm ET)
    10000: [10, 4], 200: [1050, 276], 100: [7000, 1921], \
    40: [11270, 3054], 25: [14000, 3806], 20: [33600, 9160], \
    10: [100800, 27930], 5: [100800, 28347], 4: [100800, 28722], \
    3: [100800, 29390], 2: [705600, 208102], 1: [940800, 293548],
}
#game_list.append([wild, wild_prizes])

# DIAMOND MILLIONS
diamond = Game(name="DIAMOND MILLIONS", tickets=20160000, cost=30, standard=0.807)
diamond_prizes = {

    # (Last updated: 7/2/22 @11:17pm ET)
    1000000: [80, 5], 20000: [120, 2], 3000: [700, 27], \
    1000: [10500, 417], 500: [46900, 612], 200: [64400, 950], \
    100: [1095640, 13818], 60: [403200, 7705], 50: [1612800, 24678], \
    40: [1612800, 28577], 30: [2419200, 49898],
}
game_list.append([diamond, diamond_prizes])

# FASTEST ROAD TO $1 MILLION
road = Game(name="FASTEST ROAD TO $1 MILLION", tickets=25200000, cost=30, standard=0.807)
road_prizes = {

    # (Last updated: 7/20/22 @12:00pm ET)
    650000: [122, 5], 20000: [250, 10], 3000: [1050, 30], \
    1000: [25200, 556], 500: [81200, 529], 200: [50575, 445], \
    100: [1364650, 6285], 60: [504000, 6095], 50: [2016000, 16779], \
    40: [2016000, 21856], 30: [3024000, 40213],
}
game_list.append([road, road_prizes])

#Modify the program so that prizes are contained within classes and
#automatically updated with scraping script! This way, we can make a games list and loop through it...

print()
for game in game_list:
    game[0].calc_payout(game[1])
    print(game[0].show_payout())
print()
