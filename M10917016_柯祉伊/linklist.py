# 節點
class Node:
    # 初始化
    def __init__(self,val):
        self.val = val
        self.next = None
        # if(isinstance(next,Node)):
        #    self.next = next
        # else:
        #     print("Error!Your next value type error!")
class LinkList:
    # 初始化
    def __init__(self):
        self.head = None #head 的型態是Node
    # 新增head
    def add(self,val):
        h = Node(val)
        h.next = self.head
        self.head = h
    # 查看head是否為空值
    def is_empty(self):
        if(self.head==None):
            return True
        else:
            return False
    # 新增Node在最後面
    def append(self,val):
        if(self.is_empty()):
            self.add(val)
        else:
            cont = self.head
            while(cont.next !=None):
                cont = cont.next
            cont.next = Node(val)
    def travel(self):
        if(self.is_empty()==False):
            copyhead = self.head
            while(copyhead.next!=None):
                print(copyhead.val)
                copyhead = copyhead.next
            print(copyhead.val)
        else:
            print("No Vaule")
    # 找尋與Value相同的前一個Node節點(程式錯誤)
    def searchB1(self,val):
        copyhead = self.head
        if(copyhead.next != None):
            while(copyhead.next.val != val):
                copyhead = copyhead.next
            return copyhead
        else:
            print('Not found this node.')
    # 在index的位置新增數值(未設立防呆)
    def insert(self,index,val):
        calInd = 0
        copyhead = self.head
        while(calInd != index):
            calInd=calInd+1
            copyhead = copyhead.next
        if(calInd == 0):
            self.add(val)
        else:
            h = Node(val)
            b1 = self.searchB1(copyhead.val)
            h.next= copyhead
            b1.next = h
    # 搜尋value數值相同的 Node 
    def search(self,val):
        copyhead = self.head
        while(copyhead.val !=val):
            copyhead = copyhead.next
        return copyhead
    #   刪除(bug 當head被刪除時)
    def delete(self,val):
        pos = self.search(val)
        copyhead = self.head
        while(copyhead.next.val != pos.val):
            copyhead = copyhead.next
        copyhead.next = copyhead.next.next
lin = LinkList()
lin.add(2)
