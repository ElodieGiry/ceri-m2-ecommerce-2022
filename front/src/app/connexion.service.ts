import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders, HttpParams } from '@angular/common/http';
import { Observable } from 'rxjs';
import { BehaviorSubject } from 'rxjs';



// const httpOptions : any    = {
//   headers: new HttpHeaders({
//     //'Content-Type':  'application/json',
//     'Access-Control-Allow-Headers': 'Content-Type',
//     'Access-Control-Allow-Methods': '*',
//     'Access-Control-Allow-Origin': '*'
//   })
// };
@Injectable({
  providedIn: 'root'
})
export class ConnexionService {

  constructor(private http :HttpClient) { }
  


  login(emaill:string,passwordd:string) : Observable<any>{
    console.log("test service connexion");
    let params=new HttpParams()
    .append('email',emaill)
    .append('password',passwordd)
    const headers = new HttpHeaders()
    .set('Content-Type','application/json')
    .set('Access-Control-Allow-Origin','*');
    console.log("tesssssst");
	  return this.http.post<any>('http://127.0.0.1:8000/connexion',{email: emaill, password: passwordd},{'headers':headers});
  }
 
  inscription(nomm:string, prenomm:string, emaill:string, passwordd:string, telephonee:string, adressee:string, codePostall:string, villee:string, payss:string) : Observable<any>{
    console.log("test service inscription");
    let params=new HttpParams()
    .append('nom',nomm)
    .append('prenom',prenomm)
    .append('email',emaill)
    .append('password',passwordd)
    .append('telephone',telephonee)
    .append('adresse',adressee)
    .append('codePostal',codePostall)
    .append('ville',villee)
    .append('pays',payss)
    const headers = new HttpHeaders()
    .set('Content-Type','application/json')
    .set('Access-Control-Allow-Origin','*');
    console.log("tesssssst");
	  return this.http.post<any>('http://127.0.0.1:8000/inscription',{nom:nomm,prenom:prenomm,email:emaill,password:passwordd,
    telephone:telephonee,adresse:adressee,codePostal:codePostall,ville:villee,pays:payss},{'headers':headers});
  }


}