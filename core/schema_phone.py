import re

from pydantic import BaseModel, Field, validator


class PhoneSchema(BaseModel):
    phone_number: int = Field(..., gt=0, description="Phone number (positive integer)")
    address: str = Field(..., min_length=1, description="Address")

    @validator("phone_number")
    def validate_phone_number(cls, value):
        # Преобразуем число в строку для проверки длины
        phone_str = str(value)
        if (
            len(phone_str) < 2 or len(phone_str) > 15
        ):  # 15 - максимальная длина международного номера
            raise ValueError("Phone number must be between 3 and 15 digits long")
        # Дополнительная проверка: убедимся, что номер состоит только из цифр
        if not re.match(r"^\d+$", phone_str):
            raise ValueError("Phone number must contain only digits")
        return value
