# 🌱 Sistema Automatizado de Monitoreo Ambiental y QA/QC Analítico

Este proyecto es una plataforma interactiva diseñada para laboratorios analíticos y consultoras ambientales. Permite automatizar la ingesta de datos de monitoreo en formato Excel, realizar la homologación de parámetros según la normativa peruana, aplicar tratamiento estadístico y evaluar el cumplimiento en tiempo real frente a los Estándares de Calidad Ambiental (ECA).

## 🚀 Características Clave

* **Homologación de Parámetros:** Reconoce sinónimos comunes de laboratorio (ej. pH, cd, pb y otros parámetros) y los estandariza automáticamente a los nombres oficiales regulatorios.
* **Evaluación Normativa Dinámica:** Permite alternar entre diferentes normativas mediante un menú interactivo:
  * ECA Agua Subcategoría A1 (Agua Potable)
  * ECA Agua Subcategoría D1 (Riego y Bebida de Animales)
  * ECA Aguas Residuales Domésticas (LMP PTAR)
* **Tratamiento Químico-Analítico:** Procesa e imputa automáticamente valores especiales de laboratorio como los límites de detección (<LOD), reemplazándolos matemáticamente para evitar quiebres en las tendencias estadísticas.
* **Dashboard Operativo:** Despliega métricas de control en tiempo real (KPIs) con códigos de color de cumplimiento y gráficos de tendencias dinámicos e interactivos desarrollados con **Plotly**.
* **Exportación Automatizada:** Genera reportes técnicos ejecutivos en formato Excel (.xlsx) aplicando estilos corporativos y formato condicional (celdas fuera de norma en rojo) de manera segura con **OpenPyXL**.

## 🛠️ Tecnologías Utilizadas

* **Python 3.12+**
* **Streamlit** (Interfaz web interactiva)
* **Pandas** y **NumPy** (Procesamiento analítico y limpieza de datos)
* **Plotly** (Gráficos estadísticos e interactivos)
* **OpenPyXL** (Inyección de estilos y generación de reportes en hojas de cálculo)

## 📦 Instalación y Uso Local

1. **Clona este repositorio:**
  '''bash
   git clone https://github.com
   cd monitoreo-calidad-agua
   '''

2. **Instala las dependencias requeridas:**
   '''bash
   pip install -r requirements.txt
   '''

3. **Ejecuta el Dashboard interactivo:**
   '''bash
   streamlit run app.py
   '''

## 📊 Formato de Datos Soportado
La aplicación acepta archivos Excel que contengan las columnas 'Fecha', 'Estación', y parámetros fisicoquímicos o metales pesados como 'pH', 'Cadmio' y 'Plomo'. Soporta lecturas cuantitativas directas o cualitativas mixtas de laboratorio del tipo '<LOD'.
