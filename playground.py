def run(child):
    return child + " ran as fast as they could for 30 seconds!"

def slide(child):
    return child + " climbed up the slide and bravely slid back down without needing a push. I'm so proud of " + child

def swing(child):
    return "For the first time, " + child + " swung without assistance today."

def hide_and_seek(child):
    return child + " played Hide and Seek with three other kids."

# the goal is to make functions that represent "doing these activities"
# and then to iterate over the lists so that each child in the corresponding list
# is recorded as having done the activity.

running_kids = ["Pam", "Sam", "Andrea", "Will"]
swinging_kids = ["Marybeth", "Jenna", "Kevin", "Courtney"]
sliding_kids = ["Mike", "Jack", "Jennifer", "Earl"]
hiding_kids = ["Henry", "Heather", "Hayley", "Hugh"]

for i in running_kids:
    print(run(i))

for i in swinging_kids:
    print(swing(i))

for i in sliding_kids:
    print(slide(i))

for i in hiding_kids:
    print(hide_and_seek(i))