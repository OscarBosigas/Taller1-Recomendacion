import { Component, OnInit } from '@angular/core';
import { RegistroService } from '../registro/registro.service';
import { Usuario } from '../home/usuario';
import { LogInService } from '../home/login.service';
import { Artista } from './artista';
import { ArtistaService } from './artista.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-recomendacion',
  templateUrl: './recomendacion.component.html',
  styleUrls: ['./recomendacion.component.css']
})
export class RecomendacionComponent implements OnInit {
Object: any;

  constructor(private artistaService: ArtistaService, private login: LogInService, private route : Router) { }

  id: string = '';
  artistas: Array<Artista> =[new Artista('','','')]
  datos: any;
  nombres:  any;
  rate = 0;

  ngOnInit(): void {
    this.id = this.login.getId2();
    this.artistaService.getRecomendaciones(new Usuario(this.id,'','','','','',0)).subscribe(res =>{
      this.artistas = res
      this.datos = res[0].top_songs_by_artist;
      this.datos = this.datos.replace(/"/g, "'");
      this.datos = this.datos.replace("0'", "0");
      this.datos = this.datos.replace("I'M", "IM");
      this.datos = this.datos.replace(/'']/g, "']");
      this.datos = this.datos.replace(/\\/g, "");
      this.datos = this.datos.replace(/'s/g, "s");
      this.datos = this.datos.replace(/t'S/g, "S");
      this.datos = this.datos.replace(/n'T/g, "nT");
      this.datos = this.datos.replace(/n't/g, "nt");
      this.datos = this.datos.replace(/´/g, "");
      this.datos = this.datos.replace(/`/g, "");
      this.datos = this.datos.replace(/1'/g, "1 ");
      this.datos = this.datos.replace(/g'll/g, "ll");
      this.datos = this.datos.replace(/g'Ll/g, "Ll");
      this.datos = this.datos.replace(/'Ll/g, "Ll");
      this.datos = this.datos.replace("!", "");
      console.log(this.datos)
      
      console.log(this.datos.charAt(216))
      console.log(this.datos.charAt(217))
      console.log(this.datos.charAt(218))
      console.log(this.datos.charAt(219))
      this.datos = JSON.parse(this.datos.replace(/'/g, '"'));
      this.nombres = Object.keys(this.datos)
    })
  }

  rating(): void{
    this.id = this.login.getId2();
    this.login.postCalificar(new Usuario(this.id,'','','','','',this.rate)).subscribe(res =>{ 
      this.route.navigate(['recomendacion'])
    })
  }
}
