import { Component, OnInit, Input } from '@angular/core';
import { ListeAlbumsService } from '../liste-albums.service';
import {ActivatedRoute, Router} from '@angular/router';
import { HttpClient } from '@angular/common/http';
import { BodyComponent } from '../body/body.component';

@Component({
  selector: 'app-details',
  templateUrl: './details.component.html',
  styleUrls: ['./details.component.css'],
  providers:[BodyComponent]
})
export class DetailsComponent implements OnInit {

  listeDetails:any;
  liste:ListeAlbumsService;
  nomArtiste:any;
  nomAlbum:any;
  tesst:any;
  tesstt:any;
  //img:any;
  listeProod:any;
  image:any;
  prix:any;
  quantite:number=0;

  
  
  constructor(liste:ListeAlbumsService,private http: HttpClient, private router: Router, private route: ActivatedRoute) {
    this.liste=liste;
    const storedList = localStorage.getItem('listeProd');
    if (storedList) {
      this.liste.listeProd = JSON.parse(storedList);
    }


   }

  ngOnInit(): void {
 
   // this.afficheDetails(this.nomArtiste,this.nomAlbum)
   const test =this.route.snapshot.paramMap.get('test');
   console.log("test video",test);
   const testt =this.route.snapshot.paramMap.get('testt');
   console.log("test video 2",testt);
   this.tesst=test; // artiste
   this.tesstt=testt; // album
   //const imga =this.route.snapshot.paramMap.get('imga');
   //this.img=imga;
   

   this.nomArtiste=this.tesst;
   this.nomAlbum=this.tesstt;

  

  this.liste.getMusicsByArtist(this.nomArtiste,this.nomAlbum).subscribe(
   (data:any)=>{  
      
      this.listeDetails=data;  
      console.log("nom artiste"+this.nomArtiste);
      console.log("test details",data);
      console.log("test affiche",this.listeDetails.Artiste)
      console.log("affiche prix",this.listeDetails.Prix)
      console.log("affiche image",this.listeDetails.Image)
      this.prix=this.listeDetails.Prix;
      this.image=this.listeDetails.Image;
      },
      error => {console.log(error);}
      );

} 
    addToCart(){
      if(this.quantite==0){
        this.quantite+=1;
        this.liste.addProduit(this.nomAlbum,this.nomArtiste,this.prix,this.image,this.quantite)
        console.log("ajouter",this.liste.listeProd);
        localStorage.setItem('listeProd', JSON.stringify(this.liste.listeProd));
        this.listeProod= localStorage.getItem('listeProd');
      }
      
      else{
        this.quantite+=1;
        this.liste.removeProduit(this.nomAlbum)
        console.log("j'ai supprimé")
        console.log("je suis la")
        this.liste.addProduit(this.nomAlbum,this.nomArtiste,this.prix,this.image,this.quantite)
        
      }
      console.log("quantite",this.quantite);


}

  } 


  

/*  afficheDetails(nomArtiste: string,nomAlbum:string):void{
    console.log("test fonction afficheDetails");
    this.liste.getMusicsByArtist(nomArtiste,nomAlbum).subscribe(
			(data : any) => {
        console.log("dans data:",data)
				//this.listeAlb=JSON.parse(JSON.stringify(data));
        this.listeDetails=data;
       
        
       // console.log("liste "+ this.liste)
			//	console.log("liste albums = "+ this.listeAlb);
			});
			(error : any) => {
				console.log("une erreur c'est produite");
			}
  } */


