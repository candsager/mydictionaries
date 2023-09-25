# Below is a dictionary that contains information about real estate space for
# a doctor's office. Using the dictionary, create a csv file that has details
# for each space represented as rows. Name your file 'retail_space.csv.


'''
Your final output should look like:

room-number,use,sq-ft,price
100,reception,50,75
101,waiting,250,75
102,examination,125,150
103,examination,125,150
104,office,150,100

'''
import csv 
outfile = open('retail_space.csv', 'w')
outfile.write('Room-number, use, sq-ft, price\n')


datastore = { "medical":[
      { "room-number": 100,
        "use": "reception",
        "sq-ft": 50,
        "price": 75
      },
      { "room-number": 101,
        "use": "waiting",
        "sq-ft": 250,
        "price": 75
      },
      { "room-number": 102,
        "use": "examination",
        "sq-ft": 125,
        "price": 150
      },
      { "room-number": 103,
        "use": "examination",
        "sq-ft": 125,
        "price": 150
      },
      { "room-number": 104,
        "use": "office",
        "sq-ft": 150,
        "price": 100
      }

      ]
}

for record in datastore["medical"]:
    room = record['room-number'],record['use'],record['sq-ft'],record['price']

    outfile.write(f"{room}\n") 
outfile.close()
  

#JOHNNY'S 
#outfile /.....
#outfile.write....
# list_of_dict = datastore["medical"]
# for a_dict in list_of_dict:
#   room = a_dict['room-number']
#   use = a_dict['use']
#   sqft = a_dict['sq-ft']
#   price = a_dict['price']
#   outfile.write(f"{room},{use},{sqft},{price}\n")
# outfile.close()  