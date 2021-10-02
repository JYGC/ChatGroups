from fastapi import Depends, HTTPException, Response, status
from fastapi_jwt_auth import AuthJWT
from fastapi_utils.cbv import cbv
from fastapi_utils.inferring_router import InferringRouter
import logging
from pony.orm import db_session
from typing import Union
from uuid import UUID

from app.core.error import error_log
from app.models.user import User
from app.models.address import Address
from app.schemas.user import UserDetailsSchema, UserLoginSchema


user_router = InferringRouter()


class AuthCookiesSetterView:
    def _set_auth_cookies(self, user_email, authorize: AuthJWT):
        access_token = authorize.create_access_token(
            subject=user_email
        )
        refresh_token = authorize.create_refresh_token(
            subject=user_email
        )
        authorize.set_access_cookies(access_token)
        authorize.set_refresh_cookies(refresh_token)


@cbv(user_router)
class RegisterCBV(AuthCookiesSetterView):
    @user_router.post("/v0/user/register", status_code=status.HTTP_201_CREATED)
    def post(
        self,
        user_details: UserDetailsSchema,
        authorize: AuthJWT = Depends()
    ):
        try:
            with db_session:
                lowercase_email = user_details.email.lower()
                if User.exists(email=lowercase_email):
                    raise HTTPException(
                        status_code=202,
                        detail="%s already exists" % (lowercase_email)
                    )
                action = "register new user"
                new_user = User.from_schema(user_details)
                new_user.address = Address.from_schema(user_details.address)
                new_user.address.user = new_user
                # Make histories
                new_user_history = new_user.create_history(action)
                new_user_history.address = new_user.address.create_history(
                    action
                )
                new_user_history.address.user = new_user_history
                new_user.flush()
                # Set auth cookies
                self._set_auth_cookies(new_user.email, authorize)
                return { "success": "user created" }
        except HTTPException as http_exc:
            raise http_exc
        except Exception as e:
            error_log.exception(e, exc_info=True)
            raise HTTPException(
                status_code=404,
                detail="Unknown request"
            )


@cbv(user_router)
class LoginCBV(AuthCookiesSetterView):
    @user_router.post("/v0/user/login", status_code=status.HTTP_200_OK)
    def post(
        self,
        user_login: UserLoginSchema,
        authorize: AuthJWT = Depends()
    ):
        try:
            with db_session:
                users = User.select(lambda u: u.email == user_login.email
                                    and u.password == user_login.password
                                    and u.deleted == False)[:]
                if len(users) == 0:
                    raise HTTPException(
                        status_code=401,
                        detail="Unknown credentials"
                    )
                user = users[0]
                if user.banned:
                    raise HTTPException(
                        status_code=401,
                        detail=("Account was banned. Contact system "
                                "administrator")
                    )
                # Set auth cookies
                self._set_auth_cookies(user.email, authorize)
                return { "success": "logged in" }
        except HTTPException as http_exc:
            raise http_exc
        except Exception as e:
            error_log.exception(e, exc_info=True)
            raise HTTPException(
                status_code=404,
                detail="Unknown request"
            )


@cbv(user_router)
class RefreshCBV:
    @user_router.post("/v0/user/refresh")
    def post(self, authorize: AuthJWT = Depends()):
        authorize.jwt_refresh_token_required()
        current_user_email = authorize.get_jwt_subject()
        new_access_token = Authorize.create_access_token(
            subject=current_user_email
        )
        authorize.set_access_cookies(new_access_token)
        return {"msg":"The token has been refresh"}
    

@cbv(user_router)
class CheckAuthenticationCBV:
    @user_router.get("/v0/user/check_authentication")
    def get(self, authorize: AuthJWT = Depends()):
        authorize.jwt_required()
        current_user_email = authorize.get_jwt_subject()
        return {"success": "Logged in user"}


@cbv(user_router)
class LogoutCBV:
    @user_router.delete("/v0/user/logout")
    def delete(self, authorize: AuthJWT = Depends()):
        authorize.jwt_required()
        authorize.unset_jwt_cookies()
        return {"msg": "Successfully logout"}
