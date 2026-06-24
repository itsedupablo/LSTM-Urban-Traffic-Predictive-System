# **Sistema Predictivo del Tráfico Urbano basado en RNN (LSTM)**  
 ***Urban Traffic Activity Predictive System based on RNN (LSTM)***

<img width="2862" height="1538" alt="Captura de pantalla 2026-06-24 000247" src="https://github.com/user-attachments/assets/a31c8327-7604-4b08-8e52-a507df6e18c0" />


> ##### **Idiomas / Languages:** [Español](#español) | [English](#english)
> <a name="español"></a>
### 🇪🇸 Español
---
## Resumen
Este proyecto presenta el desarrollo de un sistema inteligente basado en redes neuronales LSTM capaz 
de predecir el comportamiento del tráfico con un horizonte de 24 horas en un punto específico de la 
autovía M-30, una de las arterias de tránsito vehicular más importantes de la ciudad de Madrid. Para 
ello se ha hecho uso de datos reales registrados durante el trimestre mayo - julio de 2025 por uno de 
los múltiples sensores de captación de datos de tráfico que conforman una extensa red IoT a lo largo 
de la ciudad: El sensor 3488, ubicado en el Nudo O'Donnell. 
Durante la etapa de desarrollo de este proyecto, se han diseñado, comparado y optimizado distintos 
diseños de arquitectura de red neuronal mediante el empleo de técnicas de aprendizaje automático. 
Los modelos evolucionaron progresivamente desde una arquitectura básica de una sola capa hasta 
una configuración multicapa que incorpora variables de contexto como el tipo de día, la franja horaria 
o la presencia de festivos. Para el entrenamiento y validación se utilizaron datos reales de intensidad, 
ocupación, velocidad y carga registrados por el sensor, con una granularidad de 15 minutos y una 
ventana temporal de 7 días. El sistema final supera el 90% de precisión media, con un coeficiente de 
determinación R² de 0,9738 y su mejor rendimiento relativo en las franjas de mayor afluencia y en 
escenarios de festivos y fines de semana. 
Como parte del trabajo se incluye además una interfaz interactiva inspirada en los centros de control 
modernos, que permite visualizar las predicciones generadas sobre un mapa de Madrid, acercando el 
sistema a un entorno de uso real. Los resultados obtenidos demuestran el potencial de este tipo de 
herramientas para mejorar la gestión proactiva de la movilidad urbana, sientan las bases de un sistema 
escalable y aplicable en entornos operativos reales.

## Hitos Técnicos y Resultados (Highlights)
*   **Arquitectura Avanzada:** Implementación de una **Stacked LSTM** multivariante capaz de capturar dependencias temporales jerárquicas (inercia inmediata vs. tendencias estacionales).
*   **Ingeniería de Características:** Integración de variables de contexto social (festivos, vísperas, horas punta) y normalización cíclica del tiempo.
*   **Alta Precisión:** Validación con datos reales del Sensor 3488 (M-30) obteniendo un **R² de 0,9738** y una precisión media del **90,38%**.
*   **Eficiencia Operativa:** Modelo optimizado para inferencia en **CPU estándar**, eliminando la necesidad de infraestructura costosa (GPU) en producción.

## Ecosistema Tecnológico
El proyecto ha sido desarrollado bajo una filosofía *Open Source*, garantizando su escalabilidad e interoperabilidad:
*   **Lenguaje:** Python 3.10. 
*   **Deep Learning:** TensorFlow / Keras.
*   **Procesamiento de Datos:** Pandas, NumPy, Scikit-Learn.
*   **Interfaz IHM:** Streamlit & PyDeck (Mapas 3D interactivos).

## Visualización de Resultados
### Dashboard de Control (IHM)
La interfaz permite a los operadores visualizar la predicción a 24 horas y la tendencia de las próximas 4 horas de forma intuitiva, con un mapa de calor dinámico sobre la ciudad de Madrid.
<img width="722" height="372" alt="image" src="https://github.com/user-attachments/assets/429b8a24-3e45-4f24-a77e-30defdb1ec83" />

### Rendimiento del Modelo PRO
Como se observa en las pruebas de validación, el sistema captura con precisión los picos de intensidad sin presentar el efecto de desfase (*lag*) común en modelos menos optimizados.
<img width="920" height="380" alt="image" src="https://github.com/user-attachments/assets/390ac384-c869-4ad9-ab37-2d76e75db464" />

### Instalación y Uso
1. **Clone the repo:** `git clone https://github.com/your-user/repo-name.git`
2. **Install requirements:** `pip install -r requirements.txt`
3. **Run the app:** `python -m streamlit run app.py`

### Licencia
**COPYRIGHT © 2025 PABLO EDU GARCÍA - TODOS LOS DERECHOS RESERVADOS.**
*Consulte el archivo [LICENSE](./LICENSE) para más detalles.*

---

<a name="english"></a>
## 🇺🇸 English
---
## Abstract
This project presents the development of an intelligent system based on LSTM neural networks 
capable of forecasting traffic tendencies over a 24-hour period at a specific point on the M-30 freeway, 
one of the most important traffic arteries in the city of Madrid. To this end, real-world data recorded 
during the May–July 2025 quarter was used, collected by one of the many traffic data sensors that 
make up an extensive IoT network throughout the city: Sensor 3488, located at the O’Donnell's traffic 
junction. 
During the development phase of this project, several neural network architecture designs were 
developed, compared, and optimized using machine learning techniques. The models evolved 
progressively from a basic single-layer architecture to a multi-layer configuration that incorporates 
contextual variables such as the type of day, the time slot, or the presence of holidays. For training and 
validation, real-world data on traffic intensity, occupancy, speed, and load recorded by the sensor were 
used, with a granularity of 15 minutes and a time window of 7 days. The final system achieves an 
average accuracy of over 90%, with a coefficient of determination R² of 0.9738, and its best relative 
performance is observed during peak traffic periods and on holidays and weekends. 
The project also includes an interactive interface inspired by modern control centers, which displays 
the generated predictions on a map of Madrid, bringing the system closer to a real-world application 
environment. The results obtained demonstrate the potential of this type of tool to improve proactive 
urban mobility management and lay the groundwork for a scalable system that can be applied in real
world operational environments. 

### Technical Highlights
*   **Advanced Architecture:** Implementation of a multivariate stacked LSTM capable of capturing hierarchical temporal dependencies (immediate inertia vs. seasonal trends).
*   **Feature Engineering:** Integration of social context variables (holidays, the day before holidays, peak hours) and cyclical normalization of time.
*   **High Accuracy:** Validation using real data from Sensor 3488 (M-30), yielding an R² of 0.9738 and an average accuracy of 90.38%.
*   **Operational Efficiency:** Model optimized for inference on a standard CPU, eliminating the need for costly infrastructure (GPUs) in production.

### Technological Environment
El proyecto ha sido desarrollado bajo una filosofía Open Source, garantizando su escalabilidad e interoperabilidad:
*   **Lenguage:** Python 3.10.
*   **Deep Learning:** TensorFlow / Keras.
*   **Data Processing: Pandas, NumPy, Scikit-Learn.
*   **Dashboard (UX/UI):** Streamlit & PyDeck (3D interactive maps) & CSS styling layer.

### Installation & Usage
1. **Clone the repo:** `git clone https://github.com/your-user/repo-name.git`
2. **Install requirements:** `pip install -r requirements.txt`
3. **Run the app:** `python -m streamlit run app.py`

### License
**COPYRIGHT © 2025 PABLO EDU GARCÍA - ALL RIGHTS RESERVED.**
*Refer to the [LICENSE](./LICENSE) file for more details.*
