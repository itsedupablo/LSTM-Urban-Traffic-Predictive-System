# **Sistema Predictivo del Tráfico Urbano basado en RNN (LSTM)** \n*Urban Traffic Activity Predictive System based on RNN (LSTM)*
----------------------------------------------------------------------------------------------------
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

----------------------------------------------------------------------------------------------------------------
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
