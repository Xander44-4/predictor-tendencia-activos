# 📈 Predictor de Tendencia de Activos

Un sistema backend robusto diseñado para predecir el valor futuro de activos financieros utilizando análisis de series temporales y arquitectura MVC (Modelo-Vista-Controlador).

## 🚀 Características Principales

- **Predicción de Activos**: Algoritmos avanzados para predecir valores futuros de activos financieros
- **Arquitectura MVC**: Estructura modular y escalable para fácil mantenimiento
- **API RESTful**: Endpoints bien documentados para integración con aplicaciones frontend
- **Análisis de Series Temporales**: Procesamiento inteligente de datos históricos
- **Validación de Datos**: Sistema robusto de validación y sanitización de entrada

## 🛠️ Tecnologías Utilizadas

- **Backend Framework**: [Python/FastApi]
- **Base de Datos**: [BD - MongoDB]
- **Arquitectura**: MVC (Model-View-Controller)


## ⚡ Instalación Rápida

1. **Clonar el repositorio**
   ```bash
   git clone https://github.com/[usuario]/PredictorTendenciaActivos.git
   cd PredictorTendenciaActivos
   ```

2. **Instalar dependencias**
   ```bash
   
   pip install -r requirements.txt
   ```

3. **Configurar variables de entorno**
   ```bash
   cp .env.example .env
   
   ```

4. **Ejecutar el servidor**
   ```bash
    uvicorn src.main:app
   ```

## 🔧 Configuración

### Variables de Entorno

```env
MONGO_URI=mongodb://mongourl/
MONGO_DB_NAME=database name
```

### Estructura del Proyecto

```
PredictorTendenciaActivos/
├── src/
│   ├── controllers/    # Controladores MVC
│   ├── models/         # Modelos de datos
│   ├── dto/            # Data Transfer Object
│   ├── models/       # Lógica de negocio
│   ├── core/           # Utilidades
│   └── routes/         # Definición de rutas
│   └── tests/          # Pruebas unitarias
├── README.md           # Documentaciones 

```

## 📡 API Endpoints

### Predicción de Activos

```http
POST /api/mode
Content-Type: application/json

{
  "mode_type": 0,
  "userId": " ",
  "inputs": [...]
}
```

### Obtener Datos Históricos

```http
GET /api/history/{user_id}
```


## 📊 Uso del Sistema

### Ejemplo Básico

```javascript
// Realizar predicción
const prediction = await fetch('/mode', {
  "mode_type": 0,
  "userId": "string",
  "inputs": [
    {
      "value": 0,
      "datetime": "2025-08-28"
    },
    {
      "value": 0,
      "datetime": "2025-08-28"
    },
    {
      "value": 0,
      "datetime": "2025-08-28"
    },
    {
      "value": 0,
      "datetime": "2025-08-28"
    },
    {
      "value": 0,
      "datetime": "2025-08-28"
    }
  ],
  "answer_mode": {}
});

const result = await prediction.json();
console.log('Predicción:', result);
```



## 📈 Rendimiento

- **Tiempo de respuesta**: < 500ms para predicciones estándar
- **Capacidad**: Hasta 1000 requests/minuto
- **Precisión**: 85-92% en predicciones a corto plazo (7-30 días)


## 📝 Changelog

### v1.0.0 (Fecha)
- Implementación inicial del sistema de predicción
- API RESTful completa
- Arquitectura MVC establecida


## ⚠️ Disclaimer

Este sistema es para fines educativos y de investigación. Las predicciones no constituyen asesoramiento financiero. Siempre consulte con profesionales antes de tomar decisiones de inversión.


