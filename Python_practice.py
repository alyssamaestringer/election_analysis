
# counties = ["Arapahoe","Denver","Jefferson"]
# if counties[1] == 'Denver':
#     print(counties[1])

# if counties[3] != 'Jefferson':

#    print(counties[2])

counties = ["Arapahoe","Denver","Jefferson"]
# if "El Paso" in counties:
#     print("El Paso is in the list of counties.")
# else:
#     print("El Paso is not the list of counties")

# if "Arapahoe" in counties and "El Paso" not in counties:
#     print("Only Arapahoe is in the list of counties")
# else:
#     print("Arapahe is in the list of counties and El Paso is not in the list")

# for county in counties:
#     print(county)

counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}


voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]


# for county, voters in counties_dict.items():
#     print(f"{county} county has {voters} registered voters.")



# for county_dict in voting_data:
#     print(county_dict)

# for i in range(len(voting_data)):
#     print(voting_data[i])

# for i in range(len(counties_dict)):
#     print(counties_dict[i])
# for county_dict in voting_data:
#     for value in county_dict.values():
#         print(value)

# for counties_dict in voting_data:
#     for value in counties_dict.values():
#         print(value)

# for county_dict in voting_data:
#     print(county_dict['registered_voters'])

# for county_dict in voting_data:
#     print(county_dict['county'])

# my_votes = int(input("How many votes did you get in the election?"))
# total_votes = int(input("What is the total votes in the election?"))
# print(f"I received {my_votes / total_votes * 100}% of the total votes." )

# candidate_votes = int(input("How many votes did the candidate get in the election?"))
# total_votes =  int(input("What is the total number of votes in the election?"))
# message_to_candidate = (
#     f"You received {candidate_votes:,} number of votes. "
#     f"The total number of votes in the election was {total_votes:,}. "
#     f"You recieved {candidate_votes / total_votes * 100:.2f}% of the total votes.")

# print(message_to_candidate)

for counties, voters in voting_data:
    'f' = len(list)
    print('f'("{counties[0]} county has {voters[0]} registered voters."))

    