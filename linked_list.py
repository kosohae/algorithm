__author__ = "SanheePark"
__version__ = 1.0

# Linked List node 구현
class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None
    
class NodeControl(object):
    def __init__(self):
        self.head_list = []
        self.head_cnt = 0

    def insert_last(self, idx, val):
        if not self._check(idx):
            print("Idex over Head count")
            return

        idx_head = self.head_list[idx] 
        tmp = idx_head
        while tmp.next:
            tmp = tmp.next
            
        tmp.next = Node(val)

    def insert_sort(self, idx, val):
        if not self._check(idx):
            print("Idex over Head count")
            return
            
        idx_head = self.head_list[idx]
        prev = None
        cur = idx_head

        if val < cur.val:
            self.insert_first(idx, val)

        else:
            while cur:
                if val < cur.val:
                    prev.next = Node(val)
                    prev.next.next = cur
                    break
                prev = cur
                cur = cur.next

            if cur is None:
                self.insert_last(idx, val)


        # middle, last insert => node가 보통 큰 경우, 사이에 끼는 경우 
        # 새로 들어오는 node가 제일 작은 경우 => head가 새롭게 만들어져야하고 이게 head list에 반영되어야 함.
    def insert_first(self, idx, val):
        if not self._check(idx):
            print("Idex over Head count")
            return

        idx_head = self.head_list[idx] 
        tmp = None
        tmp = Node(val)
        
        tmp.next = idx_head
        self.head_list[idx] = tmp
        
    def delete_last(self, idx):
        if not self._check(idx):
            print("Idex over Head count")
            return

        if self.head_cnt == 0:
            print("Delete error, empty head list")
            return
           
        if self.head_list[idx].next is None:
            #self.head_list[idx] = None
            self.head_list.pop(idx)
            return 

        # delete last node
        head = self.head_list[idx]
        prev = None
        cur = head
        while True:
            prev = cur
            cur = cur.next
            if cur is None:
                break

        prev.next = None
    
    def delete_first(self, idx):
        # delete last node
        if self.head_list[idx].next is None:
            self.head_list.pop(idx)
        else:
            self.head_list[idx] = self.head_list[idx].next

    def serach(self, idx, val):
        if not self._check(idx):
            print("Idex over Head count")
            return

        cur = self.head_list[idx]
        while cur:
            if cur.val == val:
                return True
            cur = cur.next
        
        return False

    def create(self, val):
        self.head = Node(val)
        self.head_list.append(self.head)
        self.head_cnt += 1

    def _check(self, idx):
        # boundary check
        if idx >= self.head_cnt:
            return False
        return True

    def _print(self, idx):
        if not self._check(idx):
            print("Idex over Head count")
            return
        head = self.head_list[idx]
        while head:
            print(head.val)
            head = head.next


if __name__ == '__main__':
    obj = NodeControl()
    # head 처음 만들고 list에 추가
    obj.create(1)
    obj.insert_last(0, 2)
    obj.insert_last(0, 5)
    obj.insert_last(0, 4)

    obj.create(2)
    obj.insert_last(1, 3)
    obj.insert_last(1, 2)

    obj.create(3)
    obj.insert_sort(2,6)
    obj.insert_sort(2,7)
    obj.insert_sort(2,5)
    obj.insert_sort(2,1)
    obj._print(2)

    try:
        # error test
        obj.delete_last(5)
    except IndexError as e:
        print(str(e))

    # print(obj.head_list)
    #obj.delete(2)

    # search test
    if obj.serach(3,4):
        print("exist")
    else:
        print("don't exist")

    #obj._print(3)
    #obj.delete_first(3)

