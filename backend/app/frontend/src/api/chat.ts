import config from './config.json';

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
}