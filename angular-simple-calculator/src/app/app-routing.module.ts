import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { OverviewComponent } from './overview/overview.component';
import { DesignComponent } from './design/design.component';
import { InputsComponent } from './inputs/inputs.component';
import { ParametersComponent } from './parameters/parameters.component';
import { CalculationsComponent } from './calculations/calculations.component';
import { SummaryComponent } from './summary/summary.component';
import { CasesComponent } from './cases/cases.component';

const routes: Routes = [
  { path: '', redirectTo: '/cases', pathMatch: 'full'},
  { path: 'overview/:case_id', component: OverviewComponent },
  { path: 'design/:case_id', component: DesignComponent },
  { path: 'inputs/:case_id', component: InputsComponent},
  { path: 'parameters/:case_id', component: ParametersComponent},
  { path: 'calculations/:case_id', component: CalculationsComponent},
  { path: 'summary/:case_id', component: SummaryComponent},
  { path: 'cases', component: CasesComponent}
];


@NgModule({
  imports: [ RouterModule.forRoot(routes) ],
  exports: [ RouterModule ]
})
export class AppRoutingModule {}
