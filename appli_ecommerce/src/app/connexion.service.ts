import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ConnexionService {

  constructor(private http :HttpClient) { }


  login(email:string,password:string) : Observable<any>{
    console.log("test service connexion");
    const headers = new HttpHeaders()
	  return this.http.post<any>('http://localhost:8000/connexion',{email:email,password:password});
  }

  
}
