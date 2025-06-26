# Aula 06/02

## 1. Componentes Independentes  
**O que é?** Arquiteturas compostas por componentes com baixo acoplamento, que podem ser substituídos ou replicados sem afetar o sistema como um todo.  
**Exemplo:** dividir uma aplicação monolítica em microsserviços, onde cada serviço funciona isoladamente.

## 2. Design de Serviços  
**O que é?** Pensar em infraestrutura como serviços, não apenas servidores físicos ou virtuais.  
**Exemplo:** usar containers orquestrados por Kubernetes e filas de mensagens (RabbitMQ, Kafka) para comunicação entre serviços.

## 3. Escolher Melhores Opções de Banco de Dados  
**O que é?** Avaliar performance, escalabilidade e consistência de cada solução.  
**Exemplo:** optar por um banco NoSQL (DynamoDB) para alta taxa de leitura e por um relacional (Aurora) para transações complexas.

## 4. Evitar Pontos Únicos de Falha  
**O que é?** Não depender de um único recurso crítico.  
**Exemplo:** ter múltiplas réplicas de banco de dados, backups e cópias de serviços para failover automático.

## 5. Otimização de Custo  
**O que é?** Balancear o nível de serviço necessário com o orçamento disponível.  
**Dica:** não usar clusters de alta capacidade para workloads pequenas; escalar apenas o que você realmente consome.

## 6. Cache  
**O que é?** Armazenar dados temporariamente em memória para acelerar respostas.  
**Exemplo:** Redis para sessões de usuário e consultas frequentes, diminuindo a latência do banco principal.

## 7. Segurança  
**O que é?** Implementar múltiplas camadas de proteção: criptografia, isolamento de redes e autenticação forte.  
**Dica:** use services gerenciados (ex.: AWS KMS, IAM) e criptografe dados em trânsito e em repouso.

## 8. Seleção de Regiões e AZs  
**O que é?** Escolher localização geográfica que minimize latência, atenda a requisitos legais e otimize custo.  
**Exemplo:** armazenar dados de brasileiros em sa-east-1 (São Paulo) para rapidez e conformidade com a LGPD.

## 9. Local Zones  
**O que é?** Extensões de regiões principais, colocadas próximas a grandes centros urbanos para ultrabaixa latência.  
**Exemplo:** usar uma Local Zone em Santiago para streaming em tempo real, sem depender da região de São Paulo.

## 10. Infraestrutura Global  
**Fatos:** a AWS conta com dezenas de regiões, centenas de zonas de disponibilidade e milhares de Edge Locations, garantindo alta disponibilidade e performance global.

---

# Aula 27/02

## 1. Trade-offs  
**O que é?** Escolhas entre características opostas para atender melhor aos requisitos do projeto.  
- Durabilidade vs. custo  
- Cache vs. consistência  
**Exemplo:** priorizar durabilidade em sistemas financeiros e cache agressivo em sistemas de recomendação.

## 2. Escalabilidade  
**O que é?** Capacidade de manter níveis de serviço à medida que a demanda cresce.  
**Exemplo:** adicionar nós a um cluster ou usar serviços serverless que escalam automaticamente.

## 3. Automatização  
**O que é?** Criar pipelines e scripts que gerenciem provisão, deploy e monitoramento sem intervenção manual.  
**Exemplo:** usar Terraform para IaC e pipelines CI/CD para deploy automático em múltiplos ambientes.

## 4. IaC (Infraestrutura como Código)  
**Vantagens:** reprodutibilidade, versionamento e redução de erros de configuração manual.  
**Ferramentas:** Terraform, CloudFormation, Pulumi.

## 5. Recursos Descartáveis  
**O que é?** Tratar servidores e serviços como efêmeros, reproduzíveis a qualquer momento.  
**Exemplo:** instâncias spot para workloads não críticas, fáceis de recriar se forem interrompidas.

---

# Aula 10/03

## 1. AWS POPs  
Pontos de presença que entregam conteúdo com baixa latência (CloudFront, Edge Locations).

## 2. Securing Access  
Segurança de usuários e permissões: autenticação multifatorial, políticas de acesso mínimas e rotação de credenciais.

## 3. Modelo de Responsabilidade Compartilhada  
- **AWS:** segurança física e infraestrutura de hardware/software gerenciado.  
- **Cliente:** sistemas operacionais, aplicações, dados e configuração de segurança.

---

# Aula 13/03 _(complemento)_

## 5. Autenticação  
**O que é?** Verificar identidade usando algo que você sabe (senha), algo que você é (biometria) e algo que você possui (token).  
**Boas práticas:** MFA sempre ativa, rotação periódica de credenciais e não uso do root para tarefas do dia a dia.

## 6. Acesso Programático  
**O que é?** Uso de Roles e chaves temporárias para que aplicações/scripts executem ações na AWS sem expor credenciais permanentes.

---

# Aula 17/03 _(complemento)_

## 6. RBAC (Role-Based Access Control)  
Definição de permissões por função dentro da organização, garantindo coerência e auditabilidade.

## 7. IAM Policies e Permissions  
Políticas que definem exatamente quais ações um usuário ou serviço pode executar em quais recursos.

## 8. Determining Permissions at Request Time  
**O que é?** Avaliar todas as políticas associadas a um usuário/role e testar condições antes de autorizar a ação.

## 9. Tipos de Armazenamento (EBS, EFS, FSx, S3)  
Comparativo entre block storage, file storage e object storage, cada um adequado a diferentes cenários de uso.

## 10. Amazon S3  
Detalhes de funcionamento: namespace global, versionamento, criptografia e políticas de ciclo de vida.

---

# Aula 24/03

## 1. Lifecycle Policies no S3  
Automação de transição de classes de armazenamento e expiração de objetos obsoletos.

## 2. Versionamento no S3  
Proteção contra sobregravações, criando novas versões de objetos a cada upload.

## 3. Cross-Origin Support (CORS)  
Configuração de compartilhamento controlado entre domínios para aplicações web.

---

# Aula 27/03

## 1. Amazon Costs  
- Pague apenas pelo que usar  
- Custos de transferência de dados  
- Monitoramento de gastos via AWS Cost Explorer

---

# Aula 03/04

## 1. EC2  
Máquinas virtuais elásticas para qualquer tipo de workload; uso de AMIs para clonagem de servidores.

## 2. EBS  
Armazenamento persistente em blocos, com possibilidade de redimensionamento e troca de tipo a quente.

## 3. Compute Optimizer  
Serviço de IA que recomenda tipos de instância mais adequados a cada workload.

## 4. File Share  
- FSx: file shares para Windows  
- EFS: sistemas de arquivos NFS para Linux, elásticos e compartilhados

---

# Aula 07/04

## 1. Instance Metadata  
API interna para recuperar informações da instância sem expor dados sensíveis.

## 2. HPC vs. Spread vs. Partition  
- **HPC:** instâncias próximas para máxima performance de rede  
- **Spread:** instâncias distribuídas para alta disponibilidade  
- **Partition:** meio-termo, usado por Kafka, Cassandra e Spark

## 3. EC2 Free Tier  
Uso gratuito de instâncias elegíveis por 12 meses.

## 4. Modelos de EC2  
- On-Demand: flexível, sem compromisso  
- Reserved: 1–3 anos por menor custo  
- Saving Plans: desconto por uso previsto  
- Spot: aproveita capacidade ociosa, sujeito a interrupções

---

# Aula 10/04

## 1. Considerações ao Criar um Banco  
Avaliar escalabilidade, duração dos dados e padrões de acesso.

## 2. Amazon RDS  
Bancos relacionais gerenciados (PostgreSQL, MySQL, Aurora etc.).

## 3. Serviços NoSQL (DynamoDB, Neptune, ElastiCache)  
Soluções sem esquema rígido, orientadas a documentos, grafos ou cache.

## 4. Amazon Aurora & Aurora Serverless  
- Aurora: performance 3–5× MySQL/Postgres  
- Serverless: escala automática, pagando apenas ao rodar

---

# Aula 17/04

## 1. Connection Pooling (RDS Proxy)  
Gerenciamento eficiente de conexões para aplicações de alta concorrência.

## 2. Backups no RDS  
- Automáticos (5-day window)  
- Snapshots manuais para retenção indefinida

## 3. KMS (Key Management Service)  
Cofre de gerenciamento de chaves, suportando criptografia simétrica e assimétrica.

## 4. DynamoDB  
Banco NoSQL totalmente gerenciado, com performance em milissegundos e criptografia automática.

## 5. Redshift  
Data warehouse para análises em larga escala.

## 6. Outros Bancos AWS  
DocumentDB, Keyspaces, MemoryDB, Neptune, Timestream, Quantum Ledger

---

# Aula 05/05

## 1. VPC  
Rede virtual isolada por região, com controle de tráfego granular.

## 2. CIDR  
Máscara de rede que define o tamanho e o alcance da VPC.

## 3. Subnet Pública  
Recursos acessíveis da internet, conforme regras de Security Group e ACL

---

# Aula 08/05

## 1. NAT Gateway / NAT Instance  
Permite que instâncias em subnets privadas façam chamadas à internet sem expor IP público.

## 2. Arquitetura de VPC  
- Banco de dados em subnets privadas  
- Servidores web em subnets públicas  
- NAT e firewalls centralizados

## 3. Security Groups & Network ACLs  
Regras de entrada/saída em nível de instância e de subnet.

## 4. AWS Network Firewall & VPC Flow Logs  
Inspeção avançada de tráfego e registro de fluxos de rede para auditoria.

---

# Aula 19/05

## 1. Topologia Full Mesh  
Todas as VPCs conectadas entre si diretamente.

## 2. Hub-and-Spoke (Shared VPC)  
Um hub central que interliga várias spoke VPCs.

## 3. Transit Gateway  
Ponto único de conexão para múltiplas VPCs e redes locais, suportando milhares de anexos.

## 4. VPC Peering  
Conexão direta entre duas VPCs; não é transitivo.

## 5. AWS Direct Connect  
Conexão dedicada de alta largura de banda entre sua rede e a AWS.
Aula 26/05/2025
IAM Groups: criar um role para associar todas as permissões que as pessoas desse grupo devem ter, e depois vincular essas pessoas ao grupo.
ele sempre vai dar prioridade para negar o acesso, ex: caso tenha 20000 mil acessos e um "deny" ele vai perder seus acessos

RBAC - Role Base Access Control.
Concedar permissão para os usuarios através de roles para melhor controle de quem acessa oque.
Toda vez que um usuário assume uma role, ele recebe uma credencial nova e temporária.
Ao terminas o prazo, pode-se assumir a role novamente, porém a credencial irá ser diferente

AWS Cognito.
Ele permite acesso usando conta de outras plataformas
## Aula 29/05/2025
Iriamos criar um Cognito para cirar uma autenticação java

User pool: banco de dados de usuarios e senhas, independente da linguagem, ao invés de ter uma tela de login por exemplo em java, ele leva lá para a aws verifica e depois retorna a resposta, ele faz a autenticação da aplicação, e também a atutenticação para que o seu software se comunique com a AWS

AWS Organization: serviso da aws que permite você gerenciar multiplas contas usando uma extrutura ierarquica, e você ganha desconto por volume

service control polices: politicas de governanca da tua conta da aws, por exemplo se eu tenho carteira de abilitação, mas a policia me impede de dirigir babado, ou seja ela faz a governancia, eu posso dirigir, mas a policia não me deixa dirigir bebado, no caso ela limita de fazer algo fora dela

Police de limite não dão permissão
Police de grant dão permissão

Criptografia simetrica: tem uma chave só para criptografar e descriptografar
Criptografia asimetrica: tem duas chaves uma para criptografar e outra para descriptografar

Server side encryption: criptografia dentro da nuvem

AWS Key Management Service(AWS KMS): cofre de chaves e ferrameta de criptografia padrão da AWS, e é baseada em software
HSMs: igual ao KMS mas as chaves ficam em um servidor fisico ao invés da nuvem

Amazon Detective: detecta comportamentos estranhos na sua conta
## 02/06
Monitoramento de recursos
    motivos de implementação: saude operacional, utilização de recursos, performance da aplicação, segurança

CloudWatch: coleta métricas de serviços AWS atraves de regiões em um repositório de métrica, coleta logs, métricas são gratuitas, logs são pagos, pode criar alarmes para avisar sobre limites atingidos

EventBridge: barramento de eventos, jeito de monitorar a AWS em tempo real

Custos: cost explorer
## Aula 05/06
Auto Scaling: scala baseada na data e tempo, é para cargas de trabalho previsíveis, scala baseada em métricas rastreadas, é para cargas de trabalho moderadamente intensas
## Aula 16/06
Scaling aws databases
Aurora Cluster: 5x mais rapido que o sql; é um dos bancos mais automatizados; 
Load balancer: 
ELB: Distruibuidor de atividades da amazon entre as maquinas do cluster; ela é aberta para rede publica mas tambem pode ser privada; slacalabilidade basica on incoming traffic;
4 tipos de load balancer; 
classic load balancer; usa o EC2 OPERA OSI;
Aplication balacencer; camada 7; diferencia /produto de / clientes;
Network load balancer; usar tls offloading; ele sabe diferencia tcp de udp: O TCP, ou Transmission Control Protocol, é orientado à conexão, garantindo entrega confiável e ordenada dos dados, enquanto o UDP, ou User Datagram Protocol, é sem conexão e prioriza a velocidade, com entrega não garantida e sem ordem. 
gateway load balancer: barrar entradas de estranhos; e tambem caso queira utilizar loadbalancer de terceiros.
Load balancer components:
TLS certificate: tem prasos de 3 meses, porem são gratuitos;
DNS lookups:

Route 53: um servidor de dns que traduz ips; ele tem SLA 100%; pode monitorar dcloudwatch alarms; suporta multiplas rotas;
A IPV4
AAAA IPCV6
CNAME: é uma entrada no Sistema de Nomes de Domínio (DNS) que mapeia um nome de domínio (um alias) para outro nome de domínio (o nome canônico ou verdadeiro)
TXT: PROVA QUE VC DONO DE UM DNS
mx
ns: e-mail
## Aula 26/05/2025
IAM Groups: criar um role para associar todas as permissões que as pessoas desse grupo devem ter, e depois vincular essas pessoas ao grupo.
ele sempre vai dar prioridade para negar o acesso, ex: caso tenha 20000 mil acessos e um "deny" ele vai perder seus acessos

RBAC - Role Base Access Control.
Concedar permissão para os usuarios através de roles para melhor controle de quem acessa oque.
Toda vez que um usuário assume uma role, ele recebe uma credencial nova e temporária.
Ao terminas o prazo, pode-se assumir a role novamente, porém a credencial irá ser diferente

AWS Cognito.
Ele permite acesso usando conta de outras plataformas
## Aula 29/05/2025
Iriamos criar um Cognito para cirar uma autenticação java

User pool: banco de dados de usuarios e senhas, independente da linguagem, ao invés de ter uma tela de login por exemplo em java, ele leva lá para a aws verifica e depois retorna a resposta, ele faz a autenticação da aplicação, e também a atutenticação para que o seu software se comunique com a AWS

AWS Organization: serviso da aws que permite você gerenciar multiplas contas usando uma extrutura ierarquica, e você ganha desconto por volume

service control polices: politicas de governanca da tua conta da aws, por exemplo se eu tenho carteira de abilitação, mas a policia me impede de dirigir babado, ou seja ela faz a governancia, eu posso dirigir, mas a policia não me deixa dirigir bebado, no caso ela limita de fazer algo fora dela

Police de limite não dão permissão
Police de grant dão permissão

Criptografia simetrica: tem uma chave só para criptografar e descriptografar
Criptografia asimetrica: tem duas chaves uma para criptografar e outra para descriptografar

Server side encryption: criptografia dentro da nuvem

AWS Key Management Service(AWS KMS): cofre de chaves e ferrameta de criptografia padrão da AWS, e é baseada em software
HSMs: igual ao KMS mas as chaves ficam em um servidor fisico ao invés da nuvem

Amazon Detective: detecta comportamentos estranhos na sua conta
## Aula 02/06/2025
Monitoramento de recursos
    motivos de implementação: saude operacional, utilização de recursos, performance da aplicação, segurança

CloudWatch: coleta métricas de serviços AWS atraves de regiões em um repositório de métrica, coleta logs, métricas são gratuitas, logs são pagos, pode criar alarmes para avisar sobre limites atingidos

EventBridge: barramento de eventos, jeito de monitorar a AWS em tempo real

Custos: cost explorer
## Aula 05/06/2025
Auto Scaling: scala baseada na data e tempo, é para cargas de trabalho previsíveis, scala baseada em métricas rastreadas, é para cargas de trabalho moderadamente intensas
## Aula 16/06/2025
Scaling AWS databases
Escalando um cluster de Aurora: escala verticalmente mudando o tamanho da instancia de aurora, escala horisontalmente usando aurora auto scaling para gerenciar a leitura de números de replicas


Load Balance: distribui trafego entre multiplos alvos em um ou mais zonas abitaveis, pode receber trafego publico ou privado, verifica a saude das maquinas antes de mandar a requisição, scala automático. 

4 tipos de load balancer: 
    o load balancer classico, você pode usar, mas ele não é mais indicado;
    application load balancer: camada 7, é o mais utilizado, diferencia produto de cliente;
    network load balancer: usar tls offloading diferencia tcp de udp, é o segundo mais utilizado;
    gateway load balancer: é para quando você não quer utilizar o load balancer da AWS;

Load Balancer Componentc: 
TLS Certificate: são de graça, mas tem que renovar a cada 3 meses

DNS lookups: 

Route 53: um servidor de dns que traduz seu dominio para uma hosted zones, ele tem SLA 100%, pode monitorar dcloudwatch alarms, suporta multiplas rotas

AAAA IPCV6
CNAME: é uma entrada no sistema de nomes de domínio (DNS) que mapeia um nome de dominio (um alias) para outro nome de dominio (o nome canonico ou verdadeiro)
TXT: prova que você é dono de um DNS
MX
NS: e-mail
## Aula 23/06/2025
CloudFormation: serviso aws permite que você fassa criação, atualização e exclusão de recursos de forma automatizada, posso criar arquivo "YAML"(usa mesma ideia do python, ele precisa de identação, mas tem menos texto) e arquivo "JSON"(mais verboso e mais fácil de escrever)

Drift detection: permite que você identifique discrepâncias entre o estado atual dos seus recursos AWS implantados e o estado esperado, conforme definido nos seus modelos do CloudFormation

AWS Quick Start: acelerador de criação de produtos e servisos

Cache content: sempre que precisar melhorar a performance do banco, se usa cache por exemplo;
    ElastiCache: geralmente mais utilizado para banco, se coloca na frente do banco de dados para entregar mais rápido
    CloudFront: clocar na frente do site para entregar recursos mais rápidos, na frente do LoadBalancer
## Aula 26/06 
Fluxo de uma venda online:
O sistema não processa tudo de uma vez, mas em etapas assíncronas (com delays entre elas).
Exemplo:
Aguarda a nota fiscal ser gerada.
Aguarda a confirmação do cartão.
Aguarda o envio pela transportadora.
Cada etapa ocorre em momentos diferentes, sem bloqueio do processo principal.
Como o sistema gerencia isso?
Usando filas para desacoplar os processos.
Funcionamento:
O pedido passa de uma fila para outra a cada etapa concluída.
Exemplo:
Pedido confirmado → vai para uma fila.
Outro serviço consome essa fila, executa sua parte (ex: gerar nota fiscal) e envia para a próxima fila.
Repete até concluir todas as etapas.
Vantagens das filas:
Redução de acoplamento: Sistemas não se comunicam diretamente, apenas via filas.
Escalabilidade: Processos rodam de forma independente e assíncrona.
Resiliência: Se um serviço falhar, a mensagem fica na fila até ser processada.
Observação do professor:
Já implementamos esse modelo em projetos anteriores.
Filas são um padrão eficiente para operações distribuídas e complexas.
Publish/subscribe ,messaging:
vc está escrito em um grupo, onde todos inscritos recebem mensagen atumatica. podendo ter 12 milhoes e meio por topico.
