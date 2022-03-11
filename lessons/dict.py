"""dEMONSTARTING DICT CAPABILITIES."""

# Declaring the type of dict
schools: dict[str, int]


# initialize to an empty dict
schools = dict()

# Set a key value pairing in the dict
schools["UNC"] = 19_400
schools["Duke"] = 6_717
schools["NSCU"] = 26_150

# print a dict literal representation
print(schools)

# access a value by its key -- "lookup"
print(f"UNC has {schools['UNC']} students")

# remove a key-value from dict by its key
schools.pop("Duke")


# test for existence of key
is_duke_present: bool = "Duke" in schools

print(f"Duke is present: {is_duke_present}")


# demonstration of dict literals

schools = {}  # an example of empty dict literal
print(schools)
# alternatively, initalize key-value pairs
schools = {"UNC": 19400, "Duke": 6717, "NCSU": 26150}

print(schools)

print(schools["UNCC"])