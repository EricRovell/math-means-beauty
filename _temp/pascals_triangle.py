def pascals_triangle(rows):
  if rows == 1: return 1
  if rows == 2: return [1, 1]

  triangle = [[1], [1, 1]]

  # new rows
  for _ in range(rows - 2):
    next_row = [1]
    last_row = triangle[-1]

    # looping through the last row
    for index in range(len(last_row) - 1):
      next_row.append(last_row[index] + last_row[index + 1])
      
    next_row.append(1)
    # new row is ready
    triangle.append(next_row)
  
  return triangle

for row in pascals_triangle(6):
  print(row)