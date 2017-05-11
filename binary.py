class BinarySearch(list):
    def __init__(self, length, step):
        super(BinarySearch, self).__init__()

        
        for i in range(1, length+1):
            self.append(i * step)

        
        self.length = len(self)

    def search(self, val):
        first = 0
        last = len(self) - 1
        value_index = 0
        found = False

    
        count = 0

        
        if val == self[first]:
            value_index = first
            found = True
        elif val == self[last]:
            value_index = last
            found = True

        
        if val not in self:
            found = True
            value_index = -1

         
        while first <= last and not found:
            mid = (first + last) // 2
            if self[mid] == val:
                found = True
                value_index = mid
            else:
                count += 1 
                if val < self[mid]:
                    last = mid - 1
                else:
                    first = mid + 1

        return {'count': count, 'index': value_index}