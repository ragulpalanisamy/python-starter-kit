# 🏗️ Full-Stack Architecture

> **Complete system architecture** - React + FastAPI + PySpark + PyTorch

---

## 🎯 System Overview

A modern full-stack application demonstrating:

- **Frontend**: React + TailwindCSS
- **Backend API**: FastAPI (Python)
- **Data Processing**: PySpark
- **Machine Learning**: PyTorch

```
┌─────────────────────────────────────────────────────────────┐
│                    USER BROWSER                              │
│                   (React + TailwindCSS)                      │
└────────────────────────┬────────────────────────────────────┘
                         │ HTTP/REST
                         ▼
┌─────────────────────────────────────────────────────────────┐
│                    FASTAPI BACKEND                           │
│                                                              │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐      │
│  │   Health     │  │  Data API    │  │   ML API     │      │
│  │  Endpoints   │  │  Endpoints   │  │  Endpoints   │      │
│  └──────────────┘  └──────────────┘  └──────────────┘      │
└────────────┬───────────────┬───────────────┬────────────────┘
             │               │               │
             ▼               ▼               ▼
    ┌──────────────┐ ┌──────────────┐ ┌──────────────┐
    │   External   │ │   PySpark    │ │   PyTorch    │
    │     APIs     │ │   Pipeline   │ │    Model     │
    └──────────────┘ └──────────────┘ └──────────────┘
```

---

## 📊 Data Flow

### Upload → Process → Predict → Display

```
1. User uploads CSV file
   ↓
2. Frontend sends to /api/v1/data/upload
   ↓
3. FastAPI saves file
   ↓
4. User triggers processing
   ↓
5. FastAPI calls PySpark pipeline
   ↓
6. PySpark cleans and transforms data
   ↓
7. Processed data saved
   ↓
8. User requests predictions
   ↓
9. FastAPI calls PyTorch model
   ↓
10. Model returns predictions
    ↓
11. Results sent to frontend
    ↓
12. React displays with charts
```

---

## 🎨 Frontend Architecture

### React + Vite + TailwindCSS

```
frontend/
├── src/
│   ├── App.jsx                 # Root component
│   ├── main.jsx                # Entry point
│   │
│   ├── pages/
│   │   ├── Dashboard.jsx       # Main dashboard
│   │   ├── DataProcessing.jsx  # Data upload & processing
│   │   └── MLPredictions.jsx   # Sentiment analysis
│   │
│   ├── components/
│   │   ├── layout/
│   │   │   ├── Header.jsx
│   │   │   ├── Sidebar.jsx
│   │   │   └── Layout.jsx
│   │   │
│   │   ├── data/
│   │   │   ├── DataUpload.jsx      # Drag & drop upload
│   │   │   ├── DataStats.jsx       # Statistics display
│   │   │   └── DataTable.jsx       # Data preview
│   │   │
│   │   ├── ml/
│   │   │   ├── SentimentInput.jsx  # Text input
│   │   │   ├── PredictionResult.jsx # Results display
│   │   │   └── BatchPredictor.jsx   # Batch predictions
│   │   │
│   │   └── common/
│   │       ├── Button.jsx
│   │       ├── Card.jsx
│   │       └── Loading.jsx
│   │
│   ├── api/
│   │   └── client.js           # Axios API client
│   │
│   └── utils/
│       └── formatters.js       # Data formatting
│
└── package.json
```

---

## 🔧 Backend Architecture

### FastAPI + PySpark + PyTorch

```
fastapi-starter/backend/
├── app/
│   ├── main.py                     # Application entry
│   ├── config.py                   # Configuration
│   │
│   ├── routes/
│   │   ├── health.py               # Health checks
│   │   ├── external_api.py         # External APIs
│   │   ├── data_processing.py      # PySpark endpoints
│   │   └── ml_predictions.py       # PyTorch endpoints
│   │
│   ├── services/
│   │   ├── external_api_service.py
│   │   ├── data_service.py         # PySpark integration
│   │   └── ml_service.py           # PyTorch integration
│   │
│   ├── database/                   # MongoDB integration
│   │   ├── mongodb.py              # Motor async client
│   │   ├── models.py               # Pydantic models
│   │   └── repositories/
│   │       ├── data_repository.py
│   │       └── prediction_repository.py
│   │
│   ├── helpers/
│   │   ├── logger.py
│   │   ├── http_client.py
│   │   └── file_handler.py         # File upload/download
│   │
│   └── middleware/
│       └── error_handler.py
│
├── tests/
├── pyproject.toml
└── uv.lock
```

---

## 🔌 API Endpoints

### Health & External APIs (Existing)

```
GET  /health                        # Health check
GET  /api/v1/external/posts         # Get posts
POST /api/v1/external/weather       # Get weather
```

### Data Processing (New)

```
POST /api/v1/data/upload            # Upload CSV/JSON
POST /api/v1/data/process           # Run PySpark pipeline
GET  /api/v1/data/stats             # Get statistics
GET  /api/v1/data/download/:id      # Download processed data
```

### ML Predictions (New)

```
POST /api/v1/ml/predict             # Single prediction
POST /api/v1/ml/batch-predict       # Batch predictions
GET  /api/v1/ml/model-info          # Model metadata
```

---

## 🎨 UI Design System

### Color Palette

```css
/* Primary Colors */
--primary-50: #eff6ff;
--primary-500: #3b82f6;
--primary-600: #2563eb;
--primary-700: #1d4ed8;

/* Accent Colors */
--accent-500: #8b5cf6;
--accent-600: #7c3aed;

/* Neutral Colors */
--gray-50: #f9fafb;
--gray-100: #f3f4f6;
--gray-800: #1f2937;
--gray-900: #111827;

/* Success/Error */
--success: #10b981;
--error: #ef4444;
```

### Typography

```css
/* Google Fonts - Inter */
font-family: 'Inter', sans-serif;

/* Headings */
h1: 2.5rem, font-weight: 700
h2: 2rem, font-weight: 600
h3: 1.5rem, font-weight: 600

/* Body */
body: 1rem, font-weight: 400
```

### Components

```
┌─────────────────────────────────────────────────────────────┐
│  Header                                                      │
│  • Logo, Navigation, User Menu                              │
└─────────────────────────────────────────────────────────────┘

┌──────────┬──────────────────────────────────────────────────┐
│          │  Main Content Area                               │
│ Sidebar  │  • Cards with glassmorphism                      │
│          │  • Smooth animations                             │
│ • Home   │  • Interactive charts (Recharts)                 │
│ • Data   │  • Responsive tables                             │
│ • ML     │  • Loading states                                │
│          │                                                  │
└──────────┴──────────────────────────────────────────────────┘
```

---

## 💾 Data Storage

### File Structure

```
data/
├── uploads/                    # User uploaded files
│   ├── raw/
│   │   └── user_data_123.csv
│   └── processed/
│       └── user_data_123_processed.parquet
│
├── ml_data/                    # ML training data
│   ├── train.parquet
│   └── test.parquet
│
└── models/                     # Saved models
    └── sentiment_model.pt
```

---

## 🔄 Component Interaction

### Example: Sentiment Analysis Flow

```python
# 1. Frontend (React)
const analyzeSentiment = async (text) => {
  const response = await apiClient.post('/api/v1/ml/predict', {
    text: text
  });
  return response.data;
};

# 2. Backend (FastAPI)
@router.post("/predict")
async def predict_sentiment(request: PredictionRequest):
    result = ml_service.predict(request.text)
    return {"sentiment": result.sentiment, "confidence": result.confidence}

# 3. ML Service (PyTorch)
class MLService:
    def predict(self, text: str):
        model.eval()
        with torch.no_grad():
            prediction = model(preprocess(text))
        return prediction
```

---

## 🚀 Deployment Architecture

### Development

```
localhost:5173  →  React Dev Server
localhost:8000  →  FastAPI (uvicorn)
```

### Production (Future)

```
┌─────────────────────────────────────────────────────────────┐
│                    Nginx (Reverse Proxy)                     │
└────────────────────────┬────────────────────────────────────┘
                         │
        ┌────────────────┴────────────────┐
        ▼                                 ▼
┌──────────────┐                  ┌──────────────┐
│  Static      │                  │   FastAPI    │
│  Files       │                  │   (Gunicorn) │
│  (React)     │                  │              │
└──────────────┘                  └──────────────┘
```

---

## 🔐 Security Considerations

### CORS Configuration

```python
# FastAPI CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # React dev server
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

### File Upload Validation

```python
# Validate file type and size
ALLOWED_EXTENSIONS = {'.csv', '.json'}
MAX_FILE_SIZE = 10 * 1024 * 1024  # 10MB
```

---

## 📊 Technology Stack Summary

| Layer        | Technology   | Purpose            |
| ------------ | ------------ | ------------------ |
| **Frontend** | React 18     | UI framework       |
|              | Vite         | Build tool         |
|              | TailwindCSS  | Styling            |
|              | Recharts     | Data visualization |
|              | Axios        | HTTP client        |
| **Backend**  | FastAPI      | REST API           |
|              | Uvicorn      | ASGI server        |
|              | Pydantic     | Data validation    |
| **Data**     | PySpark      | Data processing    |
|              | Parquet      | Data storage       |
| **ML**       | PyTorch      | Deep learning      |
|              | Transformers | Pre-trained models |

---

## 🎯 Key Features

✅ **Modern UI**: React with TailwindCSS  
✅ **Fast API**: Async FastAPI backend  
✅ **Big Data**: PySpark processing  
✅ **ML Integration**: PyTorch models  
✅ **No API Keys**: All open-source  
✅ **Type Safety**: TypeScript + Pydantic  
✅ **Responsive**: Mobile-friendly design  
✅ **Real-time**: Live updates and feedback

---

## 📝 Development Workflow

```bash
# 1. Start MongoDB
cd database
docker-compose up -d

# 2. Start Backend
cd fastapi-starter/backend
uv run uvicorn app.main:app --reload

# 3. Start Frontend
cd fastapi-starter/frontend
npm run dev

# 4. Access Application
# Frontend: http://localhost:5173
# Backend API: http://localhost:8000
# API Docs: http://localhost:8000/docs
# MongoDB: mongodb://localhost:27017
```

---

_Updated: Feb 2026_
