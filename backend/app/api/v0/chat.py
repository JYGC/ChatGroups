from fastapi import Depends, HTTPException, Response, status
from fastapi_jwt_auth import AuthJWT
from fastapi_utils.cbv import cbv
from fastapi_utils.inferring_router import InferringRouter
from pony.orm import db_session
from uuid import UUID, uuid4

from app.core.error import unknown_error_response
from app.models.chat import Chat, ChatUser
from app.schemas.chat import ChatSchema, MyChatSchema


chat_router = InferringRouter()


@cbv(chat_router)
class GetAllMyChatCBV:
    @chat_router.get("/v0/chat/get_all_my", status_code=status.HTTP_200_OK)
    def get(
        self,
        authorize: AuthJWT = Depends()
    ) -> dict[str, list[ChatSchema]]:
        authorize.jwt_required()
        try:
            return { "success": [
                MyChatSchema(id=uuid4(), name="name1", description="desc1", number_of_participants=3),
                MyChatSchema(id=uuid4(), name="name2", number_of_participants=6),
                MyChatSchema(id=uuid4(), name="name3", description="desc3", number_of_participants=10)
            ]}
        except HTTPException as http_exc:
            raise http_exc
        except Exception as exc:
            unknown_error_response(HTTPException, exc)


@cbv(chat_router)
class CreateNew:
    @chat_router.post(
        "/v0/chat/create_new",
        status_code=status.HTTP_201_CREATED
    )
    def post(
        self,
        new_chat: MyChatSchema,
        authorize: AuthJWT = Depends()
    ):
        authorize.jwt_required()
        try:
            print(new_chat.name)
            print(new_chat.description)
            print(new_chat.number_of_participants)
            print(new_chat.visible_to_all)
        except HTTPException as http_exc:
            raise http_exc
        except Exception as exc:
            unknown_error_response(HTTPException, exc)
