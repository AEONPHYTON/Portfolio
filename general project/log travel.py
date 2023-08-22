travel_log = [
    {
        "country" : "France",
        "visit" : 12,
        "cities" : ["Paris", "Lille", "Dijon"]
    },
    {
        "country" : "Germany",
        "visit" : 5,
        "cities" : ["Berlin", "Hamburg", "Stuttgard"]   
    }
]

def add_new_country(country_visited, times_visited, cities_visited):
    new_country = {}
    new_country["country"] = country_visited
    new_country["visit"] = times_visited
    new_country["cities"] = cities_visited
    travel_log.append(new_country)

add_new_country("russia", 2, ["Moscow, Saint Petersburg", ""])
print(travel_log)