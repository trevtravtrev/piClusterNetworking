import math
import json

def split_list(lst, num_clients):
    if isinstance(lst, list):
        split_data = []
        items_per_list = math.ceil(len(lst) / num_clients)

        try:
            for i in range(0, len(lst), items_per_list):
                split_data.append(lst[i: i + items_per_list])
                
            return split_data

        except Exception as e:
            print(f'split_list error: {e}')
    else:
        print("Error: data is not type list.")

def split_str(string):
    pass

def split_dict(dictionary):
    pass

def create_message(function, data = None):
    try:
        # json.dumps turns any data into string, .encode turns string into bytes
        return serialize_data({function: data})
        
    except Exception as e:
        print(f'create_message error: {e}')

def deserialize_data(data):
    # .decode turns bytes into string, json.loads turns string back into original data type (dict, list, etc)
    try:
        return json.loads(data.decode())
        
    except Exception as e:
        return print(f'deserialize_data error: {e}')
        
def serialize_data(data):
    try:
        return json.dumps(data).encode()
        
    except Exception as e:
        return print(f'serialize_data error: {e}')

