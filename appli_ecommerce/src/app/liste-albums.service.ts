import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ListeAlbumsService {

  constructor(private http :HttpClient) { }

  getEverything() : Observable<any>{
    console.log("test service");
	  return this.http.get('http://localhost:8000',{withCredentials : true});
  }

  getMusicsByArtist(nom_Artiste:string,nom_Album:string): Observable<any> {
    var url="http://localhost:8000/"+nom_Artiste+"/"+ nom_Album;
    console.log("test service details" ,nom_Artiste,nom_Album);
    const headers = new HttpHeaders()
	    .set('Content-Type', 'application/json');
	  return this.http.get(url,{});


  }

  
}
