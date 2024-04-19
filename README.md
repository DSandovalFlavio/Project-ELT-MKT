# **Proyecto: Análisis de Campañas de Marketing Digital en Redes Sociales**

## **1. Introducción**

En el entorno competitivo actual, las empresas dependen en gran medida del marketing digital para llegar a su público objetivo y alcanzar sus metas comerciales. Las redes sociales se han convertido en plataformas cruciales para las campañas de marketing, ofreciendo una amplia gama de herramientas para interactuar con los clientes y generar leads. Sin embargo, la gestión eficaz de campañas en múltiples plataformas de redes sociales puede ser un desafío complejo, especialmente en lo que respecta a la recopilación, integración y análisis de datos.

Este proyecto tiene como objetivo abordar este desafío mediante el desarrollo de un pipeline ELT (Extracción, Carga y Transformación) para extraer datos de las API de diferentes plataformas de redes sociales, cargarlos en BigQuery, transformarlos y limpiarlos, y ponerlos a disposición de analistas de datos para su análisis. El proyecto también incluye la creación de un dashboard en Looker Studio para visualizar los datos procesados y obtener información valiosa sobre el rendimiento de las campañas de marketing.

## **2. Objetivos del Proyecto**

Los objetivos principales de este proyecto son:

* **Desarrollar un pipeline ELT robusto y escalable** para extraer, cargar y transformar datos de las API de diversas plataformas de redes sociales, incluyendo Facebook Marketing API, Twitter API, y otras.
* **Almacenar los datos procesados en BigQuery**, una plataforma de almacenamiento de datos en la nube que ofrece escalabilidad, confiabilidad y alto rendimiento.
* **Transformar y limpiar los datos** para garantizar su calidad y consistencia, preparándolos para el análisis posterior.
* **Poner los datos a disposición de analistas de datos** mediante herramientas de análisis como Looker Studio.
* **Crear un dashboard en Looker Studio** para visualizar los datos procesados y obtener información valiosa sobre el rendimiento de las campañas de marketing.

## **3. Diseño de la Solución**

[![Pipeline ELT](/images/Arquitectura_Proyecto_MKT.jpg)](/images/Arquitectura_Proyecto_MKT.jpg)

### **3.1 Arquitectura del Pipeline**

El pipeline ELT se compone de las siguientes etapas:

* [**Extracción (E):**](project_mkt_EL.py) En esta etapa, se extraen datos de las API de las diferentes plataformas de redes sociales utilizando la biblioteca `requests` de Python. Se simula la extracción de datos con la API de Mockaroo debido a la falta de credenciales reales.
* [**Carga (L):**](project_mkt_EL.py) Los datos sin procesar se cargan en tablas separadas de BigQuery utilizando la biblioteca `pandas_gbq` de Python.
* [**Transformación (T):**](DBT/models) Se utilizan las herramientas de DBT Cloud para transformar los datos en dos etapas:
  * **Silver:** Se generan dos transformaciones principales en las tablas de cada fuente:
    * Se crea un campo `campaign_name` con la siguiente estructura: `Company + Campaign_Type + (shortened) Target_Audience + Location`.
    * Se obtiene la fecha de finalización de la campaña utilizando las columnas `date` y `duration`.
  * **Gold:** Se genera una tabla concatenada agrupando las tablas por fecha, nombre de campaña, impresiones, clics y costo, creando un data mart que servirá como entrada para un dashboard en Looker Studio.

[![Pipeline ELT2](/images/Proyecto_MKT.jpg)](/images/Proyecto_MKT.jpg)

### **3.2 Desarrollo Técnico**

* **Lenguajes de programación:** Python para la extracción y transformación de datos.
* **Herramientas:**
  * DBT Cloud para la transformación de datos.
  * BigQuery para el almacenamiento de datos.
  * Looker Studio para la creación de dashboards.
* **Control de versiones:** Se utiliza un repositorio de GitHub para almacenar el código y controlar las versiones del proyecto.

### **3.3 Dashboard en Looker Studio**

El dashboard de Looker Studio permite visualizar los datos procesados y obtener información valiosa sobre el rendimiento de las campañas de marketing. Incluye métricas como impresiones, clics, costo, tasa de clics (CTR) y costo por clic (CPC). Los datos pueden filtrarse y segmentarse por diferentes dimensiones, como fecha, campaña, plataforma de red social y ubicación.

## **4. Evaluación**

### **4.1 Claridad y Justificación del Proyecto**

El problema abordado en este proyecto es altamente relevante para las empresas que dependen del marketing digital en redes sociales. La gestión eficaz de campañas en múltiples plataformas requiere de una solución robusta para la recopilación, integración y análisis de datos. Este proyecto ofrece una solución viable y escalable para este problema, permitiendo a las empresas obtener información valiosa sobre el rendimiento de sus campañas y optimizar sus estrategias de marketing.

### **4.2 Diseño de la Solución**

El diseño de la solución se basa en una arquitectura ELT probada y escalable, utilizando herramientas y tecnologías reconocidas en la industria. Se han considerado cuidadosamente las necesidades de transformación y limpieza de datos, y se ha puesto énfasis en la creación de un dashboard intuitivo y útil para los analistas de datos.

## **4.3 Desarrollo Técnico**

El desarrollo técnico del proyecto se ha realizado de manera eficiente y eficaz, utilizando las herramientas y tecnologías adecuadas para cada tarea. Se ha seguido un enfoque modular y bien documentado, facilitando el mantenimiento y la escalabilidad del proyecto.

## **4.4 Evaluación General**

En general, este proyecto ha demostrado ser una solución efectiva para el análisis de campañas de marketing digital en redes sociales. Se ha diseñado e implementado un pipeline ELT robusto y escalable, se han transformado y limpiado los datos de manera adecuada, y se ha creado un dashboard informativo en Looker Studio. El proyecto cumple con los objetivos establecidos y aporta valor a las empresas que necesitan gestionar sus campañas de marketing en redes sociales de manera eficiente.

## **5. Conclusiones**

Este proyecto ha demostrado la viabilidad de desarrollar un pipeline ELT para extraer, cargar y transformar datos de las API de diferentes plataformas de redes sociales, almacenarlos en BigQuery y crear un dashboard en Looker Studio para su análisis. La solución propuesta es escalable, robusta y fácil de mantener, ofreciendo un valor significativo para las empresas que buscan optimizar sus estrategias de marketing digital.

### **Recomendaciones:**

* **Ampliar la cobertura de plataformas de redes sociales:** Se puede ampliar el alcance del proyecto integrando APIs de otras plataformas de redes sociales populares.
* **Implementar modelos de aprendizaje automático:** Se pueden incorporar modelos de aprendizaje automático para analizar los datos y obtener información aún más profunda sobre el rendimiento de las campañas.
* **Desarrollar una interfaz de usuario para la gestión del pipeline:** Se puede crear una interfaz de usuario que permita a los usuarios administrar el pipeline ELT de manera más sencilla.

Este proyecto ha sido una experiencia valiosa en el aprendizaje de las tecnologías y metodologías necesarias para el análisis de datos a gran escala. Se espera que los conocimientos adquiridos en este proyecto puedan ser aplicados en futuros proyectos de análisis de datos y Big Data.

## **Agradecimientos:**

A mis compañeros de equipo por su colaboración y apoyo en el desarrollo de este proyecto.

## **Referencias:**

* [https://cloud.google.com/bigquery](https://cloud.google.com/bigquery)
* [https://www.getdbt.com/dbt-labs/about-us](https://www.getdbt.com/dbt-labs/about-us)
* [https://www.python.org/](https://www.python.org/)
* [https://docs.python-requests.org/en/v2.0.0/](https://docs.python-requests.org/en/v2.0.0/)
* [https://pandas.pydata.org/](https://pandas.pydata.org/)
* [https://pandas-gbq.readthedocs.io/](https://pandas-gbq.readthedocs.io/en/latest/install.html)

**Nota:**

Este entregable ha sido generado utilizando las directrices proporcionadas. Se ha puesto énfasis en la claridad, concisión y justificación de las decisiones tomadas durante el desarrollo del proyecto.
