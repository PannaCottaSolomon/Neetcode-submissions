from collections import defaultdict

class TimeMap:
    # {
    #     "alice": {
    #         1: "happy",
    #         3: "sad",
    #     }
    # }

    def __init__(self):
        store = defaultdict(dict)
        self.store = store        

    def set(self, key: str, value: str, timestamp: int) -> None:
        currItems = self.store[key]
        currItems[timestamp] = value
        self.store[key] = currItems

    def get(self, key: str, timestamp: int) -> str:
        # print(self.store)
        timings = self.store[key]
        answer = self.binarySearch(timings, timestamp)
        return answer

    def binarySearch(self, timings: dict, timestamp: int) -> str:
        keys = list(timings.keys())
        l = 0
        r = len(keys) - 1
        ans = ""
        while l <= r:
            m = (l + r) // 2
            if keys[m] <= timestamp:
                ans = timings[keys[m]]
                l = m + 1
            else:
                r = m - 1

        return ans
            
        


