import config from './config.json';
import type { UserDetailsSchema, UserLoginSchema } from '../schemas/user';

export default class UserAPI {
    public static checkAuthentication(
        successCallback: (value: any) => any,
        failCallback: (reason: any) => any
    ): void {
        fetch(`${config.apiURL}/user/check_authentication`)
        .then(response => response.json())
        .then(data => successCallback(data))
        .catch(error => failCallback(error));
    }

    public static login(
        userLogin: UserLoginSchema,
        successCallback: (value: any) => any,
        failCallback: (reason: any) => any
    ): void {
        fetch(`${config.apiURL}/user/login`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(userLogin)
        })
        .then(response => response.json())
        .then(data => successCallback(data))
        .catch(error => failCallback(error));
    }

    public static register(
        userDetails: UserDetailsSchema,
        successCallback: (value: any) => any,
        failCallback: (reason: any) => any
    ): void {
        fetch(`${config.apiURL}/user/register`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(userDetails)
        })
        .then(response => response.json())
        .then(data => successCallback(data))
        .catch(error => failCallback(error));
    }
}
