# Witch Alice

## Jogo de adivinhação baseado no famoso Akinator!

## Demonstração no Youtube
[![Witch Alice Game](https://github.com/kaique-ryan-santos-chagas/wizard-classifier-front/assets/59677362/3b927023-db36-4eb0-9f4f-85b94cbc0c8f)](https://www.youtube.com/watch?v=Bd-GbiYatEY&t=21s)

### Link para jogar o jogo: https://kaique-ryan-santos-chagas.github.io/wizard-classifier-front/

## Como modificar o código para personáliza-lo ou realizar melhorias 

* Baixe o código fonte da aplicação:

```
git clone https://github.com/kaique-ryan-santos-chagas/wizard-classifier.git
```

* O software é uma Rede Neural Artificial de classificação binária.
* Após baixar o código fonte da rede, o modelo pré-treinado já estará disponível, com o nome "model.json"
* É possível testar a classificação da rede executando o arquivo de teste "interface.py".
* Caso queira treinar a rede novamente, basta executar o arquivo "app.py".
* Para novos personagens para classificação, basta adicioná-los no arquivo "character_data.json", disponível na pasta data.

## Como o software funciona?

* A aplicação realiza a classificação dos personagens baseado em um modelo de Rede Neural Artificial.
* A Rede Neural Artificial foi desenvolvida em Python para classificação binária de dados.
* No momento existem poucos personagens na qual a Rede Neural Artificial é capaz de adivinhar.
* Os personagens foram adicionados ao dataset de treinamento da rede que se encontra na pasta data.
* Para classificar mais personagens, basta adicioná-los ao dataset e treinar a rede novamente.
