import { EventEmitter, Injectable } from '@angular/core';
import {ITaskList, ITask} from '../models/models';
import {HttpClient, HttpParams} from '@angular/common/http';
import {MainService} from './main.service';
import { environment } from 'src/environments/environment';
@Injectable({
  providedIn: 'root'
})
export class ProviderService extends MainService {
  constructor(http: HttpClient) {
    super(http);
  }


  getUrl() {
    return environment.url
  }
  getTaskLists(): Promise<ITaskList[]> {
    return this.get(this.getUrl()+'/task_lists/',  {});
  }
  getTasks(id: number) {
    return this.get(this.getUrl()+`/task_lists/${id}/tasks/`, {});
  }

}