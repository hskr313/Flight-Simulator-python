import {Component, OnInit} from '@angular/core';
import {FormControl, FormGroup, Validators} from "@angular/forms";
import {AuthService} from "../auth.service";
import {User} from "../models/user.model";
import {Router} from "@angular/router";
import {LayoutService} from "../../layout/service/app.layout.service";

@Component({
  selector: 'app-register',
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.scss']
})
export class RegisterComponent implements OnInit{

  fg: FormGroup = new FormGroup({
    email: new FormControl(null,Validators.email),
    last_name: new FormControl(null,Validators.required),
    first_name: new FormControl(null,Validators.required),
    password: new FormControl(null,Validators.pattern("^(?=.*[A-Z])(?=.*[!@#$%^&*()])(?=.*[0-9]).{10,}$")),
    address: new FormGroup( {
      street: new FormControl(null, Validators.required),
      street_number: new FormControl(null, Validators.required),
      postal_code: new FormControl(null, Validators.required),
      city: new FormControl(null, Validators.required),
      country: new FormControl(null, Validators.required)
    }),
    pilot: new FormControl(false, Validators.required),
    roles: new FormControl(['USER'])
  })

  constructor(
    protected $layoutservice: LayoutService,
    private $authservice: AuthService,
    private $router: Router
  ) {
  }

  ngOnInit(): void {
    this.fg.get('pilot')?.valueChanges.subscribe( () => this.addPilotAttribute())
  }


  onSubmit(){
    this.$authservice.register(this.fg.value as User).subscribe(
      next =>
      this.$router.navigate(["/login"])
    )
    console.log(this.fg.value)
  }


  private addPilotAttribute() {
    const isChecked = this.fg.get('pilot')?.value
    if (isChecked){
      this.fg.addControl('license_number', new FormControl(null,Validators.required))
      this.fg.get('roles')?.patchValue(['PILOT','USER'])
    } else {
      this.fg.removeControl('license_number')
    }
  }
}
