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

    public static refreshToken(
        successCallback: (value: any) => any,
        failCallback: (reason: any) => any
    ) {
        fetch(`${config.apiURL}/user/refresh`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRF-Token': this.getCookie('csrf_refresh_token'),
            }
        })
        .then(response => response.json())
        .then(data => successCallback(data))
        .catch(error => failCallback(error));
    }

    public static logout(
        successCallback: (value: any) => any,
        failCallback: (reason: any) => any
    ) {
        fetch(`${config.apiURL}/user/logout`, {
            method: 'DELETE',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRF-Token': this.getCookie('csrf_access_token'),
            }
        })
        .then(response => response.json())
        .then(data => successCallback(data))
        .catch(error => failCallback(error));
    }

    private static getCookie(name: string): string {
        const nameLenPlus = (name.length + 1);
        return document.cookie
            .split(';')
            .map(c => c.trim())
            .filter(cookie => {
                return cookie.substring(0, nameLenPlus) === `${name}=`;
            })
            .map(cookie => {
                return decodeURIComponent(cookie.substring(nameLenPlus));
            })[0] || null;
    }
}
