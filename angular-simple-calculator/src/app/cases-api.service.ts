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
    return this.http.get<Cases[]>(`${API_URL}/cases`)
  }

  addCase(new_case: Cases): Observable<Cases> {
    return this.http.post<Cases>(`${API_URL}/create`, new_case, this.httpOptions)
  }
}
