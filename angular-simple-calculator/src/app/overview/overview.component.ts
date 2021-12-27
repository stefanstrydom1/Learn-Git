import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { Location } from '@angular/common';
import { CasesApiService, Cases } from '../cases-api.service';

@Component({
  selector: 'app-overview',
  templateUrl: './overview.component.html',
  styleUrls: ['./overview.component.css']
})
export class OverviewComponent implements OnInit {

  ex_case: Cases | undefined;

  constructor(
    private route: ActivatedRoute,
    private caseApiService: CasesApiService,
    private location: Location
    ) { }

  ngOnInit(): void {
    this.getCase()
  }

  getCase(): void {
    const case_id = Number(this.route.snapshot.paramMap.get('case_id'));
    this.caseApiService.getCase(case_id)
    .subscribe(ex_case => this.ex_case = ex_case);

  }

  save(): void {
    console.log(this.ex_case)
    if (this.ex_case) {
      this.caseApiService.updateCase(this.ex_case)
      .subscribe(() => this.goBack());

    }
  }

  deleteCase(delete_case: Cases): void {
    this.caseApiService.deleteCase(delete_case)
    .subscribe(() => this.goBack());
  }

  goBack(): void {
    this.location.back();
  }
}
