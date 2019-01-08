import json
from Country_Codes import get_country_code
from pygal.maps.world import World


#1 Reading the json file
filename = "population_data.json"
with open(filename) as f:
    data = json.load(f)
    #print(data)

#2 File has data from many years,we are interested only in 2010 data, country wise population
#3 converting population vallue to int,then float
#4 obtaining the country codes
    cc_populations = {}
    for info in data:
        if info['Year'] == '2010':
            country = info['Country Name']
            population = int(float(info['Value']))
            #print(country + " : " + str(population))
            code = get_country_code(country)
            if code:
                cc_populations[code] = population
                #print(code + " : " + str(population))
            #else:
                #print("ERROR : " + country)
    cc_pops_1,cc_pops_2,cc_pops_3 = {},{},{}
    for cc,pop in cc_populations.items():
        if pop < 10000000:
            cc_pops_1[cc] = pop
        elif pop < 1000000000:
            cc_pops_2[cc] = pop
        else:
            cc_pops_3[cc] = pop

    print(len(str(cc_pops_1)),len(str(cc_pops_2)),len(str(cc_pops_3)))
wm = World()
wm.title = "World population in 2010, by Country!"
wm.add('0-1m',cc_pops_1)
wm.add('10m-1bn',cc_pops_2)
wm.add('>1bn', cc_pops_3)
wm.render_to_file('world_population.svg')
