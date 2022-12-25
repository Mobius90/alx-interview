#!/usr/bin/python3
'''n,k = n-1,k-1 + n-1,k'''


def pascal_triangle(n):
        if(n == 0):
            return []
        triangle = [[1]]
        for n in range(1, n):
            thisRow = []
            thisRow.append(1)
            for k in range(1, n):                
                thisRow.append(triangle[n-1][k-1] + triangle[n-1][k])
            thisRow.append(1)
            triangle.append(thisRow)
        return triangle
