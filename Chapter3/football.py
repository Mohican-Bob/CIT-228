teams = ["Lions", "Bears", "Packers", "Vikings", "Browns"]
print("Current Football teams:", teams)
teams.append("Steelers")
print("Updated Teams:", teams)
del teams[1]
print("Teams in Playoffs:", teams)
teams.pop()
print("Teams in Wildcard Round:", teams)
teams.remove("Packers")
print("Teams in Divisional Round:", teams)
print("Teams Seed Placement", sorted(teams))
teams.reverse()
print("Weakest teams to Strongest:", teams)
teams.sort()
print("Sorted Teams:", teams)
print("Number of Teams Left:", len(teams))

