import config from './config.json';
import type { MyChatSchema } from '../schemas/chat';

export default class ChatAPI {
    public static getAllMyChats(
        successCallback: (value: any) => any,
        failCallback: (reason: any) => any
    ): void {
        fetch(`${config.apiURL}/chat/get_all_my`)
        .then(response => response.json())
        .then(data => successCallback(data))
        .catch(error => failCallback(error));
    }

    public static createNewChat(
        myChat: MyChatSchema,
        successCallback: (value: any) => any,
        failCallback: (reason: any) => any
    ): void {
        fetch(`${config.apiURL}/chat/create_new`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(myChat)
        })
        .then(response => response.json())
        .then(data => successCallback(data))
        .catch(error => failCallback(error));
    }
}