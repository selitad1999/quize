#Instruction: choose the correct ansewr for each question

Q1="""The maximum accomudation of electron in M shell is ?

A.18    B.32    C.8    D.50  """

Q2="""The number of cycles that the wave undergoes persecond is ?   

A.Wave length    B.Frequency    C.Speed    D.Work function  """

Q3="""When n=3,l=  ?

A.0,1,2,3    B.0,1,2    C.-1,0,1    D.-2,-1,0,1,2  """

Q4="""The element Cl,F,At,Br,I then which is the correct order according to decreasing electronegativity ?

A.F,Cl,Br,I,At    B.At,I,Br,Cl,F    C.I,F,Cl,At,Br    D.F,Cl,At,I,Br  """

Q5="""If a point p has the coordinate (5,2), then which one is its reflection about the line y=-x ?

A.(5,-2)    B.(-5,2)    C.(-2,-5)    D.(2,5)  """

Q6="""what is the area of the triangle with vectices (1,0),(1,2), and (3,2) ?

A.2 Sq. unit   B.3 Sq. unit   C.4 Sq. unit   D.All  """

Q7="""If a triangle takes (7,2) to the point (5,3), the what is the image of line y=2x-3 ?

A.Y=X+2    B.Y=3X+3   C.Y=2X-2  D.Y=2X+2  """
 
Q8="""wchih one of the following is the image of a point (3,5) reflected by the y=0 or x_axis 

A. (-3,5)   B.(3,-5)     C.(-3,-5)   D.(3,5)  """

Q9="""Which of the following is vector quanrtity ?
 
 A.Distance   B.Electric field   C.Temperature   D.Density  """

 Q10="""The coponent of vector A is given as Ax=10 & Ay=15, what is the magnitude of vector A

 A,10   B.16.02   C.18.02   D.15.02  """

 Q11="""What is the result of adding a vector to the negative of it self ?

 A.Unit vector  B.Null(zero vector)   C.Parallel vector   D.Orthogonal vector  """

 Q12="""The force of attraction between any two objects is referred as__
 
 A.Average speed   B.Gravity   C.Force   D.Acceleration  """

 Q13="""What is enzyme kinetics ?

 A.The reat of reaction   B.Bone reaction   C.Heat reaction   D.Acidic reaction   """

 Q14="""Vasodilation to increase heat loss, while___to reatin haet.

 A.Enzyme   B.Temperature   C.Vasoconstriction   D.B & C are correct  """

 Q15="""Designing technology from nature is through

 A.Drawing   B.Photograph   C.Sketching   D.Imitaion  """

 Q16="""Which one is primary producera & feeders for living organisms ?

 A.Plants   B.Biology   C,Plants & animals   D.Technology  """

 Q17="""I sleep during the day and my active__night.

 A.At   B.In   C.On   D.With  """

 Q18="""It is time for me to play__mama.
 
 A.To   B.At   C,With   D,On  """

 Q19="""Even the kind of the village could swim__him.

 A.For   B.In   C.By   D.Around  """

 Q20="""People keep unusual pets__pleasure

 A.About   B.For   C.On   D.By  """

 Q21="""Which blood cell fight infection ?

 A.Red bload cells   B.Platelets   C.White bload cells   D.Plasma  """

 Q22="""Which subatomic particle has a negative charge ?

 A.Proton   B.Neutron   C.Electron   D.Nucleus  """

 Q23="""What is the si unit of force ?

 A.Joule  B.Newton   C.Watt   D.Pascal  """

 Q24="""If 7x = 84, x = ?

 A.10   B.11   C.12   D.13  """

 Q25="""What is 25 * 4 ?

 A.75   B.100   C.125   D.150  """

 questions  = {
    Q1:'A', Q2:'B', Q3:'B', Q4:'A',Q5:'C', Q6:'A', Q7:'D', Q8:'B', Q9:'B', Q10:'C', Q11:'B',
    Q12:'B', Q14:'C', Q15:'D', Q16:'C', Q17:'B', Q18:'A', Q19:'C', Q20:'B', Q21:'C', Q22:'C', Q23:'B', Q24:'C', Q25:'B' 
    } 
print("welcome to general quiz ")
name = input("enter your full name")
print(f"dear {name}, welcome to exam hall")
print("please ready carefull the following instraction")
print("instr.1:don't forget to write your full name")
print("instr.2:cheating will nullify your total result")

mark = 0
list = ['a','b','c','d']
for item in questions:
   print(item)
   answer = input("choose tge correct answer a/b/c/d:").lower()

   if answer == questions[item]:
      print(f"{answer} is correct answer,your got 2 point.")
      mark =mark+2
   else:
      print(f"{answer} is incorrect,{questions[item]} is the correct answer")
      mark =mark

   if mark >= 23
      print(f"{mark}/25,exellent")
   elif mark >= 20
      print(f"{mark}/25,v.good")
   elif mark >= 18
      print(f"{mark}/25,good")
   elif mark >= 10
      print(f"{mark}/25,satisfactory")
   elif mark >= 5
      print(f"{mark}/25,failed")