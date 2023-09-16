class Bank:
  def __init__(self,Bankname , Branchname , Branchcode):
    self.Bankname = Bankname
    self.Branchname = Branchname
    self.Branchcode = Branchcode

class Costumer(Bank):
  def __init__(self,costumername,accno,bankbalance,Bankname,Branchname,Branchcode):
    self.costumername = costumername
    self.accno = accno
    self.bankbalance = bankbalance
    super().__init__(Bankname , Branchname , Branchcode)
  def display (self):
    print(self.costumername)
    print(self.accno)  
    print(self.bankbalance)  
    print(self.Bankname)  
    print(self.Branchname)  
    print(self.Branchcode)  
child = Costumer("varun",2352524243,30000,"centralbank","idinagar",4314)
child.display()
