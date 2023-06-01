import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import {AppLayoutComponent} from "./layout/app.layout.component";
import { LoginComponent } from './security/login/login.component';

const routes: Routes = [
  {
    path: '', component: AppLayoutComponent,
    children: [
    ]
  },
  {path: 'login', component: LoginComponent}

];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
