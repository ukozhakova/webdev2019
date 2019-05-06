import { EventEmitter, Injectable } from '@angular/core';
import {ITaskList, ITask, IAuthResponse} from '../models/models';
import {HttpClient, HttpParams} from '@angular/common/http';
import {MainService} from './main.service';

@Injectable({
  providedIn: 'root'
})
export class ProviderService extends MainService {
  constructor(http: HttpClient) {
    super(http);
  }

  getTaskLists(): Promise<ITaskList[]> {
    return this.get('http://127.0.0.1:8000/task_lists/',  {});
  }

  getTasks(taskList: ITaskList) {
    return this.get(`http://localhost:8000/task_lists/${taskList.id}/tasks/`, {});
  }
  getTasksByName(id:number, name:string): Promise<ITask[]>{
    return this.get(`http://localhost:8000/task_lists/${id}/tasks/?name=${name}/`, {id, name});
  }
  getTasksByNameAndStatus(id:number, name:string, status:string): Promise<ITask[]>{
    return this.get(`http://localhost:8000/task_lists/${id}/tasks/?name=${name}&status=${status}/`, {id, name, status});
  }
  searchListByName(name:string): Promise<ITask[]>{
    return this.get(`http://localhost:8000/task_lists/?search=${name}/`, {name})
  }
  createTaskList(name: any): Promise<ITaskList>{
    return this.post('http://127.0.0.1:8000/task_lists/',{
      name: name,
    });
  }
  createTaskListWithTasks(name: any, tasks: ITask[]): Promise<ITaskList>{
    return this.post('http://127.0.0.1:8000/task_lists/',{
      name: name,
      tasks:tasks
    });
  }
  updateTaskList(taskList: ITaskList): Promise<ITaskList>{
    return this.put(`http://localhost:8000/task_lists/${taskList.id}/`, {
      name: taskList.name
    });
  }

  deleteTaskList(id: number): Promise<any>{
    return this.delet(`http://localhost:8000/task_lists/${id}/`, {});
  }

  updateTask(tl_id: number, t_name: any, t_status: any, task: ITask): Promise<ITask>{
    return this.put(`http://localhost:8000/task_lists/${task.task_list}/tasks/${task.id}/`, {
      name: t_name,
      status: t_status,
      task_list: task.task_list, 
    });
  }
  deleteTask(task: ITask): Promise<ITask>{
    return this.delet(`http://localhost:8000/task_lists/${task.task_list}/tasks/${task.id}/`, {
    });
  }
  createTask(name: any, status: any, id: number): Promise<ITask>{
    return this.post(`http://localhost:8000/task_lists/${id}/tasks/`, {
      name: name,
      status: status,
      task_list: id
    });
  }
  logIn(login: any, password: any): Promise<IAuthResponse> {
    return this.post('http://127.0.0.1:8000/login/', {
      username: login,
      password: password
    });
  }

  logout(): Promise<any> {
    return this.post('http://127.0.0.1:8000/logout/', {
    });
  }

}
