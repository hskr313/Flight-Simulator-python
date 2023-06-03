import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ButtonModule } from 'primeng/button';
import { CheckboxModule } from 'primeng/checkbox';
import { ReactiveFormsModule } from '@angular/forms';
import { PasswordModule } from 'primeng/password';
import { InputTextModule } from 'primeng/inputtext';


import { LoginComponent } from './login/login.component';
import {PanelModule} from "primeng/panel";
import {RouterLink} from "@angular/router";
import {RippleModule} from "primeng/ripple";
import { RegisterComponent } from './register/register.component';
import {AppLayoutModule} from "../layout/app.layout.module";
import {InputSwitchModule} from "primeng/inputswitch";
import { NotfoundComponent } from './notfound/notfound.component';


@NgModule({
  declarations: [
    LoginComponent,
    RegisterComponent,
    NotfoundComponent
  ],
  imports: [
    CommonModule,
    ReactiveFormsModule,
    CheckboxModule,
    PasswordModule,
    InputTextModule,
    ButtonModule,
    PanelModule,
    RouterLink,
    RippleModule,
    AppLayoutModule,
    InputSwitchModule,
  ],
  exports: [
    LoginComponent,
    RegisterComponent
  ]
})
export class SecurityModule { }
