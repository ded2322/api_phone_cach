from fastapi import APIRouter, HTTPException
from fastapi_cache import FastAPICache
from fastapi_cache.decorator import cache

from core.schema_phone import PhoneSchema

router = APIRouter(
    prefix="",
    tags=["Phones"],
)


@router.get("/check_data")
@cache(expire=60)
async def get_address_by_phone(phone_number: int) -> dict[str, str]:
    """
    Получает адрес по номеру телефона. Использует кеширование для ускорения доступа.

    Args:
        phone_number (int): Номер телефона для поиска.

    Returns:
        Dict[str, str]: Словарь с ключом 'address' и значением - найденным адресом.

    Raises:
        HTTPException: Если номер телефона не найден.
    """

    cache_key = f"{phone_number}"
    cached_address = await FastAPICache.get_backend().get(cache_key)

    if cached_address:
        return {"address": cached_address.decode("utf-8")}
    else:
        raise HTTPException(status_code=404, detail="Data not found")


@router.post("/write_data")
@cache(expire=60)
async def write_phone_data(user_data: PhoneSchema) -> dict[str, str]:
    """
    Записывает или обновляет данные телефона и адреса в кеше.

    Args:
        user_data (PhoneSchema): Данные пользователя, содержащие номер телефона и адрес.

    Returns:
        dict: Словарь с информацией о совершенном действии и сообщением.
    """
    cache_key = str(user_data.phone_number)
    cache_value = user_data.address

    # Получаем backend для работы с Redis
    backend = FastAPICache.get_backend()

    # Проверяем, существует ли уже такой ключ
    existing_address = await backend.get(cache_key)

    # Записываем или обновляем данные в Redis
    await backend.set(cache_key, cache_value, expire=60)

    if existing_address:
        return {
            "action": "update",
            "message": f"Address updated: '{cache_value}', for phone_number: {cache_key}",
        }
    else:
        return {
            "action": "write",
            "message": f"New phone_number saved with addres: {cache_value}",
        }
