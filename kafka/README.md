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

Agora que o seu serviço Kafka está em pé, você pode começar a executar alguns comandos para utilização do serviço.

##### Criar novo tópico no Kafka

```
C:\kafka\bin\windows>kafka-topics.bat --create --bootstrap-server 192.168.0.86:9092 --topic topiconovo
	Created topic topiconovo.
```

##### Listar tópicos existentes no kafka

```
C:\kafka\bin\windows>kafka-topics.bat --bootstrap-server 192.168.0.86:9092 --describe
Topic: topiconovo       TopicId: zZr990bIRAaAZy_okT45DQ PartitionCount: 1       ReplicationFactor: 1    Configs: segment.bytes=1073741824
        Topic: topiconovo       Partition: 0    Leader: 0       Replicas: 0     Isr: 0
```

#### Curiosidades

