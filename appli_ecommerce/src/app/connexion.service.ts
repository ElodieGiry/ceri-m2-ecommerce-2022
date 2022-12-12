import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders, HttpParams } from '@angular/common/http';
import { Observable } from 'rxjs';



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

//   login(email:string,password:string): Observable<any> {
//     var url="http://localhost:8000/connexion"+"/"+email+"/"+ password;
//     console.log("test service details" ,email,password);
//     const headers = new HttpHeaders()
// 	    .set('Content-Type', 'application/json');
// 	  return this.http.get(url,{});
// }


}