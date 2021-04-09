# Monitoramento_Cryptomoedas_BTC-ETH-XRP
O algoritmo realiza o monitoramento da variação de preço das cryptomoedas Bitcoin (BTC), Ethereum (ETH) e XRP a partir do consumo da API da CoinGecko e apresenta os valores atuais em dolar e real das cryptomoedas e indica através de um sistema de cores se o valor da moeda subiu, desceu ou parou no mesmo valor.

## Requisitos
-colorama (pip install colorama)

## API
url: https://www.coingecko.com/api/documentations/v3

![API](https://user-images.githubusercontent.com/40063504/114242963-22863e80-9962-11eb-8eef-71c8dc6570cf.PNG)

## Operação

#### Legenda:
- Vermelho - Indica que o valor da crypto caiu comparado com o último valor.
- Verde - Indica que o valor da crypto subiu comparado com o último valor.
- Amarelo - Indica que o valor da crypto se manteve estável comparado com o último valor.

### Via VSCode
- Você pode executar o código diretamente em sua IDE de preferência conforme a imagem abaixo:

![VSCode](https://user-images.githubusercontent.com/40063504/114242804-e18e2a00-9961-11eb-97be-ec11ab7fd012.PNG)

### Via arquivo executável
- Ou você pode rodar o arquivo executável em sua máquina que esta localizado dentro da pasta "dist", o qual irá apresentar via terminal as variações de preço das moedas:


![Application](https://user-images.githubusercontent.com/40063504/114242850-f36fcd00-9961-11eb-8033-02e0cc072a7c.PNG)


![Application-2](https://user-images.githubusercontent.com/40063504/114242860-f5d22700-9961-11eb-8ef8-55704c2e7dad.PNG)
