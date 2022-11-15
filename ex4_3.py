class Node:
   def __init__(self, dataval=None):
      self.dataval = dataval
      self.nextval = None

class SLinkedList:
    def __init__(self):
        self.headval = None
    def listprint(self):
      printval = self.headval
      while printval is not None:
         print (printval.dataval ,end = "->")
         printval = printval.nextval
    def AtBegining(self,newdata):
        NewNode = Node(newdata)
# Update the new nodes next val to existing node
        NewNode.nextval = self.headval
        self.headval = NewNode
    def AtEnd(self, newdata):
        NewNode = Node(newdata)
        if self.headval is None:
            self.headval = NewNode
            return
        laste = self.headval
        while(laste.nextval):
            laste = laste.nextval
        laste.nextval=NewNode
    def RemoveNode(self, Removekey):
        HeadVal = self.headval  
        if (HeadVal is not None):
            if (HeadVal.dataval == Removekey):
                self.head = HeadVal.nextval
                HeadVal = None
                return
        while (HeadVal is not None):
                if HeadVal.dataval == Removekey:
                    break
                prev = HeadVal
                HeadVal = HeadVal.nextval

        if (HeadVal == None):
            return
        prev.nextval = HeadVal.nextval
        HeadVal = None


linklist = SLinkedList()
linklist.headval = Node(44)
newNode1 = Node(36)
newNode2 = Node(90)
newNode3 = Node(10)
newNode4 = Node(60)
newNode5 = Node(99)

linklist.headval.nextval = newNode1
newNode1.nextval = newNode2
newNode2.nextval = newNode3
newNode3.nextval = newNode4
newNode4.nextval = newNode5
linklist.AtBegining(104)
linklist.AtEnd(57)
linklist.RemoveNode(10)
linklist.listprint()