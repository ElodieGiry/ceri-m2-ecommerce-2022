import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders,HttpParams } from '@angular/common/http';
import { Observable } from 'rxjs';


import { environment } from '../environments/environment';

@Injectable({
  providedIn: 'root'
})
export class ListeAlbumsService {
  //backend:string='http://localhost:8000'
  //backend=environment.BACKEND_URL
  listeProd: { albumName: string, artisteName: string,prix:string,image:string,quantite:number }[] = [];
 

  constructor(private http :HttpClient) { }

  getEverything() : Observable<any>{
    console.log("test service");
	  return this.http.get("http://localhost:8000/",{withCredentials : true});
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
  
  afficheCommande() : Observable<any>{   // affiche commande en cours mode admin
    console.log("test service commande");
	  return this.http.get("http://localhost:8000/admin",{withCredentials : true});

  
}

modifCommande(params: HttpParams){
  return this.http.get(`http://localhost:8000/admin`, { params });
}


ajouterArtiste(params:HttpParams){
  console.log("test service ajout artiste")
  return this.http.get('http://localhost:8000/ajouter',{params});
}
}
