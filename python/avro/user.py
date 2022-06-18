'''
This programa reads the avro schema user.avsc with definition of fields and generates new
values for it, store in a json file called users.avro 
and after read it back.
Taken from: https://avro.apache.org/docs/current/gettingstartedpython.html
'''
import avro.schema
from avro.datafile import DataFileReader, DataFileWriter
from avro.io import DatumReader, DatumWriter

schema = avro.schema.parse(open("user.avsc", "rb").read())

writer = DataFileWriter(open("users.avro", "wb"), DatumWriter(), schema)
writer.append({"name": "Alyssa", "favorite_number": 256})
writer.append({"name": "Ben", "favorite_number": 7, "favorite_color": "red"})
writer.close()

reader = DataFileReader(open("users.avro", "rb"), DatumReader())
for user in reader:
    print(user)
    print(user['name'])
    print(user['favorite_number'])
    print(user['favorite_color'])
reader.close()
      