import { Component, OnInit } from '@angular/core';
import {ConnexionService} from '../connexion.service';
import { HttpClient } from '@angular/common/http';

import {Router} from '@angular/router';

@Component({
  selector: 'app-inscription',
  templateUrl: './inscription.component.html',
  styleUrls: ['./inscription.component.css']
})
export class InscriptionComponent implements OnInit {

  inscrip:ConnexionService;
  connecte:any;

  constructor(inscription:ConnexionService,private http:HttpClient,private router:Router) {
    this.inscrip=inscription;
   }


  ngOnInit(): void {
  }




  inscription(formConnex:any){
    console.log("test inscription");
    console.log("test mail", formConnex.form.value.email);
    this.inscrip.inscription(formConnex.form.value.nom,formConnex.form.value.prenom,
      formConnex.form.value.email,formConnex.form.value.password,formConnex.form.value.telephone,
      formConnex.form.value.adresse,formConnex.form.value.code,formConnex.form.value.ville,formConnex.form.value.pays )
      
    console.log("inscription ok") 
    
    
  

  }

  inscriptionValide(){
    this.router.navigate(['/']);
    this.connecte=1
    localStorage.setItem("connecte",this.connecte);
    
  }
       
          
        
          
          
    
       

  
}