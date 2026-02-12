🌎 IoT Climate Data Pipeline – ESP32 + MicroPython

Projeto de Engenharia de Dados aplicado a IoT, focado na construção de uma estação meteorológica resiliente com coleta estruturada, sincronização temporal confiável e arquitetura preparada para integração com pipelines de dados.

🎯 Visão do Projeto

Desenvolver uma estação meteorológica de baixo custo capaz de:

Coletar dados ambientais em tempo real

Garantir integridade temporal via NTP

Operar com tolerância a falhas de rede

Estruturar dados em JSON padronizado

Preparar os dados para ingestão via MQTT ou pipeline ETL

O projeto simula um cenário real de Edge Computing aplicado à Engenharia de Dados.

🏗️ Arquitetura Atual
Sensores → ESP32 (Edge Layer)
            ↓
        Processamento local
            ↓
     Padronização JSON
            ↓
   Buffer Offline (Resiliência)
            ↓
     Pronto para envio (MQTT / HTTP)

🔎 Variáveis Coletadas

Temperatura (°C)

Umidade Relativa (%)

Luminosidade (classificação)

Timestamp ISO 8601 (UTC-3)

Identificação da estação

Exemplo de payload:

{
  "estacao": "adamantina_01",
  "timestamp": "2026-02-12T02:34:46",
  "temperatura": 29,
  "umidade": 63,
  "luminosidade": "CLARO"
}

🧠 Decisões Técnicas Implementadas
✅ Sincronização Temporal Confiável

Uso de NTP para garantir precisão temporal

Conversão para ISO 8601

Ajuste para UTC-3 (Brasil)

✅ Arquitetura Offline-First

Implementação de buffer local

Prevenção de perda de dados em caso de falha de conexão

Estrutura preparada para flush automático ao restabelecer rede

✅ Padronização de Dados

Estrutura JSON consistente

Preparação para ingestão por sistemas downstream

Facilita ETL, armazenamento em Data Lake ou banco relacional

⚙️ Stack Tecnológica

ESP32 (Edge Computing)

MicroPython

NTP (Time Sync)

JSON

Conceitos de Buffer Resiliente

Arquitetura IoT

🔜 Roadmap Técnico

Integração com BMP280 (pressão atmosférica)

Integração com sensor UV (GUVA-S12S)

Implementação de MQTT (modelo publish/subscribe)

Deep Sleep para eficiência energética

Rotação inteligente de arquivos

Pipeline ETL para armazenamento estruturado

Dashboard analítico (Power BI / Python / Grafana)

🧩 Conceitos Demonstrados

Este projeto demonstra conhecimento prático em:

Engenharia de Dados aplicada a IoT

Resiliência e tolerância a falhas

Sincronização temporal distribuída

Estruturação de dados para análise

Edge Processing

Arquitetura escalável orientada a eventos

📊 Aplicação

Projeto desenvolvido em contexto de iniciação científica com foco em análise de dados climáticos regionais e futura modelagem estatística.

🚀 Próxima Etapa Estratégica

Evoluir para arquitetura baseada em:

MQTT Broker

Pipeline de ingestão

Armazenamento estruturado

Dashboard analítico

Transformando a estação em um mini ecossistema completo de dados.
