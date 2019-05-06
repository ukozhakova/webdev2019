export interface ITaskList{
    id:number;
    name:string;
}

export interface ITask{
    id:number;
    name:string;
    status:string;
    created_at: Date;
    due_on: Date;
    task_list: number;
}

export interface IAuthResponse{
    token:string;
}