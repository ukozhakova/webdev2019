import { Component, OnInit } from '@angular/core';
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
  public numbers: number[]=[1,2,3,4];
  constructor(private provider: ProviderService) { }

  ngOnInit() {
    
    this.provider.getTaskLists().then(res => {
      this.taskLists =res;
  });

}

  getTasks(taskList: ITaskList){
    this.provider.getTasks(taskList.id).then(res=>{
      this.tasks= res;
    });
  }
}
