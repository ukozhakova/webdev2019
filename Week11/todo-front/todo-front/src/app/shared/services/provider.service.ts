import { EventEmitter, Injectable } from '@angular/core';
import {ITaskList, ITask} from '../models/models';
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
  getTasks(id: number) {
    return this.get(`http://localhost:8000/task_lists/${id}/tasks/`, {});
  }

}