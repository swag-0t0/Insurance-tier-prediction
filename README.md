# Insurance Premium Prediction API

A FastAPI-based web service that predicts insurance premium categories using machine learning. The API analyzes user health metrics, lifestyle factors, and demographic information to classify insurance premiums into categories (Low, Medium, High).

## Features

- **User Input Validation**: Comprehensive input validation using Pydantic schemas
- **Feature Engineering**: Automatic calculation of derived features:
  - BMI (Body Mass Index) calculation
  - Lifestyle risk assessment (based on smoking status and BMI)
  - Age group classification (Young, Adult, Middle-aged, Senior)
  - City tier mapping (Tier 1, Tier 2, Tier 3 cities)
- **ML Predictions**: Pre-trained classification model with confidence scores
- **Probability Distribution**: Returns probability distribution across all premium categories
- **Error Handling**: Robust error handling with appropriate HTTP status codes
- **Health Check Endpoint**: Built-in health status monitoring

## Project Structure

```
InsurancePrediction/
├── main.py                          # FastAPI application and route definitions
├── reaquirements.txt                # Python dependencies
├── Config/
│   └── city_tier.py                 # City classification configuration
├── Model/
│   ├── prediction.py                # ML model loading and prediction logic
│   └── model.pkl                    # Pre-trained ML model (pickle format)
└── Schema/
    ├── user_input.py                # Input data schema with field validators
    └── prediction_response.py        # Response schema for predictions
```

## Installation

### Prerequisites
- Python 3.8+
- pip

### Setup

1. Clone or navigate to the project directory:
```bash
cd InsurancePrediction
```

2. Create and activate a virtual environment:
```bash
# Windows
python -m venv venv
.\venv\Scripts\Activate.ps1

# macOS/Linux
python -m venv venv
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r reaquirements.txt
```

## Running the Application

Start the FastAPI development server:
```bash
uvicorn main:app --reload
```

The API will be available at `http://localhost:8000`

### Interactive API Documentation
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## API Endpoints

### 1. Home Endpoint
```
GET /
```
Returns a welcome message.

**Response:**
```json
{
  "message": "Welcome to Home!"
}
```

### 2. Health Check
```
GET /health
```
Returns the API and model health status.

**Response:**
```json
{
  "status": "device okay",
  "version": "1.0.0"
}
```

### 3. Predict Insurance Premium
```
POST /predict
```
Predicts insurance premium category based on user input.

**Request Body:**
```json
{
  "age": 35,
  "weight": 75,
  "height": 1.75,
  "income_lpa": 25.5,
  "smoker": false,
  "city": "Mumbai",
  "occupation": "private_job"
}
```

**Response:**
```json
{
  "response": {
    "predicted_category": "High",
    "confidence": 0.8432,
    "class_probabilities": {
      "Low": 0.01,
      "Medium": 0.15,
      "High": 0.84
    }
  }
}
```

## Input Validation

### UserInput Schema
| Field | Type | Description | Constraints |
|-------|------|-------------|-------------|
| age | int | User's age | 0 < age < 120 |
| weight | float | User's weight in kg | > 0 |
| height | float | User's height in meters | 0 < height < 2.5 |
| income_lpa | float | Annual income in LPA | > 0 |
| smoker | bool | Smoking status | true/false |
| city | str | User's city | From tier lists |
| occupation | str | User's occupation | retired, freelancer, student, government_job, business_owner, unemployed, private_job |

### Automatic Feature Calculation
- **BMI**: weight / (height²)
- **Lifestyle Risk**: 
  - 'high' if smoker AND BMI > 30
  - 'medium' if smoker AND BMI > 27
  - 'Low' otherwise
- **Age Group**: 
  - 'young' if age < 25
  - 'adult' if 25 ≤ age < 45
  - 'middle_aged' if 45 ≤ age < 60
  - 'senior' if age ≥ 60
- **City Tier**:
  - Tier 1: Major metros (Mumbai, Delhi, Bangalore, etc.)
  - Tier 2: Secondary cities (Jaipur, Pune, Indore, etc.)
  - Tier 3: All other cities

## Technology Stack

- **Framework**: FastAPI
- **Data Validation**: Pydantic
- **Machine Learning**: scikit-learn
- **Data Processing**: pandas
- **Server**: Uvicorn

## Dependencies

See `reaquirements.txt` for the complete list of dependencies.

## Error Handling

The API returns appropriate HTTP status codes:
- **200 OK**: Successful prediction
- **500 Internal Server Error**: Model prediction failure

## Model Information

- **Version**: 1.0.0
- **Type**: Classification model
- **Output Classes**: Low, Medium, High
- **Features**: BMI, Age Group, Lifestyle Risk, City Tier, Occupation

## Future Enhancements

- Database integration for prediction history
- Model performance monitoring and logging
- Advanced feature engineering
- Model versioning and A/B testing
- API rate limiting and authentication
- Deployment to production (Docker, AWS, etc.)

## License

This project is for educational and interview purposes.

## Contact

For questions or suggestions, please contact the project owner.
