# -*- coding: utf-8 -*-
"""
Copyright ©  2025-2026 Pablo Edu García
Este código fuente es software libre: puedes redistribuirlo y/o modificarlo bajo los términos de la GNU General Public License versión 3 (GPL v3).
"""

import streamlit as st
import pandas as pd
import pydeck as pdk
import numpy as np
import joblib
import tensorflow as tf
from datetime import datetime, timedelta
import altair as alt

# 1. CONFIGURACIÓN DE PÁGINA 
st.set_page_config(
    page_title="Centro de Control de Tráfico · Madrid",
    page_icon="🚦",
    layout="wide"
)

# 2. INYECCIÓN DE ESTILOS UNIFICADOS
def load_css(path: str):
    try:
        with open(path, "r", encoding="utf-8") as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    except Exception as e:
        st.error(f"[ERROR] Error al cargar la hoja de estilos: {e}")

load_css("styles/main.css")

# Ajuste estricto del contenedor principal para evitar scroll horizontal
st.markdown("""
<style>
  .main .block-container {
    max-width: 100% !important;
    padding-top: 1.5rem !important;
    padding-bottom: 1.5rem !important;
    padding-left: 2rem !important;
    padding-right: 2rem !important;
  }
</style>
""", unsafe_allow_html=True)

# 3. CARGA OPTIMIZADA DE RECURSOS IA
@st.cache_resource
def load_resources():
    model = tf.keras.models.load_model('models/traffic_model_pro2.0.keras')
    scaler = joblib.load('models/scaler_pro2.0.pkl')
    df = pd.read_csv('data/datos_procesados2.csv', index_col=0, parse_dates=True)
    columnas = joblib.load('models/columnas_pro2.0.pkl')
    return model, scaler, df, columnas

try:
    model, scaler, df, columnas_input = load_resources()
    fecha_inicio_test = datetime(2025, 7, 13).date() 
    fecha_fin_test = df.index.max().date()
except Exception as e:
    st.error(f"[ERROR] Error crítico en la carga de modelos neuronales: {e}")
    st.stop()

# 4. CONFIGURACIÓN SEMÁNTICA DE ESTADOS (SCADA COLOR)
def get_status_config(pred):
    if pred <= 100:
        return {"color": [144, 238, 144], "hex": "#90ee90", "label": "FLUIDO (Muy Bajo)"}
    elif pred <= 500:
        return {"color": [52, 211, 153],  "hex": "#34d399", "label": "FLUIDO"}
    elif pred <= 1000:
        return {"color": [16, 185, 129],  "hex": "#10b981", "label": "ESTABLE"}
    elif pred <= 2000:
        return {"color": [245, 158, 11],  "hex": "#f59e0b", "label": "LENTO"}
    elif pred <= 3000:
        return {"color": [234, 179, 8],   "hex": "#eab308", "label": "RETENCIONES"}
    elif pred <= 5000:
        return {"color": [249, 115, 22],  "hex": "#f97316", "label": "CONGESTIÓN"}
    else:
        return {"color": [239, 68, 68],   "hex": "#ef4444", "label": "SATURACIÓN"}

# 5. MOTOR DE INFERENCIA DE RED NEURAL 
def predecir(fecha_busqueda):
    try:
        idx = df.index.get_loc(fecha_busqueda)
        ventana = df.iloc[idx - 672 : idx][columnas_input].values
        ventana_scaled = scaler.transform(ventana).reshape(1, 672, len(columnas_input))
        pred_norm = model.predict(ventana_scaled, verbose=0)
        dummy = np.zeros((1, len(columnas_input)))
        dummy[0, 0] = pred_norm[0, 0]
        return int(abs(scaler.inverse_transform(dummy)[0, 0]))
    except: 
        return None

# 6. PANEL DE CONTROL LATERAL (NATIVO SLIDING)
st.sidebar.title("Control de Tráfico M-30 🚦")
st.sidebar.markdown("<p style='opacity:0.6; font-size:12px; margin-top:-15px; margin-bottom:25px;'>Ayuntamiento de Madrid · Plataforma Operativa</p>", unsafe_allow_html=True)

# Selección de Nodo con restricciones visuales directas
# Diccionario con los distritos de Madrid 
DISTRITOS_MADRID = {
    4: "4-Salamanca",
    1: "1-Centro",
    2: "2-Arganzuela",
    3: "3-Retiro",
    5: "5-Chamartín",
    6: "6-Tetuán",
    7: "7-Chamberí",
    8: "8-Fuencarral-El Pardo",
    9: "9-Moncloa-Aravaca",
    10:"10-Latina",
    11:"11-Carabanchel",
    12:"12-Usera",
    13:"13-Puente de Vallecas",
    14:"14-Moratalaz",
    15:"15-Ciudad Lineal",
    16:"16-Hortaleza",
    17:"17-Villaverde",
    18:"18-Villa de Vallecas",
    19:"19-Vicálvaro",
    20:"20-San Blas-Canillejas",
    21:"21-Barajas"
}

st.sidebar.markdown("### Ubicación")

# Selector de Distrito en la barra lateral
id_distrito_seleccionado = st.sidebar.selectbox(
    "Distrito de Madrid:",
    options=list(DISTRITOS_MADRID.keys()),
    format_func=lambda x: DISTRITOS_MADRID[x] if x == 4 else f"{DISTRITOS_MADRID[x]} [🔒 Bloqueado]"
)

# Coordenadas Sensor 3488
lon, lat = -3.659420, 40.421756 

# Control de flujo dentro de la barra lateral
if id_distrito_seleccionado != 4:
    st.sidebar.error("[INFO] Este distrito está bloqueado en el MVP. Selecciona 'Salamanca'.")
    sensor_seleccionado = None
else:
    # Si elige Salamanca, se desbloquea de forma estricta el único sensor del estudio
    sensor_seleccionado = st.sidebar.selectbox(
        "Sensor Disponible:",
        options=[3488],
        format_func=lambda x: f"Sensor Estudio - ID: {x}",

    )


st.sidebar.markdown("<label class='sidebar-label'>📅 FECHA DE CONSULTA</label>", unsafe_allow_html=True)
fecha_user = st.sidebar.date_input("Fecha", value=fecha_fin_test, min_value=fecha_inicio_test, max_value=fecha_fin_test, label_visibility="collapsed")

# Selector Horario Inteligente en intervalos de 15 minutos (96 pasos diarios)
# 1. Generamos los intervalos de 15 minutos en formato texto HH:MM
start_time = datetime.strptime("00:00", "%H:%M")
time_options = [
    (start_time + timedelta(minutes=i)).strftime("%H:%M") 
    for i in range(0, 24 * 60, 15)
]

# 2. Lo pintamos estrictamente EN LA BARRA LATERAL
hora_seleccionada = st.sidebar.select_slider(
    "Selecciona la hora de análisis:",
    options=time_options,
    value="08:00"  # Hora por defecto
)
fecha_final = pd.to_datetime(f"{fecha_user} {hora_seleccionada}:00")

# Escala visual integrada limpia
st.sidebar.markdown("<label class='sidebar-label' style='margin-top:25px;'>📊 ESCALA DE INTENSIDAD</label>", unsafe_allow_html=True)
st.sidebar.markdown("""
<div class="leyenda-box">
    <div class="leyenda-item"><span style='color:#90ee90'>●</span> 0 - 100: Muy bajo</div>
    <div class="leyenda-item"><span style='color:#34d399'>●</span> 100 - 500: Fluido</div>
    <div class="leyenda-item"><span style='color:#10b981'>●</span> 500 - 1000: Estable</div>
    <div class="leyenda-item"><span style='color:#f59e0b'>●</span> 1000 - 2000: Lento</div>
    <div class="leyenda-item"><span style='color:#eab308'>●</span> 2000 - 3000: Retenciones</div>
    <div class="leyenda-item"><span style='color:#f97316'>●</span> 3000 - 5000: Congestión</div>
    <div class="leyenda-item"><span style='color:#ef4444'>●</span> > 5000: Saturación</div>
</div>
""", unsafe_allow_html=True)

# 7. CUERPO PRINCIPAL DEL DASHBOARD 
st.title("Centro de Control de Tráfico: Madrid")
st.markdown(f"<p class='main-subtitle'>Punto Analizado: Enlace Puente de Ventas (<strong>{sensor_seleccionado}</strong>) | Corte Temporal: {fecha_final.strftime('%d/%m/%Y - %H:%M h')}</p>", unsafe_allow_html=True)

prediccion = predecir(fecha_final)

if prediccion is not None:
    config = get_status_config(prediccion)
    col_map, col_info = st.columns([2.3, 1])
    
    with col_map:
        st.markdown("<p class='section-title'> PERSPECTIVA URBANA DE RED MADRID </p>", unsafe_allow_html=True)
        
        # --- MAPA CORREGIDO - SIN TEXTO ---
        sensor_data_limpia = [{
            "position": [lon, lat],
            "color": config["color"] + [200],
            "radius": 110,
            "sensor_id": sensor_seleccionado,
            "flujo": f"{prediccion} veh/h",
            "estado": config["label"]
        }]
        
        layer_centro = pdk.Layer(
            "ScatterplotLayer",
            data=sensor_data_limpia,
            get_position="position",
            get_fill_color="color",
            get_radius="radius",
            pickable=True,
            auto_highlight=True
        )
        
        view_state = pdk.ViewState(
            latitude=lat,
            longitude=lon,
            zoom=15.2,
            pitch=45,
            bearing=-10
        )
        
        deck = pdk.Deck(
            map_style='https://basemaps.cartocdn.com/gl/dark-matter-gl-style/style.json',
            initial_view_state=view_state,
            layers=[layer_centro],
            map_provider='carto'
        )
        
        st.pydeck_chart(deck, use_container_width=True)

    with col_info:
        st.markdown("<p class='section-title'>📊 MÉTRICAS DE OPERACIÓN</p>", unsafe_allow_html=True)
        
        # --- TARJETA DE MÉTRICAS CORREGIDA (usando st.html si está disponible) ---
        # Definimos el HTML de la tarjeta
        html_metric = f"""
        <div class="metric-card" style="border-left: 6px solid {config['hex']};">
            <span class="card-label">CAUDAL PREDICTIVO</span>
            <div class="card-value">{prediccion} <span class="card-unit">veh/h</span></div>
            <div class="card-status" style="color: {config['hex']};">{config['label']}</div>
        </div>
        """
        # Intentamos usar st.html (Streamlit 1.38+)
        try:
            st.html(html_metric)
        except AttributeError:
            # Fallback a st.markdown con unsafe_allow_html
            st.markdown(html_metric, unsafe_allow_html=True)
        # ------------------------------------------------
        
        st.markdown("<p class='section-title' style='margin-top: 25px;'>📈 TENDENCIA PRÓXIMAS 4 HORAS</p>", unsafe_allow_html=True)
        
        proximas_preds = []
        for i in range(1, 5):
            f_next = fecha_final + timedelta(hours=i)
            p = predecir(f_next)
            if p: 
                proximas_preds.append({
                    "Hora": f_next.strftime("%H:%M"), 
                    "Vehículos": p
                })
        
        # --- GRÁFICO CORREGIDO ---
        if proximas_preds:
            df_trend = pd.DataFrame(proximas_preds)
            
            chart = alt.Chart(df_trend).mark_line(
                point=True,
                strokeWidth=3,
                color=config['hex']
            ).encode(
                x=alt.X('Hora:N', title=None, axis=alt.Axis(labelColor='rgba(240,242,255,0.7)', labelFontSize=11)),
                y=alt.Y('Vehículos:Q', title=None, axis=alt.Axis(labelColor='rgba(240,242,255,0.7)', labelFontSize=11))
            ).properties(
                height=160,
                background='rgba(22, 28, 45, 0.7)'
            ).configure_view(
                strokeWidth=0,
                cornerRadius=12
            ).configure(
                background='rgba(22, 28, 45, 0.7)'
            )
            
            st.altair_chart(chart, use_container_width=True)
            
       
else:
    st.markdown("""
    <div class="error-box">
        [ERROR] Error en análisis temporal: Ventana temporal fuera de los rangos válidos del modelo predictivo.
    </div>
    """, unsafe_allow_html=True)
