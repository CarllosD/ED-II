class Tree:
   def __init__(self):
      self.raiz = None

   def inOrdem(self):
      if self.raiz != None: return self.inOrdem()

   #Método para encontrar o nível
   def nivel(self, valor):
      if self.raiz != None: return self.raiz.nivel(valor)
      
   #INSERE NOS NA AVL
   def insere(self, valor):
      if self.raiz == None: self.raiz = No(valor)
      
      else: self.raiz.insere(valor)
      
   #BALANCEIA P/ ESQUERDA QUANDO O FB É POSITIVO
   def balanceia_dir(self):
      if self.raiz != None: return self.raiz.balanceia_dir()

   #BALANCEIA P/ DIREITA QUANDO O FB É NEGATIVO
   def balanceia_esq(self):
      if self.raiz != None: return self.raiz.balanceia_esq()

   def altura(self):
      if self.raiz != None: return self.raiz.altura()

   #CALCULA FB (FATOR DE BALANCEAMENTO) DO NO
   def calcfb(self):
      if self.raiz != None: return self.raiz.calcfb()
      

#################################################################################


class No:
   def __init__(self, valor):
      self.info = valor
      self.esq = None
      self.dir = None
      self.fb = 0

   def insere(self, valor):
      if valor <= self.info:
         if self.esq == None:
            self.esq = No(valor)
            self.fb = self.calcfb()
            print(self.fb)

         else:
            self.esq.insere(valor)
            self.fb = self.calcfb()
            print(self.fb)

      else:
         if self.dir == None:
            self.dir = No(valor)
            self.fb = self.calcfb()
            print(self.fb)
            
         else:
            self.dir.insere(valor)
            self.fb = self.calcfb()
            print(self.fb)

      if self.fb == 2: self.balanceia_esq()

      elif self.fb == -2: self.balanceia_dir()

      elif self.fb * -1 > 2: print("FUDEO!!! -> ",+self.info)

   def balanceia_dir(self):
      q = self
      temp = q.dir
      q.dir = self
      self.esq= temp
      p=q 
      #METE O CÓDIGO AE

   def balanceia_esq(self):
      q = self
      temp = q.esq
      q.esq = self
      self.esq= temp 
      p=q
      #METE O CÓDIGO AE

   def calcfb(self):
      if self.dir != None and self.esq != None: return self.dir.altura() - self.esq.altura()

      else:
         if self.dir == None: return 0 - self.esq.altura()

         else: return self.dir.altura() - 0

   def altura(self):
      esq = dir = 0

      if self.esq != None: esq = self.esq.altura()

      if self.dir != None: dir = self.dir.altura()

      if esq > dir: return esq + 1
      
      else: return dir + 1

   def inOrdem(self):
      if self.esq != None: self.esq.inOrdem()
         
      print(self.info)
      
      if self.dir != None: self.dir.inOrdem()


   def nivel(self, valor):
      ct = 1
      if self.info > valor:
         if self.info == valor:
            return ct
         elif self.esq != None:
            ct += self.esq.nivel(valor) 
      elif self.info < valor:
         if self.info == valor:
            return ct
         elif self.dir != None:
            ct += self.dir.nivel(valor)
      return ct



