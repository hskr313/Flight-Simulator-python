import { Component } from '@angular/core';
import { AuthService } from './security/auth.service';
import { User } from './security/models/user.model';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent {
  title = 'Flight-Simulator-Angular';

  constructor(private authService: AuthService) {}

  userProfile?: User | null;

  ngOnInit(): void {
    this.authService.userSubject.subscribe((data) => {
      this.userProfile = data;
    });
  }
}
