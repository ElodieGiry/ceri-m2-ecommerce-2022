import { Component, OnInit } from '@angular/core';
import { ListeAlbumsService } from '../liste-albums.service';
import { ActivatedRoute, Router } from '@angular/router';
import { HttpClient } from '@angular/common/http';
import { NgFor } from '@angular/common';


@Component({
  selector: 'app-panier',
  templateUrl: './panier.component.html',
  styleUrls: ['./panier.component.css'],
})
export class PanierComponent implements OnInit {

  liste: ListeAlbumsService
  finalPanier;

  constructor(liste: ListeAlbumsService, private http: HttpClient, private router: Router, private route: ActivatedRoute) {
    this.liste = liste;
    const storedList = localStorage.getItem('listeProd');
    if (storedList) {
      this.liste.listeProd = JSON.parse(storedList);
    }
    this.finalPanier = this.liste.listeProd
    console.log("panier", this.finalPanier)
  }
  ngOnInit(): void {

  }
  deleteItem(item: any, event: Event) {
    event.preventDefault();
    // Supprime l'item de la liste finalPanier
    this.finalPanier = this.finalPanier.filter(i => i !== item);
    // Supprime l'item du local storage en utilisant l'ID de l'item
    localStorage.removeItem(item.id);
    // Met à jour la liste de panier dans le local storage
    localStorage.setItem('listeProd', JSON.stringify(this.finalPanier));
  }
  getPrix(item: any): number {
    return parseInt(item.prix, 10) + 5;
  }
  calculerPrixTotal(panier: any[]): number {
    let total = 0;
    panier.forEach(item => {
      total += parseInt(item.prix, 10);
    });
    return total;
  }
  calculerPrixLivraison(prixTotal: any): number {
    let prixlivraison = prixTotal * 0.2;
    let prixarrondie = parseInt(prixlivraison.toFixed(2));
    return prixarrondie;
  }
  calculerPrixLivraison2(prixTotal: any): number {
    let prixlivraison = prixTotal * 0.26;
    let prixarrondie = parseInt(prixlivraison.toFixed(2));
    return prixarrondie;
  }
  calculerPrixLivraison3(prixTotal: any): number {
    let prixlivraison = prixTotal * 0.32;
    let prixarrondie = parseInt(prixlivraison.toFixed(2));
    return prixarrondie;
  }
  calculerPrixLivraison4(prixTotal: any): number {
    let prixlivraison = prixTotal * 0.38;
    let prixarrondie = parseInt(prixlivraison.toFixed(2));
    return prixarrondie;
  }

  calculerPrixTotalCommande(panier: any[]): number {
    return this.calculerPrixTotal(panier) + this.calculerPrixLivraison(this.calculerPrixTotal(panier));
  }




}