### Apache Kafka

#### Introdução

O Apache Kafka é uma plataforma que é denominada como Pub/Sub (Publisher / Subscriber), significa que é possível publicar e subscrever em eventos para enviar e/ou receber determinados dados, esses eventos possuem o nome de tópicos. 
Ele é usado para aplicações robustas, como por exemplo _Big Data_, então é super interessante analisar o cenário de utilização dessa ferramenta antes de sair utilizando apenas porque está no _Hype_.

Bom tendo isso em mente, eu iniciei meus estudos no Kafka e gostaria de compartilhar algumas experiências aqui com vocês, a primeira delas é relacionado a instalação dessa ferramenta, eu estou usando Windows aqui na minha estação pessoal e tive algumas dificuldades na instalação dele no Windows, vou compartilhar como fazer essa instalação no Windows nas seções mais abaixo.

#### Como instalar o Kafka no Windows

* 1 - Antes de qualquer coisa, sugiro instalar o JRE e configurar **JAVA_HOM**E e path do windows **%JAVA_HOME%/bin**

* 2 - Seguir esse tutorial: https://mmarcosab.medium.com/usando-apache-kafka-e-apache-zookeeper-no-windows-3e48e76e795f

* 3 - Quando for subir o kafka o erro **"A linha de entrada é muito longa"** pode ocorrer:* 
    * Para resolver isso, pode colocar o kafka no caminho C://kafka
    * Referência: https://cursos.alura.com.br/forum/topico-kafka-e-zookeeper-nao-iniciam-no-windows-10-114880

* 4 - Caso ocorra erro ao se conectar no _zookeeper_ e subir o kafka, pare e inicie no serviço do _zookeeper_:
  * Referência: https://stackoverflow.com/questions/63933799/kafka-zookeeper-zookeeperclienttimeoutexception-timed-out-waiting-for-connectio

* 5 - **Dica**, Atenção nos comandos do primeiro tutorial
	- Não existe **--zookeeper**, o certo é **--bootstrap-server**
	- Referência: https://stackoverflow.com/questions/53428903/zookeeper-is-not-a-recognized-option-when-executing-kafka-console-consumer-sh

* 6 - Caso o comando de erro de _timeout_, preste atenção no console do Kafka, deve pegar o IP Certo:
	- Procurar pela frase pra achar o caminho certo: 
```
Recorded new controller, from now on will use broker
192.168.0.86:9092 (id: 0 rack: null) (kafka.server.BrokerToControllerRequestThread)
```

##### Como subir os serviços no Windows

Zookeper:
```
C:\Users\<caminho_zookeeper>\apache-zookeeper-3.8.0-bin> .\bin\zkserver
```

Kafka:
```
C:\kafka>.\bin\windows\kafka-server-start.bat .\config\server.properties
```

#### Comandos

Agora que o seu serviço Kafka está em pé, você pode começar a executar alguns comandos para utilização do serviço, consultar as pastas topic, producer e consumer para isso.


#### Curiosidades

##### Zookeeper

Quando comecei a estudar Kafka, percebi que tinha que subir esse serviço do Zookeeper antes do Kafka e fiquei na dúvida sobre o que seria esse serviço, então eu pesquisei e descobri algumas respostas interessantes, resumindo meu entendimento, o zookeper é uma plataforma _Open Source_ que foi criada com o intuito de auxiliar no gerencimento de aplicações distribuídas que são desenvolvidades para Cloud, como por exemplo, auxiliar no gerencimento de um Cluster.

Definição Wikipedia: "Apache ZooKeeper is an open-source server for highly reliable distributed coordination of cloud applications..."
Referência: https://en.wikipedia.org/wiki/Apache_ZooKeeper#:~:text=Apache%20ZooKeeper%20is%20an%20open-source%20server%20for%20highly,is%20a%20project%20of%20the%20Apache%20Software%20Foundation.

Documentação do próprio Zookeeper: https://zookeeper.apache.org/

Blog com algumas respostas interessantes: https://qastack.com.br/programming/23751708/is-zookeeper-a-must-for-kafka#:~:text=O%20Kafka%20foi%20desenvolvido%20para%20usar%20o%20Zookeeper.,pergunta%2C%20parece%20que%20voc%C3%AA%20n%C3%A3o%20precisa%20do%20Kafka.

#### Dicas

##### O que fazer quando mudar o zookeper de local na minha estação
Quando isso acontece o Kafka para de funcionar, o ideal nesses casos para que o kafka volte a funcionar é limpar a pasta de log do Kafka, com isso o serviço volta a subir corretamente.


