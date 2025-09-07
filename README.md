# 🛸 Monero Node Alien Dashboard

Un dashboard con tema extraterrestre para monitorear datos de un nodo Monero en tiempo real.

## 🚀 Características

- **Tema Alien**: Diseño futurista con efectos visuales extraterrestres
- **Actualización en Tiempo Real**: Los datos se actualizan automáticamente cada 10 segundos
- **Métricas Completas**: Muestra información detallada del nodo Monero:
  - Estado de sincronización
  - Altura de bloque actual
  - Conexiones activas
  - Información del último bloque
  - Estimaciones de comisiones
  - Hash rate de la red
  - Tamaño de base de datos

## 📋 Requisitos

- Python 3.7+
- Nodo Monero ejecutándose en `192.168.122.185:18081` (contenedor Docker)
- Túnel SSH hacia la VM con el nodo Monero
- Dependencias Python: Flask, requests

## 🛠 Instalación y Ejecución

1. **Establecer túnel SSH al nodo Monero:**
   ```bash
   # Conectar con túnel de puerto desde tu máquina local
   ssh -L 18081:172.18.0.4:18081 user1@192.168.122.185
   # Mantener esta conexión activa en una terminal separada
   ```

2. **Instalar dependencias (en otra terminal):**
   ```bash
   cd /home/user1/syslab-nosync/1-projects/0-claude-demo-1
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

3. **Ejecutar el dashboard:**
   ```bash
   # Opción 1: Usando el script
   ./run.sh
   
   # Opción 2: Directamente con Python
   source venv/bin/activate
   python app.py
   ```

4. **Acceder al dashboard:**
   - Abrir navegador web en: `http://localhost:8282`
   - O desde otra máquina en la red: `http://[IP_DEL_SERVIDOR]:8282`

## 🌐 Endpoints API

- `GET /` - Dashboard principal
- `GET /api/data` - Datos JSON del nodo Monero
- `GET /api/health` - Estado de salud de la aplicación

## ⚙️ Configuración

El nodo Monero debe estar configurado para:
- Host: `192.168.122.185`
- Puerto: `18081` (puerto estándar)
- RPC habilitado

## 🔄 Frecuencias de Actualización

- **Información del nodo**: Cada 30 segundos
- **Información de bloques**: Cada 10 segundos
- **Conexiones**: Cada 60 segundos
- **Estimación de comisiones**: Cada 120 segundos
- **Dashboard web**: Cada 10 segundos

## 🎨 Características Visuales

- Animaciones de fondo alienígenas
- Efectos de brillo y pulsación
- Ojos alienígenas flotantes
- Esquema de colores verde neón
- Responsive design para móviles

## 🐛 Solución de Problemas

1. **Error de conexión al nodo**:
   - Verificar que el nodo Monero esté ejecutándose
   - Confirmar la IP y puerto del nodo
   - Verificar configuración de firewall

2. **Dependencias**:
   - Asegurar que el entorno virtual esté activado
   - Reinstalar dependencias: `pip install -r requirements.txt`

3. **Puerto ocupado**:
   - Cambiar puerto en `app.py` línea final: `app.run(host='0.0.0.0', port=NUEVO_PUERTO)`

## 📱 Compatibilidad

- Chrome/Chromium 90+
- Firefox 88+
- Safari 14+
- Edge 90+
- Responsive en dispositivos móviles