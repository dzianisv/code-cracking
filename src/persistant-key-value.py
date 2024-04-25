# design a single machine KV store that’s durable.
# pseudo code is fine 

# how will you use it?
#     - a single machine program read from/write to import
# if the program restart, will the db be wiped or kept?
#     - kept
# do you need multi thread or single thread
#     - multi thread
# what does durable mean? 
#  - what do you think durable should cover
#       - persistent
# are key/v integer/string
#       - can be anything
# do you think json is efficient?
#   - no, use pickle
# what if there're remove and overwrite needs?
#

import json
import os

# 1. in-memory
# 2. file-persistance, naive
# 3. a) file per key, "foo", .store/foo, 
# 3. b) levelDB key-value DB

class Store:
    def __self__(self, file_store='store.json'):
        self.file_store = file_store
        self._load()

    def _dump(self):
        with open(self.file_store, "wb") as f:
            json.dump(self.store, f)
    
    def _load(self):
        if os.path.exists(self.file_store):
            with open(self.file_store, "rb") as f:
                self.store = json.load(f)
        else:
            self.store = dict()
    
    def setValue(self, key, value):
        self.store[key] = value
        self._dump()
    
    def getValue(self, key):
        if key not in self.store:
            raise KeyError(f"not such key {key}")
        return self.store[key]


import typing
import pickle
# [0]: type, string, float, integer, boolean
# [1-4]: size
# [5+]: data
# [a 128bytes]:[1024 bytes]
# [b 128bytes]:[1024 bytes]
# [c 128bytes]:[1024 bytes]
# [d 128bytes]:[1024 bytes]

class Store2:
    def __self__(self, store_dir='store'):
        self.store_dir = store_dir
        self._load()
        self.max_files = 1024

    def _get_value_file(self, key: typing.Any) -> str:
        # todo: check collisions
        # how to name files?
        # a) str(type(key)) + str(key)
        # b) str(hash(key))
        # question: is `hash` is reliable, collisions? 
        return os.path.join(self.store_dir, str(hash(key) % self.max_files))

    def _dump(self, key: typing.Any, value: typing.Any):
        # hash(a) -> 1
        # hasb(b) -> 1
        # ./store/1
        # open(./store/1).read() = {a: value, b: bVaule}
        file_path = self._get_value_file(key)
        key_value_hashmap = dict()

        if os.path.exists(file_path):
            with open(file_path, "wb") as fp:
                key_value_hashmap = pickle.load(fp)
        
        key_value_hashmap[key] = value
        with open(file_path, "wb") as fp:
            pickle.dump(key_value_hashmap, fp)

    def _load(self):
        if os.path.exists(self.store_dir):
            for (dirpath, dirnames, filenames) in os.walk(self.store_dir):
                for file_name in filenames:
                    with open(file_name, 'rb') as f:
                        key_value = pickle.load(f)
                        self.store[key_value.key] = key_value.value
        else:
            self.store = dict()
    
    def setValue(self, key, value):
        self.store[key] = value
        self._dump(key, value)
    
    def getValue(self, key):
        if key not in self.store:
            raise KeyError(f"not such key {key}")
        return self.store[key]

    def deleteValue(self, key: typing.Any):
        if key in self.store:
            del self.store
        
        key_value_file = self._get_value_file(key)

        if os.path.exists(key_value_file):
            os.unlink(key_value_file)
    