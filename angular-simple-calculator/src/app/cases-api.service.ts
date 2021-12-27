import { Injectable } from '@angular/core';
import { API_URL } from './env';
import { HttpClient, HttpHeaders } from '@angular/common/http'
import { Observable } from 'rxjs';


export interface Cases {
  case_id?: Number;
  insured_name: String;
  created?: Date;
  inception_date?: Date;
  expiry_date?: Date;
} 

@Injectable()
export class CasesApiService {

  httpOptions = {
    headers: new HttpHeaders({ 'Content-Type': 'application/json' })
  };

  constructor(private http: HttpClient) { }

  getCases(): Observable<Cases[]> { 
    const url = `${API_URL}/cases`;
    return this.http.get<Cases[]>(url)
  }

  addCase(new_case: Cases): Observable<Cases> {
    const url = `${API_URL}/create`;
    return this.http.post<Cases>(url, new_case, this.httpOptions)
  }

  getCase(case_id: number): Observable<Cases> {
    const url = `${API_URL}/overview/${case_id}`;
    return this.http.get<Cases>(url)
  }

  updateCase(ex_case: Cases): Observable<any> {
    const url = `${API_URL}/edit`; /*${ex_case.case_id}*/
    console.log(url)
    return this.http.put<Cases>(url, ex_case, this.httpOptions)
  }
}
