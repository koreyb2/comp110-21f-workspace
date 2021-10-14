

schools: dict[str, int]

schools = dict()

schools["UNC"] = 19400
schools["Duke"] = 6717
schools["NCSU"] = 26150

schools.pop("Duke")

schools["UNC"] = 20000
schools["NCSU"] += 200

schools = {"UNC": 19400, "Dukie": 6717, "NCSU": 26150}

for school in schools:
    print(f"Key: {school} -> Value: {schools[school]}")
