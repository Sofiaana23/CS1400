# Request initial values
# Casting to Int, assuming that valid values are provided
print("How many pirates:")
total_pirates = int(input())
print("How many units:")
total_units = int(input())

# Remove the initial 3 credits for each crew member (except for Yondu and Quill)
remaining_units = total_units - 3*(total_pirates-2)

# Calculate Yondu's share of 13%
yondu_share = round(remaining_units * .13,2)
remaining_units -= yondu_share

# Calculate Quill's share 11% of the 87%
quill_share = round(remaining_units * .11,2)
remaining_units -= quill_share

# Calculate the remaining share for each crew member
pirate_share = round(remaining_units / total_pirates,2)
yondu_share += pirate_share
quill_share += pirate_share

# Account for initial 3 credits given to crew members at the beginning
pirate_share += 3

# Print Results
print() # Add Newline for recommended formatting
print(f"Yondu's share: {yondu_share:.2f}")
print(f"Peter's share: {quill_share:.2f}")
print(f"Crew's share: {pirate_share:.2f}")
