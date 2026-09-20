# Jacob Steinberg
# COP 4045
# Homework 2 - Problem 4
# IMDB Movie Data

import csv

def read_movie_list(filename: str) -> dict:
    try:
      movies = {}

      file = open(filename, "r", encoding="utf-8")
      reader = csv.reader(file)

      next(reader)

      for row in reader:
          title = row[1]
          year = row[2]
          value = row[3]

          movies[(title, year)] = value

      file.close()
      return movies

    except Exception as error:
      print("There was a problem reading", filename)
      print(error)
      raise

def read_casts(filename: str) -> dict:
    try:
        casts = {}
          
        file = open(filename, "r", encoding="utf-8")
        reader = csv.reader(file)

        for row in reader:
            title = row[0]
            year = row[1]
            director = row[2]
            actors = row[3:]

            casts[(title, year)] = (director, actors)

        file.close()
        return casts

    except Exception as error:
        print("There was a problem reading", filename)
        print(error)
        raise

def display_top_collaborations(rated_file: str,
                               cast_file: str,
                               limit=None) -> None:

    try:
        rated_movies = read_movie_list(rated_file)
        casts = read_casts(cast_file)

        collaborations = {}

        for movie in rated_movies:
          if movie in casts:
              director = casts[movie][0]
              actors = casts[movie][1]

              for actor in actors:
                  pair = (director, actor)

                  if pair in collaborations:
                      collaborations[pair] += 1
                  else:
                      collaborations[pair] = 1

        ranking = []

        for pair in collaborations:
            director = pair[0]
            actor = pair[1]
            count = collaborations[pair]

            ranking.append((director, actor, count))

        ranking.sort(key=lambda item: item[2], revers=True)

        if limit is not None:
          ranking = ranking[:limit]

        for item in ranking:
            print(item)

    except Exception as error:
        print("There was a problem displaying the top actors.")
        print(error)
        raise

def main() - None:

    print("Jacob Steinberg")
    print("COP 4045 - Homework 2 - Problem 4")
    print()

    rated_file = "imdb-top-rated.csv"
    grossing_file = "imdb-top-grossing.csv"
    cast_file = "imdb-top-casts.csv"

    print("Part A - Top Director/Actor Collaborations")
    print("------------------------------------------")
    display_top_collaborations(rated_file, cast_file, 10)

    print()

    print("Part B - Top Actors by Total Box Office")
    print("---------------------------------------")
    display_top_actors(grossing_file, cast-file, 10)

if __name__ == "__main__":
    main()
  
