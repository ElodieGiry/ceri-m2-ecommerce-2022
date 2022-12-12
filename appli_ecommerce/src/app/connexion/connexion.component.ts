import { HttpClient } from '@angular/common/http';
import { Component, OnInit } from '@angular/core';
import {ConnexionService} from '../connexion.service';
import {Router} from '@angular/router';

@Component({
  selector: 'app-connexion',
  templateUrl: './connexion.component.html',
  styleUrls: ['./connexion.component.css']
})
export class ConnexionComponent implements OnInit {
  isLogged:any;
  connect:ConnexionService;
  email="test"
  password="test";
 
 // email:string;
  //password:string;


  constructor(connect:ConnexionService,private http:HttpClient,private router:Router) {
    this.connect=connect;
   }

  ngOnInit(): void {

  }

  
  connexion(formConnex:any){
    console.log("test connexion");
    console.log("test mail", formConnex.form.value.email);
    this.connect.login(formConnex.form.value.email, formConnex.form.value.password).subscribe(
    (data:any) =>{
        //this.email=formConnex.form.value.email;
        console.log("dans login");
        console.log("test email",this.email);
			
    
			});
			(error : any) => {
				console.log("une erreur c'est produite");
			}
  }

}
