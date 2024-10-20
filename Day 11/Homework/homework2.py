# მაგალითი 1
result1 = True and True
print(result1)  # შედეგი: True

# მაგალითი 2
result2 = True and False
print(result2)  # შედეგი: False

# მაგალითი 3
result3 = False and True
print(result3)  # შედეგი: False

# მაგალითი 4
result4 = False and False
print(result4)  # შედეგი: False

# მაგალითი 5 (არასრული)
x = 5
result5 = (x > 3) and (x < 10)
print(result5)  # შედეგი: True, რადგან 5 უფრო დიდი 3-ზე და პატარა 10-ზე




# მაგალითი 1
result1 = True or True
print(result1)  # შედეგი: True
# რადგან ორივე operand არის True, შედეგად არის True.

# მაგალითი 2
result2 = True or False
print(result2)  # შედეგი: True
# რადგან ერთი operand (True) არის True, შედეგად არის True.

# მაგალითი 3
result3 = False or True
print(result3)  # შედეგი: True
# რადგან ერთი operand (True) არის True, შედეგად არის True.

# მაგალითი 4
result4 = False or False
print(result4)  # შედეგი: False
# რადგან ორივე operand არის False, შედეგად არის False.

# მაგალითი 5
x = 2
result5 = (x > 3) or (x < 5)
print(result5)  # შედეგი: True
# რადგან მეორე operand (x < 5) არის True (2 უფრო პატარაა 5-ზე), შედეგად არის True.

# მაგალითი 6
y = 10
result6 = (y < 5) or (y > 15)
print(result6)  # შედეგი: False
# რადგან არც ერთი operand არ არის True, შედეგი არის False.

# მაგალითი 7
z = 7
result7 = (z == 7) or (z == 10)
print(result7)  # შედეგი: True
# რადგან პირველი operand (z == 7) არის True, შედეგად არის True.

