🌦️ Estação Meteorológica IoT – ESP32 + MicroPython

Projeto de iniciação científica para coleta de dados climáticos utilizando ESP32 + MicroPython, com foco em:

Aquisição de dados ambientais

Padronização em JSON

Sincronização de horário via NTP

Tolerância a falhas de conexão (buffer local)

Preparação para integração com MQTT / pipeline de dados

📌 Objetivo

Construir uma estação meteorológica de baixo custo capaz de:

Medir variáveis climáticas

Gerar dados estruturados

Operar mesmo com falhas de rede

Servir como base para um futuro pipeline ETL de dados climáticos

🧰 Hardware Utilizado

ESP32 DOIT DevKit (ESP32-WROOM-32)

Sensor DHT11 (Temperatura e Umidade)

Sensor LDR (Luminosidade – módulo digital)

Protoboard + Jumpers

Fonte externa 12V 1A (para módulo da protoboard)

📊 Variáveis Coletadas

Atualmente o sistema coleta:

🌡️ Temperatura (°C)

💧 Umidade relativa do ar (%)

💡 Luminosidade (CLARO / ESCURO)

🕒 Timestamp ISO 8601 (UTC-3 Brasil)

🏷️ Identificação da estação

Exemplo de saída:

{
  "estacao": "adamantina_01",
  "timestamp": "2026-02-12T02:34:46",
  "temperatura": 29,
  "umidade": 63,
  "luminosidade": "CLARO"
}

🌐 Conectividade

Conexão WiFi automática

Sincronização de horário via NTP

Ajuste manual de offset UTC-3 (Brasil)

🧠 Arquitetura Atual

Fluxo de execução:

Conecta ao WiFi

Sincroniza horário via NTP

Lê sensores

Gera JSON estruturado

Armazena em buffer caso falhe conexão

Aguarda 60 segundos

Repete

💾 Sistema de Buffer (Offline First)

Caso a conexão caia:

Os dados são armazenados localmente

São reenviados quando a conexão retorna

Evita perda de dados

Garante integridade para análises futuras

Esse modelo permite evolução para:

Deep Sleep

MQTT

Armazenamento rotativo

Pipeline ETL automatizado

🔜 Próximas Evoluções Planejadas

 Integração com BMP280 (pressão atmosférica)

 Integração com GUVA-S12S (radiação UV)

 Implementação de MQTT

 Deep Sleep para economia de energia

 Rotação inteligente de arquivos

 Envio para banco de dados

 Construção de pipeline ETL

 Dashboard de visualização (Power BI / Python / Grafana)

🚀 Tecnologias Envolvidas

MicroPython

ESP32

NTP

JSON

Arquitetura resiliente

Conceitos de IoT

Conceitos de Engenharia de Dados

🎯 Aplicação Acadêmica

Projeto desenvolvido no contexto de iniciação científica com foco em:

Coleta de dados climáticos regionais

Estruturação de dados para ciência de dados

Análise estatística e modelagem futura

📌 Estrutura do Projeto
/main.py
/README.md


(Estrutura será expandida conforme novas funcionalidades forem adicionadas)

📎 Status do Projeto

🟡 Em desenvolvimento
Versão atual: coleta + JSON + NTP + buffer local
