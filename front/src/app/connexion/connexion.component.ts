import { HttpClient } from '@angular/common/http';
import { Component, OnInit } from '@angular/core';
import {ConnexionService} from '../connexion.service';
import {Router} from '@angular/router';
import { Output, EventEmitter } from '@angular/core';

@Component({
  selector: 'app-connexion',
  templateUrl: './connexion.component.html',
  styleUrls: ['./connexion.component.css']
})
export class ConnexionComponent implements OnInit {
  //logged=false;
  connect:ConnexionService;
  email:any;
  password:any;
  connec:any
  value:any;
  emailAdmin:any;  
 
  logged: boolean = false;
 
 // email:string;
  //password:string;


  constructor(connect:ConnexionService,private http:HttpClient,private router:Router) {
    this.connect=connect;
   }

  ngOnInit(): void {
    

  }


  refreshPage() {
    window.location.reload();
  }
  
  connexion(formConnex:any){
    console.log("test connexion");
    console.log("test mail", formConnex.form.value.email);
    this.connect.login(formConnex.form.value.email, formConnex.form.value.password).subscribe(
    (data:any) =>{
        console.log("test data",data[0])   

        if(data[0]=="Erreur de connexion, le mail ou le mot de passe est incorrect"){   // ECHEC DE CONNEXION
          console.log("Erreur de connexion");
          this.logged=false;  
          
             
          
        }

        
        if(formConnex.form.value.email=="jcvinyl@gmail.com"){
          console.log("vous etes connecté en tant que admin")
          this.emailAdmin=1
          this.logged=true;
          this.connec=1;
          this.connect.setIsConnected(true);
          this.router.navigate(['/']);
          
        
          
          
          }
        
        else{    // CONNEXION OK
          console.log("Connexion réussi");  
          this.logged=true;
          this.connec=1;
          this.connect.setIsConnected(true);
          this.router.navigate(['/']);
          
          
        
          
          
        }
        
        console.log("dans login");
        console.log("data",data);
        console.log("test email",this.email);
        console.log("Bienvenue " + this.email + ", dernière connexion : "+localStorage.getItem("date")+" "+localStorage.getItem("time"));
        localStorage.setItem("time",this.email);   // stocke la date dans le localStorage
			  localStorage.setItem("date",new Date().toDateString());
			  localStorage.setItem("connecte",this.connec);
        localStorage.setItem("admin",this.emailAdmin);  
        console.log(localStorage.getItem("connecte"));
        this.value=(localStorage.getItem("connecte"));
       

    
			});
			(error : any) => {
				console.log("une erreur c'est produite");
			}
  }

}
