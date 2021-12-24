import { Component, OnInit } from '@angular/core';
import { CasesApiService, Cases } from '../cases-api.service';
import { Subscription } from 'rxjs';


@Component({
  selector: 'app-cases',
  templateUrl: './cases.component.html',
  styleUrls: ['./cases.component.css']
})

export class CasesComponent implements OnInit {
  
  cases_list: Cases[] = [];

  constructor(private CasesApiService: CasesApiService) { }

  ngOnInit(): void {
    this.getCases();
  }

  getCases() {
    this.CasesApiService.getCases()
    .subscribe(cases_list => this.cases_list = cases_list)
  } 

}
