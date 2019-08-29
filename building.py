import datetime

class Building:
    def __init__(self, address, stories):
        self.designer = "Melanie Bond"
        self.date_constructed = ""
        self.owner = ""
        self.address = address
        self.stories = stories

    def construction(self):
        self.date_constructed = datetime.date.today()
    
    def purchase(self, purchaser):
        self.owner = purchaser

    def print_details(self):
        print(f"On {self.date_constructed}, {self.owner} purchased the building at {self.address} that is {self.stories} tall!")
# Create 5 building instances
# Have each one get purchased by a real estate magnate
# After purchased, construct each one
# Once all building are purchased and constructed, print the address, owner, stories, and date constructed to the terminal for each one.

seven_hundred_twelfth = Building("700 12th Ave S", 20)
seven_hundred_twelfth.construction()
seven_hundred_twelfth.purchase("Market Street")
seven_hundred_twelfth.print_details()


# import datetime

# format = "%a %b %d %H:%M:%S %Y"

# today = datetime.datetime.today()
# print 'ISO     :', today

# s = today.strftime(format)
# print 'strftime:', s

# d = datetime.datetime.strptime(s, format)
# print 'strptime:', d.strftime(format)
# $ python datetime_datetime_strptime.py

# ISO     : 2013-02-21 06:35:45.707450
# strftime: Thu Feb 21 06:35:45 2013
# strptime: Thu Feb 21 06:35:45 2013

# def construction(self):
#         format = "%d %b %Y"
#         self.date_constructed = date
#         date = datetime.date.today()
#         date.strftime(format)