# empty_dict = {}

# print(empty_dict)

# bike_owners = { "james" : "Dukati", 
#                "Sumit" : "Pulsar", 
#                "Saumya" : "Scooty"}

# print(bike_owners["james"])
# print(bike_owners["Sumit"])

# int_dict = {1:22, 2:23, 3:24}

# print(int_dict)

# student_details = {"sumit": 2000, "saumya" : 9000, "shwetank": 6000, "shubhang" : 90000}

# print(student_details.keys())

# print( "sumit" in student_details.keys())

# print(student_details.values())

# mixed_dict = { False : "tempa", "list_val" : [1,2,3], "tup_val" : (1,2,3), "my_dict": {"ram": "hindu"}
# }

# print(mixed_dict)


bike_details = {"name" : " Sumit", "bike_model" : "pulse", "year": 2010}

print(bike_details.keys())

bike_details["purchasing_place"] = "Bangalore"


print(bike_details)

bike_details["bike_model"] = "Pulser"

print(bike_details.get("bike_model"))