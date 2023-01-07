import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ListeAlbumsService {
  BACKEND_URL:string='http://localhost:8000'

  listeProd: { albumName: string, artisteName: string,prix:string,image:string,quantite:number }[] = [];
 

  constructor(private http :HttpClient) { }

  getEverything() : Observable<any>{
    console.log("test service");
	  return this.http.get(this.BACKEND_URL,{withCredentials : true});
  }

  getMusicsByArtist(nom_Artiste:string,nom_Album:string): Observable<any> {
    var url="http://localhost:8000/"+nom_Artiste+"/"+ nom_Album;
    console.log("test service details" ,nom_Artiste,nom_Album);
    const headers = new HttpHeaders()
	    .set('Content-Type', 'application/json');
	  return this.http.get(url,{});


  }

  addProduit(albumN: string,nomArt:string,price:string,img:string,q:number) {
    this.listeProd.push({ albumName: albumN, artisteName:nomArt ,prix:price,image:img,quantite:q });
  }


  removeProduit(albumN: string) {
    let index = this.listeProd.findIndex(p => p.albumName === albumN);
    console.log("index",index)
    if (index !== -1) {
      this.listeProd.splice(index, 1);
    }
  }
  
  

  
}
