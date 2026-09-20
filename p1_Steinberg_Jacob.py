# p1_Steinberg_Jacob.py
# Jacob Steinberg
# COP 4045 - Python Programming
# Homework 2 - Problem 1

def line_number(input_filename: str, output_filename: str) -> None:
  try:
    infile = open(input_filename, "r")
    outfile = open(output_filename, "w")

    number = 1

    for line in infile:
      outfile.write(str(number) + ". " + line)
      number += 1

    infile.close()
    outfile.close()

  except Exception as error:
    print("There was a problem opening or writing the file.")
    print(error)
    raise

def parse_functions(filename: str) -> tuple:
  try:
    file = open(filename, "r")
    lines = file.readlines()
    file.close()

    functions = []
    i = 0

    while i < len(lines):

      if lines[i].startswith("def"):
        line_num = i + 1

        start = 4
        open_paren = lines[i].find("(")
        close_paren = lines[i].find(")")

        function_name = lines[i][start:open_paren]
        arguments = lines[i][open_paren + 1:close_paren]
        definition = lines[i]

        if "#" in definition:
          definition = definition[:definition.find("#")].rstrip() + "\n"

        function_code = definition

        i += 1

        while i < len(lines):
          if lines[i].startswith("def"):
            break

          if (lines[i].strip() != ""
                and not lines[i][0].isspace()
                and not lines[i].startswith("#")):
            break

          current_line = lines[i]

          if current_line.strip() == "":
            i += 1
            continue

          if current_line.lstrip().startswith("#"):
            continue

          if "#" in current_line:
            current_line = (
              current_line[:current_line.find("#")].rstrip() + "\n"
            )

          function_code += current_line
          i += 1

        function_info = (
          line_num,
          function_name,
          arguments,
          fuction_code
        )

        functions.append(function_info)

      else:
        i += 1

    functions.sort(key=lambda x: x[1])

    return tuple(functions)

  except Exception as error:
    print("There was a problem reading the python file.")
    print(error)
    raise

def main() -> None:
  filename = "p1_Steinberg_Jacob.py"
  output_filename = "p1_Steinberg_Jacob_numbered.txt"

  print("Jacob Steinberg")
  print("Homework 2 - Problem 1")
  print()

  #Part A
  print("Part A")
  line_number(filename, output_filename)
  print("Numbered file created:", output_filename)

  print()

  #Part B
  print("Part B")

  result = parse_functions(filename)

  for function in result:
    print(fuction)
    print()

if __name__ == "__main__":
  main()
  
          
