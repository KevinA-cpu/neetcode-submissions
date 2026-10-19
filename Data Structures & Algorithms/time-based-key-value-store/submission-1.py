class TimeMap:

    def __init__(self):
        self.hash={}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        index = (key, timestamp)
        self.hash[index] = value


    def get(self, key: str, timestamp: int) -> str:
        index = (key,timestamp)
        if index in self.hash:
            return  self.hash[(key,timestamp)]
        else:
            temp = timestamp - 1
            while temp >= 0:
                index = (key,temp)
                if index in self.hash:
                    return self.hash[index]
                temp -= 1
        return ""