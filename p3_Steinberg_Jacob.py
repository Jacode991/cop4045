# Jacob Steinberg
# COP 4045
# Homework 2 - Problem 3
# Social Network

import csv

def add_user(sn: dict,, username: str, fullname: str) -> bool:
    try:
      if username in sn:
        return False

      sn[username] = (fullname, [])
      return True

    except Exception as error:
        print("There was a problem adding the user.")
        print(error)
        raise

def add_friend(sn: dict, user1: str, user2: str) -> bool:
  try:
    if user1 not in sn or user2 not in sn:
      return False

    if user2 not in sn[user1][1]:
      sn[user1][1].append(user2)

    return True

  except Exception as error:
    print("There was a problem adding the friendship.")
    print(error)
    raise

def get_friends(sn: dict, user1: str, distance: int) -> list:
  try:
    if user1 not in sn or distance <= 0:
      return []

    friends_found = []
    current_level = [user1]
    visited = [user1]

    for level in range(distance):
      next_level = []

      for user in current_level:
        for friend in sn[user][1]:

          if friend not in visited:
            visited.append(friend)
            friends_found.append(friend)
            next_level.append(friend)

      current_level = next_level

      if len(current_level) == 0
          break

    return friends_found

  except Exception as error:
    print("There was a problem finding the friends.")
    print(error)
    raise

def save_network(filename: str, sn: dict) -> None:
  try:
    file = open(filename, "w", newline="")
    writer = csv.writer(file)

    for username in sn:
      fullname = sn[username][0]
      friends = sn[username][1]

      row = [username, fullname] + friends
      writer.writerow(row)

    file.close()

  except Exception as error:
      print("There was a problem saving the network.")
      print(error)
      raise

def load_network(filename: str) -> dict:
  try:
    sn = {}

    file = open(filename, "r", newline="")
    reader = csv.reader(file)

    for row in reader:
      username = row[0]
      fullname = row[1]
      friends = row[2:]

      sn[username] = (fullname, friends)

    file.close()

    return sn

  except Exception as error:
    print("There was a problem loading the network.")
    print(error)
    raise

def main() -> None:
    print("Jacob Steinberg")
    print("COP 4045 - Homework 2 - Problem 3")
    print()

    sn = {}

#Part A
    print("Part A - Adding Users")

    print("Adding alice:",
          add_user(sn, "alice", "Alice Smith"))
    print("Adding maria:",
          add_user(sn, "maria", "Maria Cortez"))
    print("Adding joe:",
          add_user(sn, "joe", "Joseph Adams"))
    print("Adding eve:",
          add_user(sn, "eve", "Evelyn Cooper"))
    print("Adding david:",
          add_user(sn, "david", "David Benson"))

#Adding existing user
    print("Adding alice again:",
          add_user(sn, "alice", "Alice Smith"))

    print()
    print("Network after adding users:")
    print(sn)
    print()

#Part B
    print("Part B - Adding Friends")

    print("alice and maria:",
          add_friend(sn, "alice", "maria"))

    print("maria and joe:",
          add_friend(sn , "maria", "joe"))

    print("maria and david:",
          add_friend(sn, "maria", "david"))

    print("joe and eve:",
          add_friend(sn, "joe", "eve"))
  #test username that doesn't exist
    print("alice and bob:",
          add_friend(sn, "alice", "bob"))

    print()
    print("Network after adding friends:")
    print(sn)
    print()

#Part C
    print("Part C - Getting Friends")

    print("Alice, distance 1:",
          get_friends(sn, "alice", 1))
    
    print("Alice, distance 2:",
          get_friends(sn, "alice", 2))

    print("Alice, distance 3:",
          get_friends(sn, "alice", 3))

    print("Unknown user:",
          get_friends(sn, "bob", 2))

    print()

#Part D
    print("Part D - Saving Network")

    filename = "social_network.csv"
    save_network(filename, sn)

    print("Network saved to", filename)
    print()

#Part E
    print("Part E - Loading Network")

    loaded_network = load_network(filename)

    print("Loaded_network:")
    print(loaded_network)
    print()

    print("Original network equals loaded network:",
          sn == loaded_network)

if __name__ == "__main__":
  main()
  
          
  
