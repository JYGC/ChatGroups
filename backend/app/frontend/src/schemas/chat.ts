export interface ChatSchema {
    name: string;
    description: string;
    number_of_participants: number;
}

export interface MyChatSchema extends ChatSchema {
    visible_to_all: boolean;
}

export interface JoinedChatSchema extends ChatSchema {
    user_is_admin: boolean;
}
