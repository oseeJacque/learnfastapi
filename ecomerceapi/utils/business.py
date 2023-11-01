from tortoise.signals import post_save
from typing import List,Optional,Type 
from tortoise import BaseDBAsyncClient
from models.models import User,Business,business_pydantic


@post_save(User)
async def create_business(
    sender: "Type[User]", 
    instance: User,
    created: bool, 
    using_db: "Optional[BaseDBAsyncClient]", 
    update_fields: List[str]
)->None : 
    if created:
        business_obj = await Business.create(
            business_name = instance.username, owner = instance
        )
        await business_pydantic.from_tortoise_orm(business_obj)
  