import { Component, OnInit } from '@angular/core';
import { ListeAlbumsService } from '../liste-albums.service';
import { HttpClient } from '@angular/common/http';
import {Router} from '@angular/router';
import { HttpParams } from '@angular/common/http';


@Component({
  selector: 'app-admin',
  templateUrl: './admin.component.html',
  styleUrls: ['./admin.component.css']
})
export class AdminComponent implements OnInit {
  listeCommande : ListeAlbumsService
  commandes:any
  idCommande:any
  etatCommande:any
  newArtiste:any
  nomArt:any
  option:any
  prixAlbum: any
  quantite:any 
  anneeAlbum: any
  typeAlbum:any
  nomAlbum: any 
  imageAlbum: any
  idAlbumChanson: any
  nomChanson: any
  

  

  constructor(listeCommande:ListeAlbumsService) {
    this.listeCommande=listeCommande;
    

   }

  

  ngOnInit(): void {
  }


  afficheCommande(){
    console.log("test fonction affiche commande admin");
    this.listeCommande.afficheCommande().subscribe(
			(data : any) => {
        console.log("dans data commande admin",data);   

        this.commandes=data; 
       // console.log("id commande",data.Commandes[i][0]) 
       // this.idCommande=data[0]   
			});
			(error : any) => {
				console.log("une erreur c'est produite");
			}
  }

  modifEtat(){
    const params = new HttpParams()
    .set('idCommande', this.idCommande)
    .set('etat', this.etatCommande);
    console.log("test modif etat")

    this.listeCommande.modifCommande(params).subscribe(
        (data : any) => {
            console.log("test etat",this.etatCommande)
        //  window.location.reload();
        },
        (error : any) => {
        console.log("une erreur c'est produite");
        });
  }


  ajouterArtiste(){
    const params = new HttpParams()
    .set('a_ajouter', this.option)  // type d'ajout à faire
    .set('nomNouvelArtiste', this.newArtiste)
    .set('nomArtiste', this.nomArt)
    .set('prixAlbum', this.prixAlbum)
    .set('quantite', this.quantite)
    .set('anneeAlbum', this.anneeAlbum)
    .set('typeAlbum', this.typeAlbum)
    .set('nomAlbum', this.nomAlbum)
    .set('imgageAlbum', this.imageAlbum)
    .set('idAlbumChanson', this.idAlbumChanson)
    .set('nomChanson', this.nomAlbum)
    
    console.log("test ajout artiste admin")

    this.listeCommande.ajouterArtiste(params).subscribe(
        (data : any) => {
          console.log("data ajouter",data)
          console.log("artiste",this.newArtiste)
          console.log("choix",this.option)
          
        },
        (error : any) => {
        console.log("une erreur c'est produite");
        });
  }

  }


