#!/usr/bin/python3

"""Creates a function."""


def pascal_triangle(n):
    """func  that returns a list of lists of integers of Pascal Triangle."""
    if n <= 0:
        """if n is less than 0, return empty string."""
        return []
    else:
        triangle = [[1]]
        for i in range(1, n):
            """calculates the values based on the previous row."""
            prev_row = triangle[i-1]
            new_row = [1]
            for j in range(1, i):
                new_row.append(prev_row[j-1] + prev_row[j])
            new_row.append(1)
            triangle.append(new_row)
    return triangle
