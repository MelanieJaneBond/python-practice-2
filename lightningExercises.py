eye_colors = [
  {
    "color": "brown"
  },
  {
    "color": "green"
  },
  {
    "color": "amber"
  },
  {
    "color": "blue"
  },
  {
    "color": "amber"
  },
  {
    "color": "amber"
  },
  {
    "color": "brown"
  },
  {
    "color": "amber"
  },
  {
    "color": "brown"
  },
  {
    "color": "brown"
  },
  {
    "color": "purple"
  },
  {
    "color": "purple"
  },
  {
    "color": "blue"
  },
  {
    "color": "blue"
  },
  {
    "color": "brown"
  },
  {
    "color": "amber"
  },
  {
    "color": "amber"
  },
  {
    "color": "green"
  },
  {
    "color": "green"
  },
  {
    "color": "green"
  },
  {
    "color": "brown"
  },
  {
    "color": "amber"
  },
  {
    "color": "brown"
  },
  {
    "color": "amber"
  },
  {
    "color": "blue"
  },
  {
    "color": "blue"
  },
  {
    "color": "green"
  },
  {
    "color": "green"
  }
]

#create a new collection that contains the unique color names in the list above

unique_colors = set()

for color_dict in eye_colors:
    #look at this^ the "color_dict" is DECLARED inside the function
    #it's separated out, then, as a dictionary within the 
    current_color = color_dict["color"]
    unique_colors.add(current_color)

print(unique_colors)

# 2. Create a new collection that stores the unique color names AND how many
# times each one is in the list

color_table = {}

for color_dict in eye_colors:
    current_color = color_dict["color"]

    if current_color not in color_table:
        color_table[current_color] = 1
    else:
        color_table[current_color] += 1

#a new exercise for the morning:
appliances = (["oven", "refrigerator", "coffee maker", "rice cooker"])
# Add 3 indispensable appliances to this tuple

appliances.append(["toaster", "sink", "trash compactor"])
#the above was the method I tried, but I think I basically made it a list
#which isn't "keeping it a tuple" and is more confusing than "making it a set"
#as some people did... TUPLES ARE IMMUTABLE but they can contain nested objects
#and the objects inside the tuples are not immutable.
# print(appliances)

appliancesTuple = ("oven", "refrigerator", "coffee maker", "rice cooker")
otherTuple = appliancesTuple + ("toaster", "sink", "trash compactor")
#this one was discovered by Danny, it's very cool and clear to me
print(otherTuple)

appliances_joe = ("oven", "refrigerator", "coffee maker", "rice cookier")
appliances_joe = set(appliances_joe)
appliances_joe.update(["dishwasher", "microwave", "toaster oven"])
appliances_joe = tuple(appliances_joe)
print(appliances_joe)

appliances_jake = ("oven", "refrigerator", "coffee maker", "rice cookier")
appliances_jake += ("stuff",)
#this method was discovered by Jake. I don't understand it, the teaching team
#explained it, but, I'm a little fuzzy.
print(appliances_jake)