# 🏢 CondoPortal

**Sistema integral de gestión de condominios con diseño moderno y funcionalidades avanzadas**

## 🌟 Características Principales

### 🎨 **Diseño & UX**
- **Paleta de colores profesional** con tonalidades café claras
- **Tema claro/oscuro** con persistencia en localStorage  
- **Diseño responsive** optimizado para móviles y desktop
- **Efectos glassmorphism** y gradientes modernos
- **Animaciones suaves** y microinteracciones

### 📱 **Páginas Incluidas**

#### **Landing Page (`index.html`)**
- Hero section con call-to-action
- Sección de amenidades premium
- **Mapa interactivo** de Polanco con POIs usando Leaflet.js
- **Marketplace de vecinos** con 6 negocios reales
- Footer completo con enlaces

#### **Sistema de Login (`login.html`)**
- Diseño split-screen vanguardista
- Autenticación demo integrada
- Elementos floating decorativos
- Validación de credenciales

#### **Dashboard (`app.html`)**
- **KPIs animados** con contadores dinámicos
- **Gráfico de flujo de caja** dibujado con Canvas API
- **Actividad en tiempo real** con sistema de refresh
- **4 secciones** (Dashboard, Gastos, Pagos, Estados, Negocios, Admin)
- **Sistema de pestañas** interactivo

## 🚀 **Tecnologías Utilizadas**

- **Frontend**: HTML5, CSS3, JavaScript ES6+
- **Mapas**: Leaflet.js con tiles de CartoDB
- **Gráficos**: Canvas API nativo
- **Iconografía**: Emojis y símbolos Unicode
- **Fuentes**: Inter (Google Fonts)

## 🎯 **Funcionalidades Demo**

### **Credenciales de Acceso**
```
Email: demo@condoportal.mx
Contraseña: Demo123!
```

### **Marketplace de Vecinos**
- 👨‍🍳 Chef Personal - Ana García (4.9⭐)
- 🧘‍♀️ Yoga & Mindfulness - María Fernández (4.8⭐)  
- 🐕 Cuidado de Mascotas - Carlos Ruiz (5.0⭐)
- 📚 Tutorías Académicas - Dr. Roberto López (4.9⭐)
- 📸 Fotografía Profesional - Sofía Martín (4.7⭐)
- 🔧 Reparaciones del Hogar - Ing. Miguel Torres (4.9⭐)

### **Dashboard Interactivo**
- Contadores animados de KPIs
- Gráfico de barras de flujo de caja
- Timeline de actividad reciente
- Barras de progreso animadas
- Proyecciones financieras

## 🏗️ **Estructura del Proyecto**

```
condominios/
├── index.html          # Landing page principal
├── login.html          # Sistema de autenticación
├── app.html           # Dashboard de administración  
├── base.css           # Estilos base y componentes
├── theme.css          # Temas claro/oscuro
├── landing.css        # Estilos específicos del landing
├── app.js             # Funcionalidad JavaScript
└── assets/
    └── img/
        └── logo.svg   # Logo del proyecto
```

## 🌍 **Mapa Interactivo**

**Ubicación**: Polanco V Sección, CDMX  
**Coordenadas**: [19.4326, -99.1915]

**Puntos de Interés**:
- 🚇 Metro Polanco (5 min caminando)
- 🛍️ Antara Fashion Hall (8 min caminando)  
- 🏛️ Museo Nacional de Antropología (12 min)
- 🌳 Bosque de Chapultepec (15 min)

## 🎨 **Paleta de Colores**

### **Tema Claro**
- **Fondo**: `#fdfcfa` → `#f5f0e8`
- **Primario**: `#a0734f` → `#c2956f`
- **Texto**: `#2d1810`
- **Superficie**: `rgba(255,255,255,0.7)`

### **Tema Oscuro**  
- **Fondo**: `#2c1810` → `#3d2818`
- **Primario**: `#a0734f` → `#c2956f`
- **Texto**: `#f4f1ec`
- **Superficie**: `rgba(160,115,79,0.15)`

## 🚀 **Instalación y Uso**

1. **Clonar el repositorio**:
```bash
git clone https://github.com/Teteocan-Technologies/Condominios.git
cd Condominios
```

2. **Abrir en navegador**:
```bash
# Opción 1: Abrir directamente
open index.html

# Opción 2: Servidor local (recomendado)
python -m http.server 8000
# Ir a http://localhost:8000
```

3. **Navegar por la aplicación**:
   - Inicia en `index.html` (landing page)
   - Haz clic en "Iniciar sesión" 
   - Usa las credenciales demo para acceder al dashboard

## 🔧 **Desarrollo**

### **Estructura CSS**
- `base.css`: Variables CSS, reset, componentes base
- `theme.css`: Variaciones de tema claro/oscuro  
- `landing.css`: Estilos específicos del landing page

### **JavaScript Modular**
- Router simple para navegación SPA
- Sistema de pestañas dinámico
- Animaciones de contadores y gráficos
- Gestión de temas y localStorage

## 📊 **Métricas del Proyecto**

- **Archivos**: 8 archivos principales
- **Líneas de código**: ~3,500 líneas
- **Imágenes**: Integración con Unsplash API
- **Performance**: Optimizado para carga rápida
- **Responsive**: 100% compatible móvil/tablet/desktop

## 🏆 **Características Avanzadas**

- ✅ **Mapa interactivo** con marcadores personalizados
- ✅ **Gráficos Canvas** dibujados dinámicamente  
- ✅ **Animaciones CSS/JS** sincronizadas
- ✅ **Sistema de temas** persistente
- ✅ **Marketplace** con ratings y reseñas
- ✅ **Dashboard** con datos en tiempo real
- ✅ **Navegación SPA** sin recarga de página

## 🎯 **Casos de Uso**

- **Administradores**: Gestión completa del condominio
- **Residentes**: Acceso a servicios y pagos
- **Proveedores**: Marketplace para ofrecer servicios
- **Visitantes**: Información del desarrollo inmobiliario

---

**Desarrollado por**: Teteocan Technologies  
**Versión**: 1.0.0  
**Licencia**: MIT

🌟 **¡Dale una estrella si te gusta el proyecto!**
