import { Component } from '@angular/core';
import { FormControl, FormGroup, Validators } from '@angular/forms';
import { Router } from '@angular/router';
import { LayoutService } from 'src/app/layout/service/app.layout.service';
import { AuthService } from '../auth.service';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.scss']
})
export class LoginComponent {

  valCheck: string[] = ['remember'];

  fg: FormGroup = new FormGroup({
    email: new FormControl(null, Validators.required),
    password: new FormControl(null, Validators.required)
  })

  constructor(
    public $layoutService: LayoutService,
    private $router : Router,
    private $authservice: AuthService
    )
   { }

  onSubmit(){
    this.$authservice.login(this.fg.value as {}).subscribe(
      (data: any ) => {
        console.log(data)
        if (data) {
          this.$router.navigate(['/']);
        }
      }
    )

  }


}
