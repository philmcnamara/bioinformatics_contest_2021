from pathlib import Path

base_path = Path.home()

with open(base_path / "input.txt", "r") as infile, open(base_path / "output.txt", "w") as outfile:
    communities = int(infile.readline().strip("\n").strip("\r"))
    for t in range(communities):
        people = int(infile.readline().strip("\n").strip("\r").split(" ")[0])
        contact_log = {}
        for day in range(7):
            contact_log[day] = []
            contacts = int(infile.readline().strip("\n").strip("\r"))
            for i in range(contacts):
                contact_log[day].append(infile.readline().strip("\n").strip("\r").split(" "))
        top_infection_score = 0
        most_dangerous = ""
        for person in range(1, people + 1):
            infection_score = 1
            potentially_infected = {person : 1}
            for day in contact_log:
                for contact in contact_log[day]:
                    a = int(contact[0])
                    b = int(contact[1])
                    q = float(contact[2])
                    if a in potentially_infected:
                        infection_score += q * potentially_infected[a]
                        if b in potentially_infected:
                            potentially_infected[b] = (potentially_infected[b] + q) - (potentially_infected[b] * q)
                        else:
                            potentially_infected[b] = q
            if infection_score > top_infection_score:
                most_dangerous = person
                top_infection_score = infection_score
        
        outfile.write(str(most_dangerous)  + "\n")