# Titanic_dashboard

## Portada del proyecto

Bienvenido al repositorio del primer proyecto del bootcamp CSIC Data&IA de Upgrade-Hub. Este trabajo presenta una aplicación interactiva (app.py) diseñada para explorar, visualizar y ofrecer análisis predictivo sobre los datos del Titanic. Actuando como project manager, este documento resume alcance, estructura, uso, resultados clave y próximos pasos.

## Objetivo
- Construir un dashboard interactivo que permita:
    - Explorar la base de datos del Titanic.
    - Visualizar relaciones entre variables (clase, sexo, edad, tarifa, etc.).
    - Entender factores asociados a la supervivencia.
    - Proporcionar un prototipo de modelo predictivo explicable.
- Entregar un primer proyecto robusto, reproducible y documentado dentro del bootcamp.

## Estructura del repositorio (resumen)
- app.py — aplicación principal (interfaz y lógica de visualización).
- data/ — datasets originales y procesados (CSV).
- notebooks/ — análisis exploratorio y experimentación con modelos.
- models/ — artefactos de modelos entrenados (si aplica).
- requirements.txt — dependencias del proyecto.
- README.md — este archivo de presentación.

## Cómo ejecutar (rápido)
1. Clonar el repositorio.
2. Crear y activar entorno virtual:
     - python -m venv .venv && source .venv/bin/activate (Linux/Mac) o .venv\Scripts\activate (Windows)
3. Instalar dependencias:
     - pip install -r requirements.txt
4. Ejecutar la aplicación:
     - python app.py
     - (o el comando específico de la framework usado: e.g., streamlit run app.py, según la implementación)
5. Abrir en el navegador la URL que se muestre en consola (localhost:port).

## Contenido funcional del dashboard
- Panel de control general con KPI:
    - Tasa global de supervivencia, por clase y por sexo.
- Filtros interactivos:
    - Clase, sexo, rango de edad, tarifa, puerto de embarque.
- Visualizaciones:
    - Distribuciones (histogramas, boxplots) y comparativas.
    - Mapas de calor de correlación y matrices de confusión (si hay modelo).
    - Gráficos de supervivencia por cohortes.
- Módulo de predicción:
    - Interfaz para ingresar características y obtener probabilidad de supervivencia.
    - Explicaciones locales (ej. SHAP/LIME) para interpretabilidad.
- Sección de metodología:
    - Resumen de limpieza, ingeniería de variables y métricas del modelo.

## Datos y preprocesamiento
- Origen: dataset clásico del Titanic (fuente pública).
- Pasos principales:
    - Tratamiento de valores faltantes (edad, tarifa, embarque).
    - Codificación de variables categóricas.
    - Creación de features útiles (familiares a bordo, título a partir de nombre).
    - Split para entrenamiento/validación y normalización cuando corresponde.
- Consideraciones éticas: se documenta limitación de datos y sesgos potenciales.

## Resultados clave (ejemplo)
- Impacto mayor en supervivencia: sexo (female advantage), clase socioeconómica y edad.
- El prototipo de modelo alcanza métricas razonables en validación (ver notebooks para detalles).
- El dashboard facilita identificar patrones y comunicar hallazgos a stakeholders.

## Calidad, reproducibilidad y pruebas
- Todos los pasos experimentales están documentados en notebooks.
- requirements.txt asegura entornos reproducibles.
- Se recomienda añadir CI (tests básicos) y scripts de linting en próximas iteraciones.

## Roadmap / Próximos pasos
- Mejorar UX del dashboard y añadir tests end-to-end.
- Desplegar en un servicio (Heroku, Render, Vercel, etc.) con CI/CD.
- Extender módulo predictivo con validación cruzada y calibración.
- Añadir más explicabilidad y exported reports automáticos.

## Contribuir
- Abrir issues para errores o mejoras.
- Enviar pull requests con descripción clara y tests cuando aplique.
- Seguir guía de estilo y buenas prácticas de commits.

## Créditos y licencia
- Primer proyecto del bootcamp CSIC Data&IA (Upgrade-Hub).
- Autores: equipo del bootcamp (detallar nombres en CONTRIBUTING o en la sección de créditos).
- Licencia: añadir LICENSE (recomendado MIT o acorde al equipo).

Contacto rápido: incluir correo o perfil de GitHub del equipo para consultas y demos.

Gracias por revisar este proyecto: objetivo logrado como entrega inicial del bootcamp y base sólida para iteraciones futuras.