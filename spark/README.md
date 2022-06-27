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
Lá eu baixei dois arquivos,0**hadoop.dll** e **winutils.exe** e coloquei no diretório: **C:\spark\spark-3.2.1-bin-hadoop3.2\hadoop\bin**

Depois disso comecei a fazer testes com o spark, criei o arquivo bootsptrap.py (Explicação contida no próprio código fonte)









