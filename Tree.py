class Tree:
   def __init__(self):
      self.raiz = None

   #IMPRIME TODOS DOS NÓS EM ORDEM
   def inOrdem(self):
      if self.raiz != None: return self.inOrdem()

   #
   def nivel(self, valor):
      if self.raiz != None: return self.raiz.nivel(valor)
      
   #INSERE NÓS NA AVL
   def insere(self,valor):
      if self.raiz == None:
         self.raiz = No(valor)
         print('raiz: {} | FB: {}'.format(self.raiz.info,self.raiz.fb))

      else: self.raiz.insere(valor)
      
   #BALANCEIA P/ ESQUERDA QUANDO O FB É POSITIVO
   def balanceia_dir(self):
      if self.raiz != None: return self.raiz.balanceia_dir()

   #BALANCEIA P/ DIREITA QUANDO O FB É NEGATIVO
   def balanceia_esq(self):
      if self.raiz != None: return self.raiz.balanceia_esq()
      
   #RETORNA A ALTURA DA ÁRVORE
   def altura(self):
      if self.raiz != None: return self.raiz.altura()

   #CALCULA FB (FATOR DE BALANCEAMENTO) DO NO
   def calcfb(self):
      if self.raiz != None: return self.raiz.calcfb()

   #IMPRIME O FB DE TODOS OS NÓS DA ÁRVORE
   def showFb(self):
      if self.raiz != None: self.raiz.showFb()

   #RECEBE O NÓ QUE SE DESEJA BALANCEAR COMO ARGUMENTO
   def balanceia(self, raiz):
      if self.raiz != None: self.raiz.balanceia(raiz)
      

#################################################################################


class No(Tree):
   def __init__(self, valor):
      self.info = valor
      self.esq = None
      self.dir = None
      self.fb = 0

   def showFb(self):
      if self.esq != None: self.esq.showFb()
      
      print('Nó:  {} | FB: {}'.format(self.info, self.fb))
      
      if self.dir != None: self.dir.showFb()

   def insere(self, valor):
      if valor <= self.info:
         if self.esq == None:
            self.esq = No(valor)
            self.fb = self.calcfb()
            #print('arvore: {}, FB: {}'.format(self.info,self.fb))

         else:
            self.esq.insere(valor)
            self.fb = self.calcfb()
            #print('arvore: {}, FB: {}'.format(self.info,self.fb))

      else:
         if self.dir == None:
            self.dir = No(valor)
            self.fb = self.calcfb()
            #print('arvore: {}, FB: {}'.format(self.info,self.fb))
            
         else:
            self.dir.insere(valor)
            self.fb = self.calcfb()
            #print('arvore: {}, FB: {}'.format(self.info,self.fb))

      if abs(self.fb) == 2:
         self.balanceia(self)

      #if self.fb == 2: self.balanceia_esq(self)

      #elif self.fb == -2: self.balanceia_dir(self)

      #elif self.fb * -1 > 2: print("FUDEO!!! -> ", self.info)
      

   def balanceia_dir(self, raiz):
      print('nó sendo balanceado: {} | FB: {}'.format(raiz.info, self.fb))
      q= raiz.esq
      temp = q.dir
      q.dir = raiz
      self.esq= temp
      self= q

   def balanceia_esq(self, raiz):
      print('nó sendo balanceado: {} | FB: {}'.format(raiz.info, self.fb))
      q= raiz.dir
      temp = q.esq
      q.esq = raiz
      self.dir= temp
      raiz= q

   def balanceia(self, raiz):
      #ROTAÇÃO ESQUERDA LL
      if raiz.fb == 2 and raiz.dir.fb == 1:
         print('nó sendo balanceado: {} | FB: {} | RR'.format(raiz.info, self.fb))
         q= raiz.dir
         temp = q.esq
         q.esq = raiz
         self.dir= temp
         raiz= q
      
      #ROTAÇÃO DIREITA RR 
      if raiz.fb == -2 and raiz.esq.fb == -1:
         print('nó: {} | FB: {}| esq.FB:{} | RR'.format(raiz.info, raiz.fb, raiz.esq.fb))
         q= raiz.esq
         temp = q.dir
         q.dir = raiz
         self.esq= temp
         self= q
         
         
      #ROTAÇÃO LR
      if raiz.fb == 2 and raiz.dir == -1:
         
         return
      
      #ROTAÇÃO RL
      if raiz.fb == -2 and raiz.dir == 1:
         
         
         return

   def calcfb(self):
      if self.dir == None and self.esq == None: return 0

      elif self.dir != None and self.esq == None: return self.dir.altura()

      elif self.dir == None and self.esq != None: return -self.esq.altura()

      elif self.dir != None and self.esq != None: return self.dir.altura() - self.esq.altura()

      else:
         print('DEU RUIM AQUI NO \'calcfb\'')
         return None

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



