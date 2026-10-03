# ⚡ Metropolis AI: Autonomous Reputation Layer for Aave V3 Agents

**Metropolis AI** es una infraestructura descentralizada de identidad y verificación de confianza diseñada específicamente para auditoría y rendición de cuentas (*accountability*) de agentes autónomos de IA que operan en **Aave V3**, desplegada de forma nativa sobre la blockchain de alta velocidad de **Monad**.

El proyecto implementa el estándar **ERC-8004** para crear un registro público e inmutable (un "Buró de Crédito DeFi") donde las acciones automatizadas de los bots (como la protección de factores de salud o ejecuciones de liquidación) son auditadas on-chain por los propios protocolos y usuarios.

---

## 🚨 El Desafío DeFi de la IA Autónoma
En protocolos como **Aave V3**, los usuarios delegan capital en agentes de IA para automatizar tareas críticas: depositar colateral de emergencia, reestructurar deuda o ejecutar liquidaciones de alta velocidad. Sin embargo, el ecosistema carece de un registro de confianza:
1. **Riesgo Algorítmico:** Un bug en el bot puede causar liquidaciones erróneas o pérdida de fondos sin dejar rastro de responsabilidad.
2. **Falta de Historial Criptográfico:** No existía un método inmutable para verificar qué bots son seguros antes de delegarles capital de riesgo.
3. **Cuellos de Botella Técnicos:** Registrar micro-calificaciones por cada operación financiera saturaría cualquier red tradicional. La ejecución paralela de **Monad** es la única que hace viable este sistema a escala global.

---

## 💡 Nuestra Solución: Arquitectura ERC-8004
Metropolis AI actúa como un oráculo matemático de reputación que opera en tres capas unificadas:

*   **Identidad Soberana del Bot:** Al encenderse, el agente de IA genera su propio par de llaves criptográficas y se registra en Monad con un `AgentID`.
*   **Auditoría de Operaciones:** Cada vez que el bot ejecuta una acción en Aave (ej. salvar un *Health Factor* por debajo de 1.2), los contratos de Aave o los usuarios envían un veredicto a la red (voto positivo por éxito, reporte de falla por bug).
*   **Score Matemático Real-Time:** La blockchain procesa las interacciones calculando un Score de Confianza (0% al 100%). Los protocolos pueden restringir el acceso a sus bóvedas exigiendo un score mínimo (ej. >90%).

---

## 🛠️ Stack Tecnológico Desacoplado
El MVP se desarrolló desde cero utilizando un enfoque modular e independiente de bases de datos tradicionales:
*   **Capa On-Chain (Blockchain):** Smart Contract escrito en **Solidity**, compatible con la EVM de Monad, estructurado mediante mapeos de acceso directo para máxima eficiencia de gas.
*   **Capa Frontend (Interfaz):** Dashboard interactivo desarrollado 100% en **Python (Streamlit)** con look oscuro cyberpunk y gráficos reactivos en tiempo real.
*   **Capa Middleware (Puente):** Módulo ligero **Web3.py** preparado para conectar las firmas del backend con las funciones RPC de la Testnet de Monad.

---

## 📦 Guía de Instalación y Ejecución Local

Para levantar el Dashboard e interactuar con el simulador del oráculo, ejecuta los siguientes comandos en tu terminal de Visual Studio:

1. **Clonar el repositorio:**
   ```bash
   git clone https://github.com[TU_USUARIO]/metropolis-ai-aave.git
   cd metropolis-ai-aave
   ```

2. **Instalar las dependencias oficiales del entorno:**
   ```bash
   pip install streamlit web3
   ```

3. **Encender el motor de la aplicación web:**
   ```bash
   python -m streamlit run app.py
   ```

---
*Desarrollado de forma nativa por un equipo de 2 integrantes para el Monad Metropolis Hackathon (2026).*
