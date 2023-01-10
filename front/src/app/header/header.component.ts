import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import {Router} from '@angular/router';
import {ConnexionService} from '../connexion.service';
@Component({
  selector: 'app-header',
  templateUrl: './header.component.html',
  styleUrls: ['./header.component.css']
})


export class HeaderComponent implements OnInit {
  value:any;
  admin:any;
  serviceCo:ConnexionService;
  
 
  

  constructor(private http:HttpClient,private router:Router,private serviceCoo: ConnexionService) { 
    this.serviceCo=serviceCoo
  }

  ngOnInit(): void {
    this.value = localStorage.getItem('connecte');
    this.admin = localStorage.getItem('admin')
    
  }


  deco() {
    localStorage.removeItem('connecte');
    localStorage.removeItem('listeProd');
    this.serviceCo.setIsConnected(false);
    this.router.navigate(['/']);
    
  }
  

  

}
