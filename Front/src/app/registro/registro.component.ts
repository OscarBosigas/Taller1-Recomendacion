import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { RegistroService } from './registro.service';
import { Usuario } from '../home/usuario';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-home',
  templateUrl: './registro.component.html',
  styleUrls: ['./registro.component.css']
})
export class RegistroComponent implements OnInit {

  id: string = '';
  password: string = '';
  age: string = '';
  country: string = '';
  registered: string  = '';
  gender: string  = '';
  errorMessage: string = '';

  constructor(private singup : RegistroService, private route : Router) { }

  ngOnInit(): void {
  }

  onSingIn() {
    if(this.id != "" && this.password != "" && this.age != "" && this.gender != "" && this.country != ""){ 
    this.singup.singIn(new Usuario(this.id, this.password, this.age, this.gender, this.country, this.registered))
    .subscribe(res =>{
      this.route.navigate([''])
    }, error => {
      this.errorMessage = error;
      alert(this.errorMessage)
    }); 
  }
  }

}
