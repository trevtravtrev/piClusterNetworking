import math
import json
import server

class ClusterMessage:
    def __init__(self, ):
        pass


    def split_list(self, lst):
        if isinstance(lst, list):
            messages = []
            items_per_list = math.ceil(len(lst) / len(self.clients))

            try:
                for i in range(0, len(lst), items_per_list):
                    messages.append(lst[i: i + items_per_list])
                return messages

            except:
                print("Error: list splitting failed.")
        else:
            print("Error: data is not type list.")

    def split_str(self, string):
        pass

    def split_dict(self, dictionary):
        pass

    def create_server_message(self, data):
        pass

    def create_client_message(self, data):
        pass


def serialize_data(data):
    return json.dumps(data).encode()  # json.dumps turns any data into string, .encode turns string into bytes

def deserialize_data(serialized_data):
    return json.loads(serialized_data.decode()) # .decode turns bytes into string, json.loads turns string back into original data type (dict, list, etc)
