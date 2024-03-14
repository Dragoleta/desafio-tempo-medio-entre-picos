<h1> Como implementei minha solução ( ideias e estratégias): </h1>

A principal ideia e que ``find_all_peaks`` percorra todo o dataset uma vez, a partir dessa unica iteracao pegue TODOS os picos possiveis, sendo eles verdadeiros ou nao.

A partir os resultados gerados por ``find_all_peaks``, ``check_if_peaks_colide`` entra em acao percorrendo a lista varias vezes checando se existem picos nas posicoes entre -5 e +5 partindo do pico atual, se sim, ira verificar qual e maior e apagar o menor

Depois que ``check_if_peaks_colide`` tirer feito seu trabalho ira chamar ``find_time_media`` para achar a media de tempo em segundos entre os picos verdadeiros e ``convert_seconds`` para converter de segundos para minutos e segundos


<h1>Como você gerei os dados para validar minha solução</h1>

Usando de dataset menores com cerca de valores para ter certeza que o algoritimo estava funcionando e usando a funcao ``generate_dataset`` para gerar datasets aleatorios e testar com dados maiores


<h1>Exemplos de entradas para testar a implementação</h1>

Estam nos arquivos example.txt

<h1>Quais as maiores dificuldades ou dúvidas que encontrei quando estava desenvolvendo a solução</h1>

Entender exatamente o que foi pedido e debuggar para ter certeza do funcionamento

<h1>Como executar a solução (compilar? Instalar algum interpretador?)</h1>

Instalar o interpretador do python caso nao tenha, mudar o path em ``read_phonebook`` e rodar com ``python3 main.py``