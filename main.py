##################################################
'''
Q1: 
'''

# TODO: Write your code here
sample_dict = {
       "name": "Hermione",
       "marks": {
           "transfiguration": 90,
           "charms": 98,
           "potions": 98,
           "history of magic": 92,
       }
   }
print(sample_dict['marks']['history of magic'])

##################################################
'''
Q2:
'''

# TODO: Write your code here
sample_dict = {
        'emp1': {'name': 'Jhon', 'salary': 7500},
        'emp2': {'name': 'Emma', 'salary': 8000},
        'emp3': {'name': 'Brad', 'salary': 500}
}
sample_dict['emp3']['salary'] = 8500
print(sample_dict)

##################################################
'''
Q3:
'''

# TODO: Write your code here
mystery_pokemon = {
        "height": 15,
        "weight": 405,
        "moves": [
            {
                "name": "lick",
                "level_learned_at": 0
            },
            {
                "name": "nightmare",
                "level_learned_at": 0
            },
            {
                "name": "curse",
                "level_learned_at": 16
            }
        ]
    }

move_list = mystery_pokemon['moves']

for move in move_list:
    if move['name'] == "curse":
        print(move["level_learned_at"])

    

##################################################
'''
Q4:
'''

# TODO: Write your code here

student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco" : 74 ,
    "Nevill" : 62
}


##################################################
'''
Q5a:
'''

# TODO: Write your code here
for key, val in student_scores.items():
    print(f'{key}: {val}')

##################################################
'''
Q5b:
'''

# TODO: Write your code here
min_student = ''
min_score = 100

for key, val in student_scores.items():
    if val < min_score:
        min_student = key
        min_score = val

print(min_student)

    
##################################################
'''
Q6:
'''

# TODO: Write your code here
student_grades = {}
for key, val in student_scores.items():
    if val > 90:
        student_grades[key] = "Outstanding"
    elif val > 80:
        student_grades[key] = "Exceeds Expectations"
    elif val > 70:
        student_grades[key] = "Acceptable"
    else:
        student_grades[key] = "Fail"

print(student_grades)
    


##################################################
'''
Q7:
'''

# TODO: Write your code here
keys = ["Harry", "Ron", "Hermione"]
values = ['B', 'C', 'A']

grades= {}
for i in range (len(keys)):
    key = keys[i]
    val = values[i]
    grades[key] = val



print(grades)
##################################################
