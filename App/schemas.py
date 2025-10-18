from pydantic import BaseModel

class UserData(BaseModel):
    gender: str
    age: int
    country: str
    subscription_type: str
    listening_time: int
    songs_played_per_day: int
    skip_rate: float
    device_type: str
    ads_listened_per_week: int
    offline_listening: int

class PredictionResponse(BaseModel):
    is_churned_predicted: int
    churn_probability: float
