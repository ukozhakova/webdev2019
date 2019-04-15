import { Component, OnInit, Input } from '@angular/core';
import { ProviderService } from '../shared/services/provider.service';
import {ITaskList, ITask} from '../shared/models/models';

@Component({
  selector: 'app-parent',
  templateUrl: './parent.component.html',
  styleUrls: ['./parent.component.css']
})
export class ParentComponent implements OnInit {
  public taskLists: ITaskList[]=[];
  public tasks: ITask[]=[];
  public name: any='';
  public task_status: any='';
  public task_listid: any='';
  public task_name: any='';
  constructor(private provider: ProviderService) { }

  ngOnInit() {
    
    this.provider.getTaskLists().then(res => {
      this.taskLists =res;
  });

}

  getTasks(taskList: ITaskList){
    this.provider.getTasks(taskList).then(res=>{
      this.tasks= res;
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
      this.provider.createTaskList(this.name).then(res=>{
        this.name = '';
        this.taskLists.push(res);
      });
    }
  }
  createTask(){
    if(this.task_name!==''){
      this.provider.createTask(this.task_listid,this.task_name,this.task_status).then(res=>{
        //this.task_name = '';
        this.tasks.push(res);
        console.log(this.task_name+ ' created')
      });
    }
  }
  updateTask(task: ITask){
    this.provider.updateTask(task.task_list, task.name, task.status, task).then(res=>{
      console.log(task.name+ ' updated');
    });
  }
  deleteTask(task: ITask){
    this.provider.deleteTask(task).then(res=>{
      console.log(task.name+ ' deleted')
     
      });
    }
  }
