'''Design a time-based key-value data structure that can store multiple values for the same key at different time stamps and retrieve the key's value at a certain timestamp.

Implement the TimeMap class:

TimeMap() Initializes the object of the data structure.
void set(String key, String value, int timestamp) Stores the key key with the value value at the given time timestamp.
String get(String key, int timestamp) Returns a value such that set was called previously, with timestamp_prev <= timestamp. If there are multiple such values, it returns the value associated with the largest timestamp_prev. If there are no values, it returns "".'''

class TimeMap:

    def __init__(self):

        self.store = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        
        if key in self.store.keys():
            self.store[key].append((timestamp,value))
        else:
             self.store[key] = [(timestamp,value)]

    def get(self, key: str, timestamp: int) -> str:
        
        if key not in self.store.keys():
            return ""

        valueList = self.store[key]

        left  = 0
        right = len(valueList) - 1

        while left <= right:

            if timestamp < valueList[left][0]:
                return ""

            if valueList[right][0] <= timestamp:
                return valueList[right][1]

            if valueList[left][0] == timestamp:
                return valueList[left][1]

            if left + 1 == right or left == right:
                if valueList[right][0] <= timestamp:
                    return valueList[right][1]
                else:
                    return valueList[left][1]

            middle = int((left+right)/2)

            if valueList[middle][0] > timestamp:
                right = middle
            elif valueList[middle][0] < timestamp:
                left = middle
            else:
                return valueList[middle][1] 


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
