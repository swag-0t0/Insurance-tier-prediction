from typing import Dict, Annotated
from pydantic import BaseModel, Field

class PredictionResponse(BaseModel):
    predicted_category: Annotated[str, Field(description="The predicted insurance premium category", example="High")]# type: ignore[reportCallIssue]
    confidence: Annotated[float, Field(description="Model's confidence score for the predicted class (range: 0 to 1)", example=0.8432)]# type: ignore[reportCallIssue]
    class_probabilities: Annotated[Dict[str, float], Field(description="Probability distribution across all possible classes", example={"Low": 0.01, "Medium": 0.15, "High": 0.84})]        # type: ignore[reportCallIssue]