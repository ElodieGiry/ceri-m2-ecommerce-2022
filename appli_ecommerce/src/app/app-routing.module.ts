import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

import { AppComponent } from './app.component';
import { HeaderComponent } from 'src/app/header/header.component';
import { BodyComponent } from 'src/app/body/body.component';
import { DetailsComponent } from 'src/app/details/details.component';
import { ConnexionComponent } from './connexion/connexion.component';
import { InscriptionComponent } from './inscription/inscription.component';
const routes: Routes = [
  {path: "" , component : BodyComponent},
  {path: 'header' , component : HeaderComponent},
  {path: 'body' , component : BodyComponent},
  {path: 'details' , component : DetailsComponent},
  {path: 'details/:test/:testt' , component : DetailsComponent},
  {path: 'connexion' , component : ConnexionComponent},
  {path: 'inscription' , component : InscriptionComponent},


];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
