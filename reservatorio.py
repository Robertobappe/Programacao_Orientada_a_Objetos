'''RESERVATÓRIO
Você deve criar uma classe (complete a célula abaixo) que representa um reservatório com uma capacidade fixa. A capacidade é especificada no momento da criação do objeto.
Por exemplo, o código
Reservoir(100)
cria um reservatório vazio com capacidade de 100 unidades de volume (não importa qual unidade).

Você pode adicionar mais líquido usando o método put(x), que insere x unidades de volume no reservatório. Se houver excesso (nem tudo o que se quer inserir cabe no reservatório),
o método irá encher o reservatório até onde é possível e então retornar o valor do que excedeu a capacidade. Se não houver excesso ele deve retornar 0.

Para retirar líquido do reservatório usamos o método take(x) que tira tenta tirar x unidades de volume do reservatório. Se o reservatório não tem líquido suficiente, é retirado
tudo o que ele tem e ele fica vazio. O método deve retornar a quantidade que ele efetivamente consegui retornar.

O método used() pode ser usado para verificar quanto líquido existe atualmente no reservatório. O método capacity() pode ser usado para ver a capacidade total de um reservatório.
'''

class Reservoir:
    def __init__(self, cap):
        self.cap = cap
        self.liq = 0
        self.aux = 0
        self.aux_ = 0
    
    def put(self, add):
        self.liq += add
        if self.liq >= self.cap:
            self.aux, self.liq = self.liq, self.cap
            return self.aux - self.liq
        else:
            return 0        
    
    def take(self, remov):
        if self.liq < remov:
            self.aux_, self.liq = self.liq, 0
        else:
            self.liq -= remov
            self.aux_ = remov
        return self.aux_            
        
    def used(self):
        return self.liq
        
    def capacity(self):
        return self.cap

r1 = Reservoir(10)

assert r1.used() == 0, 'Sua inicialização está errada'
assert r1.capacity() == 10, 'Capacidade errada'

assert r1.put(6) == 0, 'Está enchendo antes do que devia'
assert r1.used() == 6, 'Não está guardando o líquido corretamente'

assert r1.put(5) == 1, 'Não está lidando com excesso corretamente'
assert r1.used() == 10, 'Não está lidando com excesso corretamente'

assert r1.take(7) == 7, 'Não tira líquido como devia'
assert r1.used() == 3, 'Cuidado com a conservação da matéria'

assert r1.take(4) == 3, 'Não tirou como devia'
assert r1.used() == 0, 'Deveria estar vazio agora'

assert r1.capacity() == 10, 'Quem alterou a capacidade?'
