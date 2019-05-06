import { Component, OnInit, OnDestroy } from '@angular/core';
import { ProviderService } from '../shared/services/provider.service';
import {ITaskList, ITask} from '../shared/models/models';
import { loadInternal } from '@angular/core/src/render3/util';
import { checkAndUpdateBinding } from '@angular/core/src/view/util';

@Component({
  selector: 'app-parent',
  templateUrl: './parent.component.html',
  styleUrls: ['./parent.component.css']
})
export class ParentComponent implements OnInit {
  public taskLists: ITaskList[]=[];
  public tasks: ITask[]=[];
  public taskList_current: ITaskList;
  public task_current: ITask;

  public name: any='';
  public search_name='';
  public search_list='';
  public task_status: any='';
  public task_listid: any='';
  public task_name: any='';
  public logged= false;
  public login: any = '';
  public password: any = '';
  public created_tasks: ITask[]=[];
  public created_task_name: any='';
  public created_task_status: any='';
  constructor(private provider: ProviderService) { }

  ngOnInit() {
    const token = localStorage.getItem('token');
    if(token){
      this.logged= true;
    }
    if(this.logged){
      this.provider.getTaskLists().then(res=>{
        this.taskLists= res;
      });
    }
  }

  getTasks(taskList: ITaskList){
    this.provider.getTasks(taskList).then(res=>{
      this.tasks= res;
    });
    this.taskList_current= taskList;

  }
  searchList(){
    this.provider.searchListByName(this.search_list).then(res=>{
      this.taskLists=res;
    });
  }
  filter1(){
    this.provider.getTasksByName(this.taskList_current.id, this.search_name).then(r=>{
      this.tasks=r;
      console.log(this.taskList_current.id);
    });
  }
  order(){
    this.provider.orderByName(this.taskList_current.id, this.search_name).then(r=>{
      this.tasks=r;
      console.log(this.taskList_current.id);
    });
  }
  updateTaskList(taskList: ITaskList){
    this.provider.updateTaskList(taskList).then(res=>{
      console.log(taskList.name+ ' updated');
    });
  }
  deleteTaskList(taskList: ITaskList){
    this.provider.deleteTaskList(taskList.id).then(res=>{
      console.log(taskList.name+ ' deleted')
      this.provider.getTaskLists().then(r=>{
        this.taskLists = r;
      });
    });
  }

  createTaskList(){
    if(this.name!==''){
      this.provider.createTaskListWithTasks(this.name, this.created_tasks).then(res=>{
      this.name = '';
      this.taskLists.push(res);
      console.log(res.id);
      this.task_current.task_list=res.id;
      console.log(this.task_current.task_list);
      this.task_current.name= this.created_task_name;
      this.task_current.status= this.created_task_status;
      this.created_tasks.push(this.task_current);
      this.tasks.push(this.task_current);
      console.log(this.created_tasks.length);
      });
      console.log('rgr');
  }
  }
  createTask(){
    if(this.task_name!==''){
      this.provider.createTask(this.task_name, this.task_status, this.task_listid).then(res=>{
        //this.task_name = '';
       // this.task_status='';
        this.tasks.push(res);
        console.log(this.task_name+ ' created');
      });
    }
  }
  updateTask(task: ITask){
    this.provider.updateTask(task.task_list, task.name, task.status, task).then(res=>{
      console.log(task.task_list+ ' updated');
    });
  }
  deleteTask(task: ITask){
    this.provider.deleteTask(task).then(res=>{
      console.log(task.name+ ' deleted')
      });
    }
    
    logIn() {
      if (this.login !== '' && this.password !== '') {
        this.provider.logIn(this.login, this.password).then(res => {
          localStorage.setItem('token', res.token);
  
          this.logged = true;
  
          this.provider.getTaskLists().then(r => {
            this.taskLists = r;
          });
  
        });
      }
    }
  
    logout() {
      this.provider.logout().then(res => {
        localStorage.clear();
        this.logged = false;
      });
    }
  }
