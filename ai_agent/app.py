import streamlit as st
import blockchain_bridge as bc 
from main import AIAgent


# ==========================================
# 1. CONFIGURACIÓN DE LA PÁGINA (LOOK METROPOLIS)
# ==========================================
st.set_page_config(
    page_title="Metropolis AI - Autonomous Reputation Layer",
    page_icon="⚡",
    layout="wide" # Cambiamos a diseño ancho para aprovechar mejor las columnas
)

# Estilos CSS inyectados para lograr el look Cyberpunk/Monad más profesional
st.markdown("""
    <style>
    .main { background-color: #0d0e12; color: #ffffff; }
    .stButton>button { width: 100%; border-radius: 4px; font-family: monospace; font-weight: bold; transition: 0.3s; }
    .stButton>button:hover { background-color: #8447ff !important; color: white !important; border-color: #8447ff !important; }
    div[data-testid="stMetricValue"] { color: #8447ff; font-family: monospace; font-size: 28px; }
    .agent-card { 
        border: 1px solid #2a2b36; 
        padding: 25px; 
        border-radius: 8px; 
        background-color: #13151a;
        margin-bottom: 25px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.3);
    }
    code { color: #00ff88 !important; background-color: #1a1c23 !important; padding: 2px 6px; border-radius: 4px; }
    </style>
    """, unsafe_allow_html=True)

# ==========================================
# 2. SISTEMA DE PERSISTENCIA DE DATOS SIMULADO
# ==========================================
if "wallet_connected" not in st.session_state:
    st.session_state.wallet_connected = False
    st.session_state.user_address = ""

if "agents" not in st.session_state:
    # Datos iniciales adaptados a casos reales de automatización en Aave
    st.session_state.agents = [
        {
            "id": "0x1a7f72...892b", 
            "name": "Aave-Health-Factor-Guard", 
            "description": "Monitorea posiciones en Aave V3. Deposita colateral automáticamente si el Health Factor cae por debajo de 1.2.", 
            "tasks": 312, 
            "reputation": 98
        },
        {
            "id": "0x2b3c54...456d", 
            "name": "Leverage-Aave-Max", 
            "description": "Agente autónomo de apalancamiento recursivo utilizando el pool de liquidez de USDC/wETH en Aave.", 
            "tasks": 85, 
            "reputation": 74
        },
        {
            "id": "0x3c9e11...710f", 
            "name": "Aave-Liquidator-Bot", 
            "description": "Bot de alta velocidad programado para ejecutar liquidaciones de préstamos riesgosos dentro de Aave Protocol.", 
            "tasks": 152, 
            "reputation": 42
        }
    ] 

# ==========================================
# 3. INTERFAZ: ENCABEZADO PRINCIPAL
# ==========================================
st.markdown("<h1 style='color: #8447ff; margin-bottom: 0;'>⚡ METROPOLIS AI</h1>", unsafe_allow_html=True)
st.markdown("<p style='color: #8a8b94; font-size: 16px; margin-top: 0;'>Decentralized Trust & Identity Verification Architecture (ERC-8004 Pattern)</p>", unsafe_allow_html=True)
st.markdown("---")

# ==========================================
# 4. BARRA LATERAL (AUTENTICACIÓN WEB3)
# ==========================================
with st.sidebar:
    st.markdown("<h2 style='color: #8447ff;'>🔐 Web3 Wallet Connect</h2>", unsafe_allow_html=True)
    st.write("Simula la conexión del cliente o creador con la testnet de Monad.")
    
    if not st.session_state.wallet_connected:
        if st.button("🔌 Conectar MetaMask / Monad Wallet"):
            st.session_state.wallet_connected = True
            st.session_state.user_address = "0x71C4B...3A90"
            st.rerun()
    else:
        st.success(f"🔗 Wallet Active: {st.session_state.user_address}")
        if st.button("❌ Desconectar Billetera"):
            st.session_state.wallet_connected = False
            st.rerun()
            
    st.markdown("---")
    st.markdown("💡 **Tip para la Demo:** Conectá la billetera para habilitar el formulario de registro y los botones de feedback.")

# ==========================================
# 5. DISEÑO DE COLUMNAS PRINCIPALES (PANEL DIVIDIDO)
# ==========================================
col_registro, col_dashboard = st.columns([1, 2], gap="large")

# ------------------------------------------
# COLUMNA IZQUIERDA: FORMULARIO DE REGISTRO
# ------------------------------------------
with col_registro:
    st.markdown("### 📝 Registrar Nuevo Agente")
    st.write("Los desarrolladores pueden registrar sus bots de IA asignándoles una firma criptográfica única de identidad.")
    
    if not st.session_state.wallet_connected:
        st.info("⚠️ Conectá tu billetera en la barra lateral para registrar un nuevo bot autónomo on-chain.")
    else:
        # Formulario estructurado nativo de Streamlit
        with st.form("agent_registration_form", clear_on_submit=True):
            new_name = st.text_input("🤖 Nombre del Agente de IA", placeholder="Ej: FlashLoan-Bot")
            new_desc = st.text_area("📄 Descripción de Funciones", placeholder="Detalla qué tareas ejecuta de forma autónoma...")
            
            submit_reg = st.form_submit_button("🚀 Desplegar Identidad On-Chain")
            
            if submit_reg:
                if new_name and new_desc:
                    # Simulación perfecta de generación de ID (Hash criptográfico ficticio)
                    import random
                    mock_hash = "0x" + "".join(random.choices("abcdef0123456789", k=8)) + "...ef34"
                    
                    # Agregamos el nuevo agente al storage global
                    st.session_state.agents.append({
                        "id": mock_hash,
                        "name": new_name,
                        "description": new_desc,
                        "tasks": 0,
                        "reputation": 100 # Inicia con reputación perfecta
                    })
                    st.success(f"¡Agente '{new_name}' registrado exitosamente en Monad!")
                    st.rerun()
                else:
                    st.error("Por favor, completa todos los campos del formulario.")

# ------------------------------------------
# COLUMNA DERECHA: DASHBOARD Y MÉTRICAS REAL-TIME
# ------------------------------------------
with col_dashboard:
    st.markdown("### 🤖 Registro de Reputación Activo")
    st.write("Lista inmutable de identidades. Los scores varían en tiempo real según el éxito de sus auditorías DeFi.")
    
    for idx, agent in enumerate(st.session_state.agents):
        # Creamos un bloque contenedor visual (Tarjeta) usando HTML inyectado de forma segura
        st.markdown(f"""
        <div class="agent-card">
            <div style="display: flex; justify-content: space-between; align-items: center;">
                <h3 style="margin: 0; color: #ffffff;">🤖 {agent['name']}</h3>
                <span style="padding: 4px 10px; border-radius: 4px; font-size: 12px; font-weight: bold;
                    background-color: {'rgba(0, 255, 136, 0.1)' if agent['reputation'] > 70 else 'rgba(255, 71, 71, 0.1)'};
                    color: {'#00ff88' if agent['reputation'] > 70 else '#ff4747'};">
                    {'● ACTIVE & TRUSTED' if agent['reputation'] > 70 else '⚠️ HIGH RISK'}
                </span>
            </div>
            <p style="color: #8a8b94; font-size: 13px; margin: 5px 0 10px 0;">Agent Hash: <code>{agent['id']}</code></p>
            <p style="color: #e2e4e9; font-size: 14px; margin-bottom: 15px;">{agent['description']}</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Métricas alineadas dentro de la tarjeta
        m_col1, m_col2 = st.columns(2)
        with m_col1:
            st.metric(label="Operaciones Ejecutadas", value=agent['tasks'])
        with m_col2:
            st.metric(label="Score de Confianza", value=f"{agent['reputation']}%")
            
        # Barra de progreso de efectividad
        st.progress(agent['reputation'] / 100)
        
        # Botones de Interacción/Votación para la Demo
        v_col1, v_col2 = st.columns(2)
        with v_col1:
            if st.button(f"👍 Validar Operación Exitosa##{idx}"):
                if not st.session_state.wallet_connected:
                    st.warning("Conectá tu billetera para calificar.")
                else:
                    st.session_state.agents[idx]['tasks'] += 1
                    st.session_state.agents[idx]['reputation'] = min(100, agent['reputation'] + 3)
                    st.toast(f"Voto positivo enviado para {agent['name']}", icon="✅")
                    st.rerun()
        with v_col2:
            if st.button(f"👎 Reportar Error / Pérdida##{idx}"):
                if not st.session_state.wallet_connected:
                    st.warning("Conectá tu billetera para reportar.")
                else:
                    st.session_state.agents[idx]['tasks'] += 1
                    st.session_state.agents[idx]['reputation'] = max(0, agent['reputation'] - 7)
                    st.toast(f"Reporte de fallo registrado para {agent['name']}", icon="🚨")
                    st.rerun()
                    
        st.markdown("<br>", unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)

# ==========================================
# 6. SECCIÓN DE ANALÍTICAS GLOBAL (GRÁFICOS)
# ==========================================
st.markdown("---")
st.markdown("### 📊 Análisis Comparativo de Confiabilidad")
st.write("Mapeo en tiempo real del ecosistema de agentes. Las barras se recalculan automáticamente con cada interacción on-chain.")

# 1. Extraemos los nombres y scores actuales de nuestro estado dinámico
nombres_bots = [agent['name'] for agent in st.session_state.agents]
scores_bots = [agent['reputation'] for agent in st.session_state.agents]

# 2. Creamos un diccionario plano compatible con los componentes de Streamlit
data_grafico = {
    "Score de Confianza (%)": scores_bots
}

# 3. Desplegamos el gráfico de barras nativo de alta velocidad
st.bar_chart(
    data=data_grafico,
    x=None, # Automáticamente usa los índices
    y="Score de Confianza (%)",
    x_label="Agentes Registrados",
    use_container_width=True
)

# Nota al pie para los evaluadores técnicos
st.caption("⚙️ Engine operando bajo el estándar descentralizado ERC-8004 en entornos de ejecución paralela Monad.")
