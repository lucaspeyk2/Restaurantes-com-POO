from modelos.restaurante import Restaurante
from Cardapio.bebidas import Bebidas
from Cardapio.pratos import Pratos
from Cardapio.sobremesa import Sobremesa


restaurante = Restaurante('Comida de vó', 'Comida Caseira')
bebida = Bebidas('Coca-Cola', 10.0, '600ml')
prato = Pratos('Feijoada', 25.0, 'Porção')
sobremesa = Sobremesa('Pudim', 8.0, 'Delicioso pudim de leite condensado')
restaurante.adicionar_no_cardapio(bebida)
restaurante.adicionar_no_cardapio(prato)
restaurante.adicionar_no_cardapio(sobremesa)

bebida.aplicar_deconto()
prato.aplicar_deconto()
sobremesa.aplicar_deconto()
def main():
    restaurante.exibir_cardapio

if __name__ == '__main__':
    main()