# Como implementei minha solução (ideias e estratégias):

A principal ideia é que `find_all_peaks` percorra todo o dataset uma vez. A partir dessa única iteração, pegue TODOS os picos possíveis, sendo eles verdadeiros ou não.

A partir dos resultados gerados por `find_all_peaks`, `check_if_peaks_colide` entra em ação percorrendo a lista várias vezes, checando se existem picos nas posições entre -5 e +5 partindo do pico atual. Se sim, irá verificar qual é maior e apagar o menor.

Depois que `check_if_peaks_colide` tiver feito seu trabalho, irá chamar `find_time_media` para achar a média de tempo em segundos entre os picos verdadeiros e `convert_seconds` para converter de segundos para minutos e segundos.

# Como gerei os dados para validar minha solução

Usando datasets menores com cerca de valores para ter certeza que o algoritmo estava funcionando e usando a função `generate_dataset` para gerar datasets aleatórios e testar com dados maiores.

# Exemplos de entradas para testar a implementação

Estão nos arquivos example.txt.

# Quais as maiores dificuldades ou dúvidas que encontrei quando estava desenvolvendo a solução

Entender exatamente o que foi pedido e debugar para ter certeza do funcionamento.

# Como executar a solução (compilar? Instalar algum interpretador?)

Instalar o interpretador do Python caso não tenha, mudar o path em `read_dataset` e rodar com `python3 main.py`.
