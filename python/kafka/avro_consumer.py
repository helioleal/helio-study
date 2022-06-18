'''
When kafka is online in local server, this program consumes everything
from a topic called impacta_project
This is a test to consume data in bytes using a AVRO schema.
'''
from kafka import KafkaConsumer
import io
from avro.io import DatumReader, DatumWriter, BinaryEncoder, BinaryDecoder

import io
import avro.schema
import avro.io

def decode(raw_bytes):
    # Schema example 
    schema_value = '''{
        "namespace": "customer.avro",
        "type": "record",
        "name": "Customer",
        "fields": [     
            {"name": "id",  "type": ["int", "null"]},
            {"name": "agency", "type": "string"},
            {"name": "operation_value", "type": ["double", "null"]},
            {"name": "type", "type": ["int", "null"]},
            {"name": "date", "type": "string"},
            {"name": "account_balance", "type": ["double", "null"]}
        ]
        }
        '''
    schema = avro.schema.parse(schema_value)
    bytes_reader = io.BytesIO(raw_bytes)
    decoder = BinaryDecoder(bytes_reader)
    reader = DatumReader(schema)
    result = reader.read(decoder)   
    return result

consumer = KafkaConsumer('impacta_project')
for msg in consumer:
    result = decode(msg.value)
    print(result)

