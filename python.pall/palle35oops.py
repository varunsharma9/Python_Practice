class Institute:
  def engineering_dept(self,head,manager):
    print(f"{head} is the head of the companys engineering dept , and {manager} is manager of it.\n")

  def hd_dept(self,head,manager):
    print(f"{head} is the head of the companys hd dept , and {manager} is manager of it.\n")
  
  def accounts_dept(self,head,manager):
    print(f"{head} is the head of the companys accounts dept , and {manager} is manager of it.\n")  

  def placement_dept(self,head,manager):
    print(f"{head} is the head of the companys placement dept , and {manager} is manager of it.")
    
i = Institute()
i.engineering_dept('Rakesh','pawan')
i.hd_dept('tarun','tilak')
i.accounts_dept('deepti','silaka')
i.placement_dept('lenin','sidman')