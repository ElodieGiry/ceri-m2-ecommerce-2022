import { Component, OnInit } from '@angular/core';
import { ListeAlbumsService } from '../liste-albums.service';


@Component({
  selector: 'app-body',
  templateUrl: './body.component.html',
  styleUrls: ['./body.component.css']
})
export class BodyComponent implements OnInit {
  listeAlb:any;
  liste : ListeAlbumsService
 
  
  

  constructor(liste:ListeAlbumsService) {
    this.liste=liste;

   }

   ngOnInit(): void {
	  this.afficheListeAlbums();
  }
  
  afficheListeAlbums(){
    console.log("test fonction afficheListeAlb");
    this.liste.getEverything().subscribe(
			(data : any) => {
        console.log("dans data");
				//this.listeAlb=JSON.parse(JSON.stringify(data));
       this.listeAlb=data;
     
        console.log("test"+this.listeAlb.Item);
        console.log("test2 : "+this.listeAlb.Item[0])
        
       // console.log("liste "+ this.liste)
			//	console.log("liste albums = "+ this.listeAlb);
			});
			(error : any) => {
				console.log("une erreur c'est produite");
			}
  }
}

