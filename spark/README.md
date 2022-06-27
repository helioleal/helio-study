### Apache Spark

Um breve explicação do Apache Spark é um framework de código aberto que auxilia no desenvolvimento de aplicações para grande volume de dados, ele trabalha com o conceito de paralelismo onde um nó mestre distribui a carga para nós trabalharoes. É possível utilizar linguagens como Java, Scala e Python para desevolver aplicações usando o spark. 
Explicação mais completas sobre Spark é possível encontrar na web, como no wikipedia: https://pt.wikipedia.org/wiki/Apache_Spark, ou no próprio site do Spark: https://spark.apache.org/

#### Como instalar o Spark no Windows

Aqui na minha estação pessoal veio instalado o Windows e eu pensei em instalar ele no Windows para ver como funciona, no começo tive muitas dificuldades e depois de um bom tempo eu consegui instalar ele e resolvi trazer algumas dicas para auxiliar quem deseja efetuar esse mesmo procedimento.

No meu caso eu utilizei a linguagem python para efetuar os testes usando o spark, então caso não tenha python e o pip instalado eu sugiro criar uma certa familiaridade com essas tecnologias antes de seguir esse pseudo tutorial. 

Bom, eu iniciei a minha brincadeira já criando um programa simples em python para rodar em spark.

Só que para isso eu precisei baixar o spark, eu baixei o spark e coloquei no C:, para baixar o spark eu digitei no Google "Spark Download", ele me deu esse caminho: https://spark.apache.org/downloads.html. 
Bom, eu baixei a bersão 3.2.1 e simples descompactei no C:\spark, ficou: **C:\spark\spark-3.2.1-bin-hadoop3.2**
Depois disso eu criar um pasta chamada hadoop, ficou: **C:\spark\spark-3.2.1-bin-hadoop3.2\hadoop\bin**
Entrei no Github: **https://github.com/cdarlint/winutils**
Lá eu baixei dois arquivos, **hadoop.dll** e **winutils.exe** e coloquei no diretório: **C:\spark\spark-3.2.1-bin-hadoop3.2\hadoop\bin**

Depois disso comecei a fazer testes com o spark, criei o arquivo bootsptrap.py  (Explicação contida no próprio código fonte: https://github.com/helioleal/helio-study/blob/main/spark/bootstrap.py). 

Gostaria de salientar que nesse fonte eu criei duas variáveis de ambiente, a **SPARK_HOME** e **HADOOP_HOME** que são utilizadas pelo spark no processo. 
Outra coisa, você vai notar a importação de um pacote chamado _**findspark**_, ele utiliza as variáveis de ambientes declaradas para utilizar as libs do spark para python.

#### Spark Streaming

O Apache spark é um framework que contém diversas ferramentas rodando em cima do Apache Core, um dele é um spark streaming, uma lib que fica rodando para processar dados em tempo real. 

##### Dicas spark streaming

Quando eu rodei os exemplos de spark streaming aqui na minha máquina foram gerando diversos erro e foi bem complicado de decifrar esses erros sem ter muito conhecimento nessa tecnologia, eu vou compartilhar abaixo algumas dicas que podem ajudar vocês nesse momento.

##### Kafka

Um dos primeiros testes que eu fiz com spark streaming foi utilizando o kafka, minha vontade era consumir dados que estavam chegando em um tópico kafka que consumir utilizando o spark streaming, porém no decorrer do meu desenvolvimento eu fui passando por diversos problemas, o primeiro deles estourava o erro:

```
'''
Para o erro: 
pyspark.sql.utils.AnalysisException:  Failed to find data source: kafka. Please deploy the application as per the deployment section of "Structured Streaming + Kafka Integration Guide".

Erro se refere a não achar o pacote do Kafka no Spark.
Usar variável de ambiente abaixo para corrigir o erro
'''
os.environ['PYSPARK_SUBMIT_ARGS'] = f'--packages org.apache.spark:spark-sql-kafka-0-10_{SCALA_VERSION}:{SPARK_VERSION} pyspark-shell'
```

Com a variável acima o erro de pacote do kafka não encontrado não ocorreu mais.


Depois que eu corrigi o erro acima ainda não tinha sido solucionado o problema de rodar o _spark streaming_ em minha máquina local, ficava dando um erro muito chato que foi meio complicado de achar a solução, depois de tanto pesquisar achei o seguinte artigo que me ajudou a solucionar o problema: https://stackoverflow.com/questions/41851066/exception-in-thread-main-java-lang-unsatisfiedlinkerror-org-apache-hadoop-io

Que era basicamente: O winutils.exe , hadoop.dll deve estar abaixo do C:\spark\spark-3.2.1-bin-hadoop3.2\hadoop\bin e a fica chave foi:

**"In addition to other solutions, Please download winutil.exe and hadoop.dll and add to $HADOOP_HOME/bin. It works for me."**

Depois da dica acima o spark streaming funcionou local, porém eu não usei a última versão do spark, eu usei uma anterior.













