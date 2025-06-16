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
02/06
Monitoramento de recursos
    motivos de implementação: saude operacional, utilização de recursos, performance da aplicação, segurança

CloudWatch: coleta métricas de serviços AWS atraves de regiões em um repositório de métrica, coleta logs, métricas são gratuitas, logs são pagos, pode criar alarmes para avisar sobre limites atingidos

EventBridge: barramento de eventos, jeito de monitorar a AWS em tempo real

Custos: cost explorer
aula 04/06
Auto Scaling: scala baseada na data e tempo, é para cargas de trabalho previsíveis, scala baseada em métricas rastreadas, é para cargas de trabalho moderadamente intensas
