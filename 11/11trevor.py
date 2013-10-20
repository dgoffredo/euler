#!/usr/bin/env python3
from sys import argv

m = argv[1] # int(input('Let m = '))
file = argv[2] # input('filename = ')
data=[line.strip() for line in open(file)]
numbers=[]
prearray=[]
arrayn=[]
array=[]

def product(P):
    X=1
    t=0
    while t < len(P):
        X=P[t]*X
        t = t+1
    return(X)

for x in data:
    numbers.append([x])
for n in range(0, len(numbers)):
    for x in numbers[n]:
        prearray.append(x.split(' '))
n=0
while n in range(0, len(prearray)):
    for x in prearray[n]:
        arrayn.append(int(x))
    array.append(arrayn)
    arrayn=[]
    n=n+1

def maxlistproduct(L,m):
    i=0
    Lproducts=[]
    while i<len(L)-m+1:
        Lproducts.append(product(L[i:i+m]))
        i=i+1
    return sorted(Lproducts)[-1]

def maxrowprod(L, m):
    rowproducts=[]
    i=0
    while i<len(L):
        rowproducts.append(maxlistproduct(array[i],m))
        i=i+1
    return sorted(rowproducts)[-1]

def maxcolumnprod(L, m):
    column=[]
    columnproducts=[]
    j=0
    while j<len(L):
        i=0
        while i<len(L):
            column.append(L[i][j])
            i=i+1
        columnproducts.append(maxlistproduct(column,m))
        column=[]
        j=j+1
    return sorted(columnproducts)[-1]


def maxLRdiagonalproduct(L,m):
    i,j=0,0
    diagonal=[]
    diagonalproduct=[]
    while i<len(L)-m+1:
        k=i
        while k<len(L):
            diagonal.append(L[k][j])
            k,j=k+1,j+1
        diagonalproduct.append(maxlistproduct(diagonal,m))
        diagonal=[]
        i,j=i+1,0
    i,j=0,0
    while j<len(L)-m+1:
        k=j
        while k<len(L):
            diagonal.append(L[i][k])
            i,k=i+1,k+1
        diagonalproduct.append(maxlistproduct(diagonal,m))
        diagonal=[]
        i,j=0,j+1
    return sorted(diagonalproduct)[-1]

def maxRLdiagonalproduct(L,m):
    i,j = m-1,0
    diagonal2=[]
    diagonal2product=[]
    while i < len(L):
        k=i
        while k>=0:
            diagonal2.append(L[k][j])
            k,j=k-1,j+1
        diagonal2product.append(maxlistproduct(diagonal2,m))
        diagonal2=[]
        i,j=i+1,0
    i,j=len(L)-1, 0
    while j<len(L)-m+1:
        k=j
        while k<len(L):
            diagonal2.append(L[i][k])
            i,k=i-1,k+1
        diagonal2product.append(maxlistproduct(diagonal2,m))
        diagonal2=[]
        i,j=len(L)-1, j+1
    return sorted(diagonal2product)[-1]
        
print('') 
print(sorted([maxrowprod(array, m), maxcolumnprod(array, m), maxLRdiagonalproduct(array, m), maxRLdiagonalproduct(array, m)])[-1])
