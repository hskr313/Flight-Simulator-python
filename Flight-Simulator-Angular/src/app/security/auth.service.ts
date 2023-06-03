import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Router } from '@angular/router';
import { BehaviorSubject, Observable, catchError, map, of } from 'rxjs';
import { environment } from 'src/environments/environment';
import { User } from './models/user.model';

@Injectable({
  providedIn: 'root'
})
export class AuthService {

  url: string = environment.url
  public userSubject = new BehaviorSubject<User | null>(null);

  constructor(
    private $router: Router,
    private $client: HttpClient,
    ) {
  }

  public get userValue(): User | null{
    return this.userSubject.value;
}


  login(login: {}): Observable<any>{
    return this.$client.post<any>(this.url+"/login", login)
    .pipe(map(data => {
      let user = data as User
      localStorage.setItem('current_user', JSON.stringify(user))

      this.userSubject.next(user);

      return true;
  }),
      catchError((error) => {
      console.log(error);
      return of(false);
  }));
  }

  register(user: User): Observable<User>{
    return this.$client.post<User>(this.url+"/register", user)
  }

}
