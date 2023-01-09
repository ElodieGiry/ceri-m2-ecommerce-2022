import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-header',
  templateUrl: './header.component.html',
  styleUrls: ['./header.component.css']
})


export class HeaderComponent implements OnInit {
  value:any;
  admin:any;
  
 
 

  constructor() { }

  ngOnInit(): void {
    this.value = localStorage.getItem('connecte');
    this.admin = localStorage.getItem('admin')
  }


  deco(){
    this.value==null
    

  }

}
