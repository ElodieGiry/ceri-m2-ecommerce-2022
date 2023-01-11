import { Component, OnInit } from '@angular/core';
import { ListeAlbumsService } from '../liste-albums.service';
import {ConnexionService} from '../connexion.service';


@Component({
  selector: 'app-body',
  templateUrl: './body.component.html',
  styleUrls: ['./body.component.css']
})
export class BodyComponent implements OnInit {
  listeAlb:any;
  liste : ListeAlbumsService
  connect:ConnexionService;
  value=(localStorage.getItem("connecte"));
 
  
  

  constructor(liste:ListeAlbumsService,connect:ConnexionService) {
    this.liste=liste;
    this.connect=connect;

   }

   ngOnInit(): void {
	  this.afficheListeAlbums();

    if(this.value=="1"){
      this.connect.setIsConnected(true)
    }
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

