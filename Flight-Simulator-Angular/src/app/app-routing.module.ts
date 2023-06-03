import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import {AppLayoutComponent} from "./layout/app.layout.component";
import { LoginComponent } from './security/login/login.component';
import {RegisterComponent} from "./security/register/register.component";
import {NotfoundComponent} from "./security/notfound/notfound.component";

const routes: Routes = [
  {
    path: '', component: AppLayoutComponent,
    children: [

    ]
  },
  {path: 'login', component: LoginComponent},
  {path: 'register', component: RegisterComponent},
  {path: '**', component: NotfoundComponent}

];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
