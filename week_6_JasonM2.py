#____Part 1: Conditional List__

web_users = ["Carl", "Donut", "Emani", "Elle", "Moredechai"]
new_users = ["Carl", "Donut", "Mongo", "Odette", "Lee"]
for new_user in new_users:
    if new_user in web_users:
        print(new_user, "This username is already taken. Please choose a different username.")
    else:        print(new_user, "This username is available.")

    #___________ Part 2: Nested Dictionaries __

Cities = { "New York": {"Country": "USA", "Population": 8804190, "Fun Fact": "It is the most linguistically diverse city in the world."}
          , "Los Angeles": {"Country": "USA", "Population": 3800000, "Fun Fact": "Cheeseburgers were invented in Los Angeles."},
            "Chicago": {"Country": "USA", "Population": 2700000, "Fun Fact": "The first skyscraper was built in Chicago."} }
for city, city_info in Cities.items():
    print("City: " + city)
    country = city_info["Country"]
    population = city_info["Population"]
    fun_fact = city_info["Fun Fact"]
    print("Country: " + country)
    print("Population: " + str(population))
    print("Fun Fact: " + fun_fact)
    