import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { LogInService } from './login.service';
import { Usuario } from './usuario';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent implements OnInit {

  id: string = '';
  password: string = '';
  errorMessage: string = '';

  constructor(private login : LogInService, private route : Router) { }

  ngOnInit(): void {
  }

  onLogin() {
    this.login.logIn(new Usuario(this.id, this.password, '', '','','',0))
    .subscribe(res =>{
      this.route.navigate(['recomendacion'])
    }, error => {
      this.errorMessage = error;
      alert(this.errorMessage)
    }); 
  }

  onSingIn() {
      this.route.navigate(['registro'])
  }

}
