import re
from officialComm import convertScrapedtoSent


def locationsInfo(articleBody):
    # reading from a body of text to find locations
    # test = open("LocationTest.txt", "r")
    lakes = re.compile(r'\S*Lake\S*(?:\s([A-Z]+))\S*')
    rivers = re.compile(r'(?:(([A-Z]))\S+\s)?\S*River')
    countys = re.compile(r'(?:(([A-Z]))\S+\s)?\S*County')
    creeks = re.compile(r'(?:(([A-Z]))\S+\s)?\S*Creek')
    townships = re.compile(r'(?:(([A-Z]))\S+\s)?\S*Townships')
    parks = re.compile(r'(?:(([A-Z]))\S+\s)?\S*Parks')
    schools = re.compile(r'\S*Elementary School|Intermediate School|Middle School|High School')
    highways = re.compile(r'I-(?:\S+\s)?|M-(?:\S+\s)?')
    cityLoc = re.compile(r'^[A-Z]\w*')
    cities = []
    cityFile = open("cities.txt", "r")
    for x in cityFile:
        cities.append(x.rstrip())
    # store all locations in array
    local = []
    # return all locations found in body of text from file
    for para in articleBody:
        temp = convertScrapedtoSent(para)
        for sent in temp:
            lake = lakes.findall(sent)
            for Lake in lake:
                local.append(Lake)
                break
            river = rivers.findall(sent)
            for River in river:
                local.append(River)
                break
            creek = creeks.findall(sent)
            for Creek in creek:
                local.append(Creek)
                break
            county = countys.findall(sent)
            for County in county:
                local.append(County)
                break
            township = townships.findall(sent)
            for Township in township:
                local.append(Township)
                break
            park = parks.findall(sent)
            for Park in park:
                local.append(Park)
                break
            school = schools.findall(sent)
            for School in school:
                local.append(School)
                break
            highway = highways.findall(sent)
            for Highway in highway:
                local.append(Highway)
                break

    # cities calculation (ONly returns the first city found for right now)
    cities = []
    cityFile = open("Cities.txt", "r")
    for x in cityFile:
        cities.append(x.rstrip().upper())
    city_set = set(cities)
    for para in articleBody:
        temp = convertScrapedtoSent(para)
        for sent in temp:
            # print(sent)
            city = re.findall(r'[A-Z][a-z]*', sent)
            citypair = ""
            for i in range(len(city)):
                if (i != len(city) - 1):
                    citypair = city[i] + " " + city[i + 1]

                # print("PRED "+city[i])
                # print("PRED "+citypair)
                if city[i].upper() in city_set:
                    local.append(city[i])
                elif citypair.upper() in city_set:
                    local.append(citypair)

    return local

