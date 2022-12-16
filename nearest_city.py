import geocoder 
import math

def ortdr (pos1, pos2):
    clen1 = math.radians(90 - pos2[0])
    clen2 = math.radians(90 - pos1[0])
    clen3 = math.radians(pos2[1] - pos1[1])
    uhel = math.acos(math.cos(clen1)*math.cos(clen2) + math.sin(clen1)*math.sin(clen2)*math.cos(clen3))
    return(6371*uhel)

coords = []

def vypis_coords(seznam):
    for i in seznam:
        print("lat: {}\t | lon: {}".format(i[0],i[1]))

with open ('lat_lon_origin.txt') as file:
        
        coords = []
        for i in file:
            coord = ''
            for c in i:
                if c.isdigit() or (c == "." or c == "-"):
                    coord = coord + c
            coords.append(float(coord))

coord_xy_pairs = []

for i in range (0, len(coords), 2):
    coord_xy_pairs.append([coords[i], coords[i+1]])

e = 0
for c in coord_xy_pairs:
    e += 1

print(e)

count_0 = 0

for i in coord_xy_pairs:
    geo = geocoder.osm(i,method ='reverse')
    print(count_0, geo.address)
    count_0+=1

cities_coords = []
cities = []

count_1 = 0

with open ('world_cities.txt', encoding = 'utf8') as file:
    for j in file:
        geo = geocoder.osm(j)
        if geo.latlng == None:
            continue
        else:
            cities_coords.append(geo.latlng)
            cities.append(j)
            print("{} | {}".format(count_1,geo.latlng))
            count_1+= 1

count_2 = 0

outputfile = open('outputfile.txt', 'w')

for i in coord_xy_pairs:
    nejbliz = ""
    vzd = 10000000000
    for j in cities_coords:
        if ortdr(i,j) <vzd: 
            vzd = ortdr(i,j)
            nejbliz = j
    outputfile.write("Input location: {} \n".format(i))
    outputfile.write("Distance: {} km \n".format(round(vzd,2)))
    outputfile.write("Nearest location: {}, {} \n".format(nejbliz, cities[count_2]))
    count_2+=1

outputfile.close()