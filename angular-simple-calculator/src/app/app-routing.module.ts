import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { OverviewComponent } from './overview/overview.component';
import { DesignComponent } from './design/design.component';
import { InputsComponent } from './inputs/inputs.component';
import { ParametersComponent } from './parameters/parameters.component';
import { CalculationsComponent } from './calculations/calculations.component';
import { SummaryComponent } from './summary/summary.component';

const routes: Routes = [
  { path: 'overview', component: OverviewComponent },
  { path: 'design', component: DesignComponent },
  { path: 'inputs', component: InputsComponent},
  { path: 'parameters', component: ParametersComponent},
  { path: 'calculations', component: CalculationsComponent},
  { path: 'summary', component: SummaryComponent}
];


@NgModule({
  imports: [ RouterModule.forRoot(routes) ],
  exports: [ RouterModule ]
})
export class AppRoutingModule {}
