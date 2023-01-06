import { Component, OnInit } from '@angular/core';
import { ListeAlbumsService } from '../liste-albums.service';
import {ActivatedRoute, Router} from '@angular/router';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-panier',
  templateUrl: './panier.component.html',
  styleUrls: ['./panier.component.css']
})
export class PanierComponent implements OnInit {

  liste:ListeAlbumsService 
  finalPanier;

  constructor(liste: ListeAlbumsService,private http: HttpClient, private router: Router, private route: ActivatedRoute) { 
    this.liste=liste;
    const storedList = localStorage.getItem('listeProd');
    if (storedList) {
      this.liste.listeProd = JSON.parse(storedList);
    }
    this.finalPanier=this.liste.listeProd
    console.log("panier",this.finalPanier)
  }
  ngOnInit(): void {

  }

}
