class Seanimals:
    def __init__(self,name,caneat,danger):
        self.name = name
        self.caneat = caneat
        self.danger = danger
      
    def introduction(self):
      print("こいつの名前は" + self.name + "です。　そして、これは食うことが" + self.caneat)
      
    def dangers(self):
      print("この生き物は" + self.danger)
  
Shark = Seanimals("ホオジロザメ","できます","あぶなあい")
Iruka = Seanimals("シロイルカ","できません","あぶなくなあい")
Maguro = Seanimals("本マグロ","できます","あぶなくなあい")
Shark.introduction()
Shark.dangers()

Iruka.introduction()
Iruka.dangers()

Maguro.introduction()
Maguro.dangers()

class Nobone(Seanimals):
  def __init__(self,name,caneat,danger,nobone):
    super().__init__(name,caneat,danger)
    self.nobone = nobone
  def introduction(self):
    print("こいつの名前は" + self.name + "です。　そして、これは食うことが" + self.caneat)
  def dangers(self):
    print("この生き物は" + self.danger)
  def Nobone(self):
    print("この生き物は骨が" + self.nobone + "です。")

Tako = Nobone("ミズタコ","できます","あぶなくなあい","ない")
Ika = Nobone("スルメイカ","できます","あぶなくなあい","ない")

Tako.introduction()
Tako.dangers()
Tako.Nobone()

Ika.introduction()
Ika.dangers()
Ika.Nobone()

class Nofish(Nobone):
  def __init__(self,name,caneat,danger,nobone,nofish):
    super().__init__(name,caneat,danger,nobone)
    self.nofish = nofish
  def introduction(self):
    print("こいつの名前は" + self.name + "です。　そして、これは食うことが" + self.caneat)
  def dangers(self):  
    print("この生き物は" + self.danger)
  def Nobone(self):
    print("この生き物は骨が" + self.nobone + "です。")
  def Nofish(self):
    print("この生き物は魚では" + self.nofish + "です。")

Kame = Nofish("カメ","できません","あぶなくなあい","あるん","ない")

Kame.introduction()  
Kame.dangers()
Kame.Nobone()
Kame.Nofish()
