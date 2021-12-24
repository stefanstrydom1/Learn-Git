import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppComponent } from './app.component';
import { AppRoutingModule } from './app-routing.module';
import { OverviewComponent } from './overview/overview.component';
import { DesignComponent } from './design/design.component';
import { InputsComponent } from './inputs/inputs.component';
import { ParametersComponent } from './parameters/parameters.component';
import { CalculationsComponent } from './calculations/calculations.component';
import { SummaryComponent } from './summary/summary.component';

@NgModule({
  declarations: [
    AppComponent,
    OverviewComponent,
    DesignComponent,
    InputsComponent,
    ParametersComponent,
    CalculationsComponent,
    SummaryComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
